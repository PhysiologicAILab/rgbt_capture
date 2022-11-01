# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QTabWidget, QWidget)

class Ui_TIComp(object):
    def setupUi(self, TIComp):
        if not TIComp.objectName():
            TIComp.setObjectName(u"TIComp")
        TIComp.resize(1208, 1000)
        TIComp.setMinimumSize(QSize(0, 0))
        TIComp.setMaximumSize(QSize(1208, 1000))
        self.gridLayout = QGridLayout(TIComp)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(TIComp)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setMaximumSize(QSize(350, 500))
        font = QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.groupBox)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.signalExtractionButton = QPushButton(self.tab)
        self.signalExtractionButton.setObjectName(u"signalExtractionButton")
        sizePolicy.setHeightForWidth(self.signalExtractionButton.sizePolicy().hasHeightForWidth())
        self.signalExtractionButton.setSizePolicy(sizePolicy)
        self.signalExtractionButton.setFont(font)

        self.gridLayout_3.addWidget(self.signalExtractionButton, 5, 0, 1, 2)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)

        self.connectButton = QPushButton(self.tab)
        self.connectButton.setObjectName(u"connectButton")
        sizePolicy.setHeightForWidth(self.connectButton.sizePolicy().hasHeightForWidth())
        self.connectButton.setSizePolicy(sizePolicy)
        self.connectButton.setFont(font)

        self.gridLayout_3.addWidget(self.connectButton, 0, 0, 1, 1)

        self.acquireButton = QPushButton(self.tab)
        self.acquireButton.setObjectName(u"acquireButton")
        sizePolicy.setHeightForWidth(self.acquireButton.sizePolicy().hasHeightForWidth())
        self.acquireButton.setSizePolicy(sizePolicy)
        self.acquireButton.setFont(font)

        self.gridLayout_3.addWidget(self.acquireButton, 1, 0, 1, 1)

        self.recordButton = QPushButton(self.tab)
        self.recordButton.setObjectName(u"recordButton")
        sizePolicy.setHeightForWidth(self.recordButton.sizePolicy().hasHeightForWidth())
        self.recordButton.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.recordButton, 1, 1, 1, 1)

        self.segButton = QPushButton(self.tab)
        self.segButton.setObjectName(u"segButton")
        sizePolicy.setHeightForWidth(self.segButton.sizePolicy().hasHeightForWidth())
        self.segButton.setSizePolicy(sizePolicy)
        self.segButton.setFont(font)

        self.gridLayout_3.addWidget(self.segButton, 4, 1, 1, 1)

        self.selectModelButton = QComboBox(self.tab)
        self.selectModelButton.addItem("")
        self.selectModelButton.addItem("")
        self.selectModelButton.addItem("")
        self.selectModelButton.setObjectName(u"selectModelButton")
        sizePolicy.setHeightForWidth(self.selectModelButton.sizePolicy().hasHeightForWidth())
        self.selectModelButton.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.selectModelButton, 4, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
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

        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_4.addWidget(self.pushButton_2, 1, 0, 1, 2)

        self.pushButton_3 = QPushButton(self.tab_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_4.addWidget(self.pushButton_3, 2, 0, 1, 2)

        self.pushButton_4 = QPushButton(self.tab_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_4.addWidget(self.pushButton_4, 3, 0, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.label = QLabel(TIComp)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(1280, 60))
        font2 = QFont()
        font2.setPointSize(14)
        self.label.setFont(font2)
        self.label.setPixmap(QPixmap(u"images/banner.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.groupBox_3 = QGroupBox(TIComp)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QSize(0, 0))
        self.groupBox_3.setMaximumSize(QSize(1280, 350))
        self.groupBox_3.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.graphicsView_resp = QGraphicsView(self.groupBox_3)
        self.graphicsView_resp.setObjectName(u"graphicsView_resp")
        sizePolicy.setHeightForWidth(self.graphicsView_resp.sizePolicy().hasHeightForWidth())
        self.graphicsView_resp.setSizePolicy(sizePolicy)
        self.graphicsView_resp.setMinimumSize(QSize(0, 0))
        self.graphicsView_resp.setMaximumSize(QSize(1270, 350))
        self.graphicsView_resp.setFont(font2)
        self.graphicsView_resp.setResizeAnchor(QGraphicsView.NoAnchor)

        self.horizontalLayout_2.addWidget(self.graphicsView_resp)


        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 2)

        self.groupBox_2 = QGroupBox(TIComp)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(512, 384))
        self.groupBox_2.setMaximumSize(QSize(900, 600))
        self.groupBox_2.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pix_label = QLabel(self.groupBox_2)
        self.pix_label.setObjectName(u"pix_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pix_label.sizePolicy().hasHeightForWidth())
        self.pix_label.setSizePolicy(sizePolicy2)
        self.pix_label.setMinimumSize(QSize(0, 0))
        self.pix_label.setMaximumSize(QSize(800, 600))
        self.pix_label.setFont(font)
        self.pix_label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.pix_label)


        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)

        self.log_label = QLabel(TIComp)
        self.log_label.setObjectName(u"log_label")
        self.log_label.setMaximumSize(QSize(1280, 30))

        self.gridLayout.addWidget(self.log_label, 3, 0, 1, 2)


        self.retranslateUi(TIComp)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TIComp)
    # setupUi

    def retranslateUi(self, TIComp):
        TIComp.setWindowTitle(QCoreApplication.translate("TIComp", u"TIComp", None))
        self.groupBox.setTitle(QCoreApplication.translate("TIComp", u"Controls", None))
        self.signalExtractionButton.setText(QCoreApplication.translate("TIComp", u"Extract and Plot \n"
"Nostril Temperature Signal", None))
        self.label_2.setText(QCoreApplication.translate("TIComp", u"<html><head/><body><p>Camera Serial </p><p>Number: ####</p></body></html>", None))
        self.connectButton.setText(QCoreApplication.translate("TIComp", u"Scan and Connect \n"
"Thermal Camera", None))
        self.acquireButton.setText(QCoreApplication.translate("TIComp", u"Start Live\n"
"Streaming", None))
        self.recordButton.setText(QCoreApplication.translate("TIComp", u"Record\n"
"Frames", None))
        self.segButton.setText(QCoreApplication.translate("TIComp", u"Perform\n"
"Segmentation", None))
        self.selectModelButton.setItemText(0, QCoreApplication.translate("TIComp", u"Select Model", None))
        self.selectModelButton.setItemText(1, QCoreApplication.translate("TIComp", u"SAM-CL", None))
        self.selectModelButton.setItemText(2, QCoreApplication.translate("TIComp", u"SOTA", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("TIComp", u"Live Acquisition", None))
        self.browseButton.setText(QCoreApplication.translate("TIComp", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("TIComp", u"Directory Path", None))
        self.pushButton_2.setText(QCoreApplication.translate("TIComp", u"Start Playing", None))
        self.pushButton_3.setText(QCoreApplication.translate("TIComp", u"Perform Segmentation", None))
        self.pushButton_4.setText(QCoreApplication.translate("TIComp", u"Extract and Plot \n"
"Nostril Temperature Signal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("TIComp", u"Recorded Data", None))
        self.label.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("TIComp", u"Extracted Signal", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TIComp", u"Live Thermal Image Acquisition", None))
        self.pix_label.setText(QCoreApplication.translate("TIComp", u"Image streaming will appear here", None))
        self.log_label.setText(QCoreApplication.translate("TIComp", u"Logging area", None))
    # retranslateUi

