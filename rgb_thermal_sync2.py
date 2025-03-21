import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
import argparse
import shutil
from datetime import datetime


def main(args_parser):

    datapath = args_parser.datapath
    print("Datapath: ", datapath)

    if not os.path.exists(datapath):
        print("Specified path for data [", datapath,"] does not exist. Please check the path")
        return
    else:
        datapath_thermal = os.path.join(datapath, "Thermal_All")
        datapath_rgb = os.path.join(datapath, "RGB_All")

    if not os.path.exists(datapath_thermal):
        print("Thermal frames not found at: ", datapath_thermal)
        return
    elif not os.path.exists(datapath_rgb):
        print("Color frames not found at: ", datapath_rgb)
        return
    else:
        pass

    savepath_rgb = os.path.join(datapath, "RGB")
    savepath_therm = os.path.join(datapath, "Thermal")
    savepath_rgb_video = os.path.join(datapath, "video")


    list_files_thermal = os.listdir(datapath_thermal)
    # print(list_files_thermal)
    n_frames_thermal = len(list_files_thermal)
    list_files_thermal = sorted(list_files_thermal)

    list_files_rgb = os.listdir(datapath_rgb)
    # print(list_files_rgb)
    n_frames_rgb = len(list_files_rgb)
    list_files_rgb = sorted(list_files_rgb)
    
    therm_images = []
    rgb_images = []
    therm_time_stamp_list = []
    rgb_time_stamp_list = []

    # Thermal - Obtained FPS
    ts_start_thermal = os.path.splitext(list_files_thermal[0])[0].split('_')[1:]
    start_time_thermal = datetime.fromtimestamp(float(ts_start_thermal[0] + '.' + ts_start_thermal[1]))
    ts_end_thermal = os.path.splitext(list_files_thermal[-1])[0].split('_')[1:]
    end_time_thermal = datetime.fromtimestamp(float(ts_end_thermal[0] + '.' + ts_end_thermal[1]))
    total_secs = (end_time_thermal - start_time_thermal).total_seconds()
    print("Datapath - thermal:", datapath_thermal)
    print("Start time (Thermal):", start_time_thermal)
    print("End time (Thermal):", end_time_thermal)
    print("Total Frames (Thermal):", n_frames_thermal)
    print("Total seconds (Thermal):", total_secs)
    fps_thermal = int(np.round(float(n_frames_thermal)/total_secs))
    print("Obtained FPS - Thermal: ", fps_thermal)

    # RGB - Obtained FPS
    ts_start_rgb = os.path.splitext(list_files_rgb[0])[0].split('_')[1:]
    start_time_rgb = datetime.fromtimestamp(float(ts_start_rgb[0] + '.' + ts_start_rgb[1]))
    ts_end_rgb = os.path.splitext(list_files_rgb[-1])[0].split('_')[1:]
    end_time_rgb = datetime.fromtimestamp(float(ts_end_rgb[0] + '.' + ts_end_rgb[1]))
    total_secs = (end_time_rgb - start_time_rgb).total_seconds()
    print('*'*50)
    print("Datapath - rgb:", datapath_rgb)
    print("Start time (RGB):", start_time_rgb)
    print("End time (RGB):", end_time_rgb)
    print("Total Frames (RGB):", n_frames_rgb)
    print("Total seconds (RGB):", total_secs)
    fps_rgb = int(np.round(float(n_frames_rgb)/total_secs))
    print("Obtained FPS - RGB: ", fps_rgb)


    for i in range(len(list_files_thermal)):
        fn = list_files_thermal[i]
        if os.path.isfile(os.path.join(datapath_thermal, fn)):
            fname, _ = os.path.splitext(fn)
            ts = fname.split('_')[1:]
            ts = float(ts[0] + '.' + ts[1])
            therm_images.append(fn)
            therm_time_stamp_list.append(ts)

    for i in range(len(list_files_rgb)):
        fn = list_files_rgb[i]
        if os.path.isfile(os.path.join(datapath_rgb, fn)):
            fname, _ = os.path.splitext(fn)
            ts = fname.split('_')[1:]
            ts = float(ts[0] + '.' + ts[1])
            rgb_images.append(fn)
            rgb_time_stamp_list.append(ts)

    therm_time_stamp_list = np.asarray(therm_time_stamp_list)
    rgb_time_stamp_list = np.asarray(rgb_time_stamp_list)


    if not os.path.exists(savepath_rgb_video):
        os.makedirs(savepath_rgb_video)

    if fps_rgb > fps_thermal:

        if not os.path.exists(savepath_rgb):
            os.makedirs(savepath_rgb)

        for i in range(len(therm_images)):

            th_ts = therm_time_stamp_list[i]
            diff_ts = np.abs(th_ts + 0.4 - rgb_time_stamp_list)
            rgb_indx = int(np.argmin(diff_ts))
            print(i, '--', rgb_indx, ':', min(diff_ts), "\r", end="")

            save_fn, _ = os.path.splitext(therm_images[i])
            _, rgb_ext = os.path.splitext(rgb_images[rgb_indx])

            # Copy time matched RGB frame 
            shutil.copyfile(os.path.join(datapath_rgb, rgb_images[rgb_indx]), os.path.join(savepath_rgb, rgb_images[rgb_indx]))
            shutil.move(os.path.join(savepath_rgb, rgb_images[rgb_indx]), os.path.join(savepath_rgb, save_fn + rgb_ext))

            th_img = np.load(os.path.join(datapath_thermal, therm_images[i]))
            rgb_img = cv2.imread(os.path.join(datapath_rgb, rgb_images[rgb_indx]))
            rgb_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)

            fig, ax = plt.subplots(1, 2, figsize=(10, 4))
            ax[0].imshow(th_img, cmap='magma')
            ax[0].axis('off')
            ax[1].imshow(rgb_img)
            ax[1].axis('off')
            plt.tight_layout()
            plt.savefig(os.path.join(savepath_rgb_video, save_fn + '.jpg'))
            plt.close()
            fig.clear()

            # if i > 100:
            #     break
    else:

        if not os.path.exists(savepath_therm):
            os.makedirs(savepath_therm)

        for i in range(len(rgb_images)):

            th_ts = rgb_time_stamp_list[i]
            diff_ts = np.abs(th_ts - therm_time_stamp_list)
            therm_indx = int(np.argmin(diff_ts))
            print(i, '--', therm_indx, ':', min(diff_ts), "\r", end="")

            save_fn, _ = os.path.splitext(rgb_images[i])
            _, therm_ext = os.path.splitext(therm_images[therm_indx])

            # Copy time matched thermal frame 
            shutil.copyfile(os.path.join(datapath_thermal, therm_images[therm_indx]), os.path.join(savepath_therm, therm_images[therm_indx]))
            shutil.move(os.path.join(savepath_therm, therm_images[therm_indx]), os.path.join(savepath_therm, save_fn + therm_ext))

            th_img = np.load(os.path.join(datapath_thermal, therm_images[therm_indx]))
            rgb_img = cv2.imread(os.path.join(datapath_rgb, rgb_images[i]))
            rgb_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)

            fig, ax = plt.subplots(1, 2, figsize=(10, 4))
            ax[0].imshow(th_img, cmap='magma')
            ax[0].axis('off')
            ax[1].imshow(rgb_img)
            ax[1].axis('off')
            plt.tight_layout()
            plt.savefig(os.path.join(savepath_rgb_video, save_fn + '.jpg'))
            plt.close()
            fig.clear()

            # if i > 100:
            #     break



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--datapath', default=None,
                        type=str, dest='datapath', help='The path with RGB and Color frames.')
    parser.add_argument('REMAIN', nargs='*')
    args_parser = parser.parse_args()

    main(args_parser=args_parser)
