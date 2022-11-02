# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import threading
import time
import datetime
import numpy as np
import copy
import argparse

import cv2
from utils.flircamera import CameraManager as tcam
from utils.signal_processing_lib import lFilter

from PySide6.QtWidgets import QApplication, QWidget, QGraphicsScene
from PySide6.QtCore import QFile, QObject, Signal, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap, QImage
import pyqtgraph as pg
from pathlib import Path
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import cv2

global camera_connect_status, acquisition_status, live_streaming_status, keep_acquisition_thread
global recording_status, save_path, num_frames, subdir_path
global capture_thermal, capture_rgb

acquisition_status = False
live_streaming_status = False
recording_status = False
camera_connect_status = False
keep_acquisition_thread = True
save_path = "recorded_frames"
num_frames = 0

class RGBTCam(QWidget):
    def __init__(self, args_parser):
        super(RGBTCam, self).__init__()
        self.load_ui(args_parser)

    def load_ui(self, args_parser):
        self.args_parser = args_parser
        
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "rgbt_form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        
        self.tcamObj = tcam()

        # input_size = self.configer.get('test', 'data_transformer')['input_size']
        self.seg_img_width = 640 #input_size[0]
        self.seg_img_height = 512 #input_size[1]

        self.ui.checkBox_Th.stateChanged.connect(lambda:self.btnstate(self.ui.checkBox_Th))
        self.ui.checkBox_RGB.stateChanged.connect(lambda:self.btnstate(self.ui.checkBox_RGB))

        self.ui.connectButton_Thermal.pressed.connect(self.scan_and_connect_camera)
        self.ui.acquireButton.pressed.connect(self.control_acquisition)
        self.ui.recordButton.pressed.connect(self.control_recording)

        # self.ui.browseButton.pressed.connect(self.browse_recorded_dir)
        self.ui.acquireButton.setEnabled(False)
        self.ui.recordButton.setEnabled(False)

        # self.fps = 50.0
        self.fps = 30.0

        self.imgAcqLoop = threading.Thread(name='imgAcqLoop', target=capture_frame_thread, daemon=True, args=(
            self.tcamObj, self.updatePixmap, self.updateLog))
        self.imgAcqLoop.start()

        self.imgAcqLoop_rgb = threading.Thread(name='imgAcqLoop_rgb', target=capture_frame_thread_rgb, daemon=True, args=(
            self.updateRGBPixmap, self.updateLog))
        self.imgAcqLoop_rgb.start()

        ui_file.close()

    def closeEvent(self, event):
        global camera_connect_status, acquisition_status, keep_acquisition_thread
        keep_acquisition_thread = False
        print("Please wait while camera is released...")
        time.sleep(0.5)
        if camera_connect_status and acquisition_status:
            self.tcamObj.release_camera(acquisition_status)

    def btnstate(self, b):
        global capture_thermal, capture_rgb

        if b.text() == "Capture Thermal":
            if b.isChecked() == True:
                capture_thermal = True
                self.updateLog(b.text()+" is selected")
                self.ui.connectButton_Thermal.setEnabled(True)
            else:
                capture_thermal = False
                self.updateLog(b.text()+" is deselected")
                self.ui.connectButton_Thermal.setEnabled(False)
				
        if b.text() == "Capture RGB":
            if b.isChecked() == True:
                capture_rgb = True
                self.updateLog(b.text()+" is selected")
                self.ui.comboBox_RGB_Cam.setEnabled(True)
            else:
                capture_rgb = False
                self.updateLog(b.text()+" is deselected")
                self.ui.comboBox_RGB_Cam.setEnabled(False)

    def scan_and_connect_camera(self):
        global acquisition_status, camera_connect_status

        if camera_connect_status == False:
            if self.tcamObj.get_camera():
                self.cam_serial_number, self.cam_img_width, self.cam_img_height = self.tcamObj.setup_camera()
                if "error" not in self.cam_serial_number.lower():
                    self.ui.connectButton_Thermal.setText("Disconnect Camera")
                    self.updateLog("Camera Serial Number: " + self.cam_serial_number)
                    camera_connect_status = True
                    self.img_width = self.seg_img_width
                    self.img_height = self.seg_img_height
                else:
                    self.updateLog("Error Setting Up Camera: " + self.cam_serial_number)

        if camera_connect_status:
            if acquisition_status == False:
                self.ui.acquireButton.setEnabled(True)
                acquisition_status = True
                self.updateLog("Camera Serial Number: " + self.cam_serial_number)
                self.ui.connectButton_Thermal.setText("Disconnect Camera")
                self.tcamObj.begin_acquisition()
            else:
                self.ui.acquireButton.setEnabled(False)
                self.tcamObj.end_acquisition()
                acquisition_status = False
                self.updateLog('No thermal camera connected')
                self.ui.connectButton_Thermal.setText("Scan and Connect Thermal Camera")

    def control_acquisition(self):
        global live_streaming_status
        if live_streaming_status == False:
            self.ui.acquireButton.setText('Stop Live Streaming')
            live_streaming_status = True
            self.ui.recordButton.setEnabled(True)
            self.updateLog("Acquisition started")

        else:
            live_streaming_status = False
            self.ui.recordButton.setEnabled(False)
            self.ui.acquireButton.setText('Start Live Streaming')
            self.updateLog("Acquisition stopped")

    def control_recording(self):
        global save_path, recording_status, subdir_path
        if recording_status == False:
            timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H-%M-%S')
            subdir_path = os.path.join(save_path, timestamp)
            if not os.path.exists(subdir_path):
                os.makedirs(subdir_path)
            self.ui.recordButton.setText('Stop Recording')
            recording_status = True
            self.updateLog("Recording started")

        else:
            recording_status = False
            self.ui.recordButton.setText('Record Frames')
            self.updateLog("Recording stopped")

    def updatePixmap(self, data_list):
        canvas, width, height = data_list        
        qimg1 = QImage(canvas.buffer_rgba(), width, height, QImage.Format_RGBA8888)
        self.ui.pix_label.setPixmap(QPixmap.fromImage(qimg1))


    def updateRGBPixmap(self, data_list):
        rgb_matrix, rgb_ret = data_list

        if rgb_ret:
            rgbImage = cv2.cvtColor(rgb_matrix, cv2.COLOR_BGR2RGB)
            h, w, ch = rgbImage.shape
            bytesPerLine = ch * w
            qimg2 = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
            qimg2 = qimg2.scaled(640, 480, Qt.KeepAspectRatio)
            self.ui.pix_label_rgb.setPixmap(QPixmap.fromImage(qimg2))


    def updateLog(self, message):
        self.ui.log_label.setText(message)


