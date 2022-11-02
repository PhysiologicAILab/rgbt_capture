# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rgbt_form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSlider,
    QTabWidget, QWidget)

class Ui_RGBT(object):
    def setupUi(self, RGBT):
        if not RGBT.objectName():
            RGBT.setObjectName(u"RGBT")
        RGBT.resize(1400, 953)
        RGBT.setMinimumSize(QSize(0, 0))
        RGBT.setMaximumSize(QSize(1400, 1000))
        self.gridLayout = QGridLayout(RGBT)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(RGBT)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setMaximumSize(QSize(680, 550))
        font = QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pix_label = QLabel(self.groupBox_2)
        self.pix_label.setObjectName(u"pix_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pix_label.sizePolicy().hasHeightForWidth())
        self.pix_label.setSizePolicy(sizePolicy1)
        self.pix_label.setMinimumSize(QSize(0, 0))
        self.pix_label.setMaximumSize(QSize(650, 520))
        self.pix_label.setFont(font)
        self.pix_label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.pix_label)


        self.gridLayout.addWidget(self.groupBox_2, 2, 1, 1, 1)

        self.groupBox = QGroupBox(RGBT)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setMaximumSize(QSize(1380, 250))
        self.groupBox.setFont(font)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.groupBox)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(1370, 250))
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 6, 1, 1)

        self.checkBox = QCheckBox(self.tab)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.checkBox, 0, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.tab)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.comboBox_2, 0, 7, 1, 1)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 0, 4, 4, 1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.tab)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.checkBox_2, 1, 0, 1, 1)

        self.recordButton = QPushButton(self.tab)
        self.recordButton.setObjectName(u"recordButton")
        sizePolicy.setHeightForWidth(self.recordButton.sizePolicy().hasHeightForWidth())
        self.recordButton.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.recordButton, 3, 1, 1, 1)

        self.comboBox_4 = QComboBox(self.tab)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_3.addWidget(self.comboBox_4, 1, 1, 1, 1)

        self.connectButton = QPushButton(self.tab)
        self.connectButton.setObjectName(u"connectButton")
        sizePolicy.setHeightForWidth(self.connectButton.sizePolicy().hasHeightForWidth())
        self.connectButton.setSizePolicy(sizePolicy)
        self.connectButton.setFont(font)

        self.gridLayout_3.addWidget(self.connectButton, 0, 1, 1, 1)

        self.acquireButton = QPushButton(self.tab)
        self.acquireButton.setObjectName(u"acquireButton")
        sizePolicy.setHeightForWidth(self.acquireButton.sizePolicy().hasHeightForWidth())
        self.acquireButton.setSizePolicy(sizePolicy)
        self.acquireButton.setFont(font)

        self.gridLayout_3.addWidget(self.acquireButton, 3, 0, 1, 1)

        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 1, 6, 1, 1)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 2, 6, 1, 1)

        self.comboBox = QComboBox(self.tab)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.comboBox, 2, 7, 1, 1)

        self.comboBox_3 = QComboBox(self.tab)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.comboBox_3, 1, 7, 1, 1)

        self.horizontalSlider = QSlider(self.tab)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.horizontalSlider, 3, 6, 1, 2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_4.addWidget(self.pushButton_2, 1, 0, 1, 2)

        self.browseButton = QPushButton(self.tab_2)
        self.browseButton.setObjectName(u"browseButton")

        self.gridLayout_4.addWidget(self.browseButton, 0, 0, 1, 1)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setItalic(True)
        self.label_3.setFont(font1)

        self.gridLayout_4.addWidget(self.label_3, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)

        self.groupBox_3 = QGroupBox(RGBT)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(680, 550))
        self.groupBox_3.setFont(font)
        self.pix_label_rgb = QLabel(self.groupBox_3)
        self.pix_label_rgb.setObjectName(u"pix_label_rgb")
        self.pix_label_rgb.setGeometry(QRect(10, 30, 650, 501))
        sizePolicy1.setHeightForWidth(self.pix_label_rgb.sizePolicy().hasHeightForWidth())
        self.pix_label_rgb.setSizePolicy(sizePolicy1)
        self.pix_label_rgb.setMaximumSize(QSize(650, 520))
        self.pix_label_rgb.setFont(font)

        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 1)

        self.label = QLabel(RGBT)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMaximumSize(QSize(1380, 70))
        font2 = QFont()
        font2.setPointSize(14)
        self.label.setFont(font2)
        self.label.setPixmap(QPixmap(u"../../../../Downloads/figure.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.log_label = QLabel(RGBT)
        self.log_label.setObjectName(u"log_label")
        self.log_label.setMaximumSize(QSize(1280, 30))

        self.gridLayout.addWidget(self.log_label, 3, 0, 1, 2)


        self.retranslateUi(RGBT)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(RGBT)
    # setupUi

    def retranslateUi(self, RGBT):
        RGBT.setWindowTitle(QCoreApplication.translate("RGBT", u"TIComp", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("RGBT", u"Thermal Image Streaming", None))
        self.pix_label.setText(QCoreApplication.translate("RGBT", u"Thermal Image streaming will appear here", None))
        self.groupBox.setTitle(QCoreApplication.translate("RGBT", u"Controls", None))
        self.label_7.setText(QCoreApplication.translate("RGBT", u"Pseudo-color Palette for Visualization", None))
        self.checkBox.setText(QCoreApplication.translate("RGBT", u"Capture Thermal", None))
        self.label_5.setText(QCoreApplication.translate("RGBT", u"Participant ID", None))
        self.checkBox_2.setText(QCoreApplication.translate("RGBT", u"Capture RGB", None))
        self.recordButton.setText(QCoreApplication.translate("RGBT", u"Record Frames", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("RGBT", u"Select RGB Camera", None))

        self.connectButton.setText(QCoreApplication.translate("RGBT", u"Scan and Connect Thermal Camera", None))
        self.acquireButton.setText(QCoreApplication.translate("RGBT", u"Start Live Streaming", None))
        self.label_8.setText(QCoreApplication.translate("RGBT", u"Frame Rate", None))
        self.label_6.setText(QCoreApplication.translate("RGBT", u"Focus Type", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("RGBT", u"Max", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("RGBT", u"1", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("RGBT", u"2", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("RGBT", u"5", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("RGBT", u"10", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("RGBT", u"15", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("RGBT", u"25", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("RGBT", u"30", None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate("RGBT", u"60", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("RGBT", u"Live Acquisition", None))
        self.pushButton_2.setText(QCoreApplication.translate("RGBT", u"Start Playing", None))
        self.browseButton.setText(QCoreApplication.translate("RGBT", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("RGBT", u"Directory Path", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("RGBT", u"Recorded Data", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("RGBT", u"RGB Image Streaming", None))
        self.pix_label_rgb.setText(QCoreApplication.translate("RGBT", u"RGB Image streaming will appear here", None))
        self.label.setText("")
        self.log_label.setText(QCoreApplication.translate("RGBT", u"Logging area", None))
    # retranslateUi