# Setup a signal slot mechanism, to send data to GUI in a thread-safe way.
class Communicate(QObject):
    data_signal = Signal(list)
    data_signal_rgb = Signal(list)
    save_signal = Signal(np.ndarray)
    save_signal_rgb = Signal(np.ndarray)
    status_signal = Signal(str)

def save_frame(thermal_matrix):
    global num_frames, subdir_path
    num_frames += 1
    np.save(os.path.join(subdir_path, f'{num_frames:04d}' + '.npy'), thermal_matrix)
    

def save_frame_rgb(rgb_matrix):
    global num_frames, subdir_path
    num_frames += 1
    cv2.imwrite(os.path.join(subdir_path, f'{num_frames:04d}' + '.jpg'), rgb_matrix)


def capture_frame_thread_rgb(updateRGBPixmap, updateLog):
    # Setup the signal-slot mechanism.
    mySrc = Communicate()
    mySrc.data_signal_rgb.connect(updateRGBPixmap)
    mySrc.status_signal.connect(updateLog)
    mySrc.save_signal_rgb.connect(save_frame_rgb)

    global live_streaming_status, acquisition_status, camera_connect_status, keep_acquisition_thread
    global recording_status
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    focus = 50  # min: 0, max: 255, increment:5
    cam.set(28, focus)

    while True:
        if keep_acquisition_thread:
            if camera_connect_status and acquisition_status and live_streaming_status:
                t1 = time.time()
                info_str = ""
                rgb_ret, rgb_matrix = cam.read()

                if rgb_ret:
                    mySrc.data_signal_rgb.emit([rgb_matrix, rgb_ret])

                    if recording_status:
                        mySrc.save_signal_rgb.emit(rgb_matrix)

                info_str = "RGB Frame acquisition status: " + str(rgb_ret) + "; " + info_str
                # time.sleep(0.05)
                t2 = time.time()
                t_elapsed = str(t2 - t1)
                info_str = info_str + "; total_time_per_frame RGB: " + t_elapsed
                mySrc.status_signal.emit(info_str)

            else:
                time.sleep(0.25)
        else:
            mySrc.status_signal.emit("Acquisition thread termination. Please restart the application...")
            break

def capture_frame_thread(tcamObj, updatePixmap, updateLog):
    # Setup the signal-slot mechanism.
    mySrc = Communicate()
    mySrc.data_signal.connect(updatePixmap)
    mySrc.status_signal.connect(updateLog)
    mySrc.save_signal.connect(save_frame)

    global live_streaming_status, acquisition_status, camera_connect_status, keep_acquisition_thread
    global recording_status

    while True:
        if keep_acquisition_thread:
            if camera_connect_status and acquisition_status and live_streaming_status:
                t1 = time.time()
                info_str = ""
                thermal_matrix, frame_status = tcamObj.capture_frame()

                if frame_status == "valid" and thermal_matrix.size > 0:
                    min_temp = np.round(np.min(thermal_matrix), 2)
                    max_temp = np.round(np.max(thermal_matrix), 2)
 
                    if recording_status:
                        mySrc.save_signal.emit(thermal_matrix)

                        info_str = "[Min Temp, Max Temp] = " + str([min_temp, max_temp])

                    fig = Figure(tight_layout=True)
                    canvas = FigureCanvas(fig)
                    ax = fig.add_subplot(111)
                    # ax.imshow(thermal_matrix, cmap='nipy_spectral')
                    # ax.imshow(thermal_matrix, cmap='rainbow')
                    ax.imshow(thermal_matrix, cmap='plasma')
                    ax.set_axis_off()
                    canvas.draw()
                    width, height = fig.figbbox.width, fig.figbbox.height
                    mySrc.data_signal.emit([canvas, width, height])
                
                info_str = "Frame acquisition status: " + frame_status + "; " + info_str                
                # time.sleep(0.05)
                t2 = time.time()
                t_elapsed = str(t2 - t1)
                info_str = info_str + "; total_time_per_frame: " + t_elapsed
                mySrc.status_signal.emit(info_str)

            else:
                time.sleep(0.25)
        else:
            mySrc.status_signal.emit("Acquisition thread termination. Please restart the application...")
            break


def str2bool(v):
    """ Usage:
    parser.add_argument('--pretrained', type=str2bool, nargs='?', const=True,
                        dest='pretrained', help='Whether to use pretrained models.')
    """
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Unsupported value encountered.')


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--savepath', default=None, nargs='+', type=str,
                        dest='savepath', help='The path to save frames.')

    parser.add_argument('REMAIN', nargs='*')

    args_parser = parser.parse_args()

    app = QApplication([])
    widget = RGBTCam(args_parser=args_parser)
    widget.show()
    sys.exit(app.exec())
