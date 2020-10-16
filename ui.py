# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("/*\n"
"AMOLED Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 22/01/2019, 12:33.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/AMOLED.qss\n"
"*/\n"
"QMainWindow {\n"
"    background-color:#000000;\n"
"}\n"
"QDialog {\n"
"    background-color:#000000;\n"
"}\n"
"QColorDialog {\n"
"    background-color:#000000;\n"
"}\n"
"QTextEdit {\n"
"    background-color:#000000;\n"
"    color: #a9b7c6;\n"
"}\n"
"QPlainTextEdit {\n"
"    selection-background-color:#f39c12;\n"
"    background-color:#000000;\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-width: 1px;\n"
"    color: #a9b7c6;\n"
"}\n"
"QPushButton{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #000000;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #e67e22;\n"
"    border-width: 1px;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #000000;\n"
"}\n"
"QToolButton {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #e67e22;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #000000;\n"
"}\n"
"QToolButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #e67e22;\n"
"    border-bottom-width: 2px;\n"
"    border-bottom-radius: 6px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-bottom: 1px;\n"
"    background-color: #000000;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #e67e22;\n"
"    border-bottom-width: 1px;\n"
"    border-bottom-radius: 6px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-bottom: 2px;\n"
"    background-color: #000000;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #e67e22;\n"
"    border-bottom-width: 2px;\n"
"    border-bottom-radius: 6px;\n"
"    border-style: solid;\n"
"    color: #e67e22;\n"
"    padding-bottom: 1px;\n"
"    background-color: #000000;\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 2px;\n"
"    border-bottom-radius: 6px;\n"
"    border-style: solid;\n"
"    color: #808086;\n"
"    padding-bottom: 1px;\n"
"    background-color: #000000;\n"
"}\n"
"QLineEdit {\n"
"    border-width: 1px; border-radius: 4px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    padding: 0 8px;\n"
"    color: #a9b7c6;\n"
"    background:#000000;\n"
"    selection-background-color:#007b50;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"QLabel {\n"
"    color: #a9b7c6;\n"
"}\n"
"QLCDNumber {\n"
"    color: #e67e22;\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color:#000000;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #e67e22;\n"
"    border-radius: 5px;\n"
"}\n"
"QMenuBar {\n"
"    background-color:#000000;\n"
"}\n"
"QMenuBar::item {\n"
"    color: #a9b7c6;\n"
"      spacing: 3px;\n"
"      padding: 1px 4px;\n"
"      background: #000000;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"      background:#000000;\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: #e67e22;\n"
"    border-bottom-color: transparent;\n"
"    border-left-width: 2px;\n"
"    color: #FFFFFF;\n"
"    padding-left:15px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color:#000000;\n"
"}\n"
"QMenu::item {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding-left:17px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color:#000000;\n"
"}\n"
"QMenu{\n"
"    background-color:#000000;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:#000000;\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(77,77,77);\n"
"        background-color:#000000;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #808086;\n"
"    padding: 3px;\n"
"    margin-left:3px;\n"
"    background-color:#000000;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #e67e22;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-left: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-left:3px;\n"
"    background-color:#000000;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: rgb(87, 97, 106);\n"
"    background-color:#000000;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #e67e22;\n"
"    color: #a9b7c6;\n"
"    background-color: #e67e22;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #e67e22;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QRadioButton {\n"
"    color: #a9b7c6;\n"
"    background-color:#000000;\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #e67e22;\n"
"    color: #a9b7c6;\n"
"    background-color: #e67e22;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #e67e22;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color:#000000;\n"
"}\n"
"QDoubleSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color:#000000;\n"
"}\n"
"QTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color:#000000;\n"
"}\n"
"QDateTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color:#000000;\n"
"}\n"
"QDateEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color:#000000;\n"
"}\n"
"QComboBox {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"}\n"
"QComboBox:editable {\n"
"    background: #1e1d23;\n"
"    color: #a9b7c6;\n"
"    selection-background-color:#000000;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"    selection-color: #FFFFFF;\n"
"    selection-background-color:#000000;\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"}\n"
"QFontComboBox {\n"
"    color: #a9b7c6;    \n"
"    background-color:#000000;\n"
"}\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color:#000000;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color:#000000;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color:#000000;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color:#000000;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: #e67e22;\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background: #e67e22;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 14px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    height: 14px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #e67e22;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background: #e67e22;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    max-height: 20px;\n"
"    background: rgb(0,0,0);\n"
"    border: 1px transparent grey;\n"
"    margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 0), stop:0.7 rgba(255, 0, 0, 0), stop:0.71 rgb(230, 126, 34), stop:1 rgb(230, 126, 34));\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0,0,0);\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgb(230, 126, 34);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0,0,0);\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid;\n"
"      border-color: rgb(0,0,0);\n"
"      background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 0), stop:0.7 rgba(255, 0, 0, 0), stop:0.71 rgb(230, 126, 34), stop:1 rgb(230, 126, 34));\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"      border: 1px solid;\n"
"      border-color: rgb(0,0,0);\n"
"    border-radius: 8px;\n"
"      background: rgb(230, 126, 34);\n"
"      height: 16px;\n"
"      width: 16px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"      border: 1px solid;\n"
"      border-color: grey;\n"
"    border-radius: 8px;\n"
"      background: rgb(230, 126, 34);\n"
"      height: 16px;\n"
"      width: 16px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid;\n"
"      border-color: rgb(0,0,0);\n"
"      background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 0), stop:0.7 rgba(255, 0, 0, 0), stop:0.71 rgb(230, 126, 34), stop:1 rgb(230, 126, 34));\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"      border: 1px solid;\n"
"      border-color: rgb(0,0,0);\n"
"    border-radius: 8px;\n"
"      background: rgb(230, 126, 34);\n"
"      height: 16px;\n"
"      width: 16px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"      border: 1px solid;\n"
"      border-color: grey;\n"
"    border-radius: 8px;\n"
"      background: rgb(230, 126, 34);\n"
"      height: 16px;\n"
"      width: 16px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"      border: 1px transparent grey;\n"
"      border-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"     background: rgb(0,0,0);\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"    border: 1px transparent grey;\n"
"    border-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"     background: rgb(0,0,0);\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"     background: none;\n"
"} \n"
"QScrollBar:vertical {\n"
"    max-width: 20px;\n"
"    background: rgb(0,0,0);\n"
"    border: 1px transparent grey;\n"
"    margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: 1px solid;\n"
"      border-color: rgb(0,0,0);\n"
"      background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 0), stop:0.7 rgba(255, 0, 0, 0), stop:0.71 rgb(230, 126, 34), stop:1 rgb(230, 126, 34));\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"      border: 1px solid;\n"
"      border-color: rgb(0,0,0);\n"
"    border-radius: 8px;\n"
"      background: rgb(230, 126, 34);\n"
"      height: 16px;\n"
"      width: 16px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"      border: 1px solid;\n"
"      border-color: grey;\n"
"    border-radius: 8px;\n"
"      background: rgb(230, 126, 34);\n"
"      height: 16px;\n"
"      width: 16px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"      border: 1px solid;\n"
"      border-color: rgb(0,0,0);\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 0), stop:0.7 rgba(255, 0, 0, 0), stop:0.71 rgb(230, 126, 34), stop:1 rgb(230, 126, 34));\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"      border: 1px solid;\n"
"      border-color: rgb(0,0,0);\n"
"    border-radius: 8px;\n"
"      background: rgb(230, 126, 34);\n"
"      height: 16px;\n"
"      width: 16px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"      border: 1px solid;\n"
"      border-color: grey;\n"
"    border-radius: 8px;\n"
"      background: rgb(230, 126, 34);\n"
"      height: 16px;\n"
"      width: 16px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"    QScrollBar::handle:vertical {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 0), stop:0.7 rgba(255, 0, 0, 0), stop:0.71 rgb(230, 126, 34), stop:1 rgb(230, 126, 34));\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0,0,0);\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(230, 126, 34);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0,0,0);\n"
"    min-heigth: 25px;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"    border: 1px transparent grey;\n"
"    border-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"     background: rgb(0,0,0);\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"      border: 1px transparent grey;\n"
"      border-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"     background: rgb(0,0,0);\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"      background: none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 841, 611))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777209))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(40, 190, 131, 41))
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 420, 181, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(140, 50, 441, 71))
        font = QtGui.QFont()
        font.setFamily("Jokerman")
        font.setPointSize(39)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(20, 260, 151, 41))
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.tab_3)
        self.progressBar.setGeometry(QtCore.QRect(90, 350, 591, 23))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet(".ProgressBar {\n"
"    position: relative;\n"
"    width: 78px;\n"
"    height:78px;\n"
"    margin:auto;\n"
"}\n"
"\n"
".ProgressBar .wBall {\n"
"    position: absolute;\n"
"    width: 74px;\n"
"    height: 74px;\n"
"    opacity: 0;\n"
"    transform: rotate(225deg);\n"
"        -o-transform: rotate(225deg);\n"
"        -ms-transform: rotate(225deg);\n"
"        -webkit-transform: rotate(225deg);\n"
"        -moz-transform: rotate(225deg);\n"
"    animation: orbit 6.96s infinite;\n"
"        -o-animation: orbit 6.96s infinite;\n"
"        -ms-animation: orbit 6.96s infinite;\n"
"        -webkit-animation: orbit 6.96s infinite;\n"
"        -moz-animation: orbit 6.96s infinite;\n"
"}\n"
"\n"
".ProgressBar .wBall .wInnerBall{\n"
"    position: absolute;\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    background: rgb(0,0,0);\n"
"    left:0px;\n"
"    top:0px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
".ProgressBar #wBall_1 {\n"
"    animation-delay: 1.52s;\n"
"        -o-animation-delay: 1.52s;\n"
"        -ms-animation-delay: 1.52s;\n"
"        -webkit-animation-delay: 1.52s;\n"
"        -moz-animation-delay: 1.52s;\n"
"}\n"
"\n"
".ProgressBar #wBall_2 {\n"
"    animation-delay: 0.3s;\n"
"        -o-animation-delay: 0.3s;\n"
"        -ms-animation-delay: 0.3s;\n"
"        -webkit-animation-delay: 0.3s;\n"
"        -moz-animation-delay: 0.3s;\n"
"}\n"
"\n"
".ProgressBar #wBall_3 {\n"
"    animation-delay: 0.61s;\n"
"        -o-animation-delay: 0.61s;\n"
"        -ms-animation-delay: 0.61s;\n"
"        -webkit-animation-delay: 0.61s;\n"
"        -moz-animation-delay: 0.61s;\n"
"}\n"
"\n"
".ProgressBar #wBall_4 {\n"
"    animation-delay: 0.91s;\n"
"        -o-animation-delay: 0.91s;\n"
"        -ms-animation-delay: 0.91s;\n"
"        -webkit-animation-delay: 0.91s;\n"
"        -moz-animation-delay: 0.91s;\n"
"}\n"
"\n"
".ProgressBar #wBall_5 {\n"
"    animation-delay: 1.22s;\n"
"        -o-animation-delay: 1.22s;\n"
"        -ms-animation-delay: 1.22s;\n"
"        -webkit-animation-delay: 1.22s;\n"
"        -moz-animation-delay: 1.22s;\n"
"}\n"
"\n"
"")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(190, 190, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_10.setGeometry(QtCore.QRect(570, 260, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(190, 260, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_11.setGeometry(QtCore.QRect(470, 420, 181, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(570, 80, 51, 71))
        font = QtGui.QFont()
        font.setFamily("Jokerman")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(80, 190, 111, 41))
        self.label_11.setObjectName("label_11")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 460, 181, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(210, 190, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(30, 260, 171, 41))
        self.label_12.setObjectName("label_12")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab)
        self.comboBox_3.setGeometry(QtCore.QRect(210, 260, 361, 41))
        self.comboBox_3.setObjectName("comboBox_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_7.setGeometry(QtCore.QRect(580, 190, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("")
        self.pushButton_7.setCheckable(False)
        self.pushButton_7.setAutoRepeat(False)
        self.pushButton_7.setAutoExclusive(False)
        self.pushButton_7.setAutoRepeatDelay(300)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(40, 320, 151, 51))
        self.label_13.setObjectName("label_13")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab)
        self.pushButton_9.setGeometry(QtCore.QRect(580, 330, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(210, 330, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(140, 50, 441, 71))
        font = QtGui.QFont()
        font.setFamily("Jokerman")
        font.setPointSize(39)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab)
        self.progressBar_2.setGeometry(QtCore.QRect(120, 410, 591, 23))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.progressBar_2.setFont(font)
        self.progressBar_2.setStyleSheet(".ProgressBar {\n"
"    position: relative;\n"
"    width: 78px;\n"
"    height:78px;\n"
"    margin:auto;\n"
"}\n"
"\n"
".ProgressBar .wBall {\n"
"    position: absolute;\n"
"    width: 74px;\n"
"    height: 74px;\n"
"    opacity: 0;\n"
"    transform: rotate(225deg);\n"
"        -o-transform: rotate(225deg);\n"
"        -ms-transform: rotate(225deg);\n"
"        -webkit-transform: rotate(225deg);\n"
"        -moz-transform: rotate(225deg);\n"
"    animation: orbit 6.96s infinite;\n"
"        -o-animation: orbit 6.96s infinite;\n"
"        -ms-animation: orbit 6.96s infinite;\n"
"        -webkit-animation: orbit 6.96s infinite;\n"
"        -moz-animation: orbit 6.96s infinite;\n"
"}\n"
"\n"
".ProgressBar .wBall .wInnerBall{\n"
"    position: absolute;\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    background: rgb(0,0,0);\n"
"    left:0px;\n"
"    top:0px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
".ProgressBar #wBall_1 {\n"
"    animation-delay: 1.52s;\n"
"        -o-animation-delay: 1.52s;\n"
"        -ms-animation-delay: 1.52s;\n"
"        -webkit-animation-delay: 1.52s;\n"
"        -moz-animation-delay: 1.52s;\n"
"}\n"
"\n"
".ProgressBar #wBall_2 {\n"
"    animation-delay: 0.3s;\n"
"        -o-animation-delay: 0.3s;\n"
"        -ms-animation-delay: 0.3s;\n"
"        -webkit-animation-delay: 0.3s;\n"
"        -moz-animation-delay: 0.3s;\n"
"}\n"
"\n"
".ProgressBar #wBall_3 {\n"
"    animation-delay: 0.61s;\n"
"        -o-animation-delay: 0.61s;\n"
"        -ms-animation-delay: 0.61s;\n"
"        -webkit-animation-delay: 0.61s;\n"
"        -moz-animation-delay: 0.61s;\n"
"}\n"
"\n"
".ProgressBar #wBall_4 {\n"
"    animation-delay: 0.91s;\n"
"        -o-animation-delay: 0.91s;\n"
"        -ms-animation-delay: 0.91s;\n"
"        -webkit-animation-delay: 0.91s;\n"
"        -moz-animation-delay: 0.91s;\n"
"}\n"
"\n"
".ProgressBar #wBall_5 {\n"
"    animation-delay: 1.22s;\n"
"        -o-animation-delay: 1.22s;\n"
"        -ms-animation-delay: 1.22s;\n"
"        -webkit-animation-delay: 1.22s;\n"
"        -moz-animation-delay: 1.22s;\n"
"}\n"
"\n"
"")
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab)
        self.pushButton_12.setGeometry(QtCore.QRect(490, 460, 181, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(570, 80, 51, 71))
        font = QtGui.QFont()
        font.setFamily("Jokerman")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_19.setGeometry(QtCore.QRect(580, 190, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("")
        self.pushButton_19.setCheckable(False)
        self.pushButton_19.setAutoRepeat(False)
        self.pushButton_19.setAutoExclusive(False)
        self.pushButton_19.setAutoRepeatDelay(300)
        self.pushButton_19.setFlat(False)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_20.setGeometry(QtCore.QRect(580, 330, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("")
        self.pushButton_20.setObjectName("pushButton_20")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(140, 50, 441, 71))
        font = QtGui.QFont()
        font.setFamily("Jokerman")
        font.setPointSize(39)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(40, 320, 151, 51))
        self.label_24.setObjectName("label_24")
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_21.setGeometry(QtCore.QRect(490, 460, 181, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("")
        self.pushButton_21.setObjectName("pushButton_21")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(70, 260, 171, 41))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(20, 190, 181, 41))
        self.label_26.setObjectName("label_26")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_5.setGeometry(QtCore.QRect(210, 260, 361, 41))
        self.comboBox_5.setObjectName("comboBox_5")
        self.progressBar_5 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_5.setGeometry(QtCore.QRect(120, 410, 591, 23))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.progressBar_5.setFont(font)
        self.progressBar_5.setStyleSheet(".ProgressBar {\n"
"    position: relative;\n"
"    width: 78px;\n"
"    height:78px;\n"
"    margin:auto;\n"
"}\n"
"\n"
".ProgressBar .wBall {\n"
"    position: absolute;\n"
"    width: 74px;\n"
"    height: 74px;\n"
"    opacity: 0;\n"
"    transform: rotate(225deg);\n"
"        -o-transform: rotate(225deg);\n"
"        -ms-transform: rotate(225deg);\n"
"        -webkit-transform: rotate(225deg);\n"
"        -moz-transform: rotate(225deg);\n"
"    animation: orbit 6.96s infinite;\n"
"        -o-animation: orbit 6.96s infinite;\n"
"        -ms-animation: orbit 6.96s infinite;\n"
"        -webkit-animation: orbit 6.96s infinite;\n"
"        -moz-animation: orbit 6.96s infinite;\n"
"}\n"
"\n"
".ProgressBar .wBall .wInnerBall{\n"
"    position: absolute;\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    background: rgb(0,0,0);\n"
"    left:0px;\n"
"    top:0px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
".ProgressBar #wBall_1 {\n"
"    animation-delay: 1.52s;\n"
"        -o-animation-delay: 1.52s;\n"
"        -ms-animation-delay: 1.52s;\n"
"        -webkit-animation-delay: 1.52s;\n"
"        -moz-animation-delay: 1.52s;\n"
"}\n"
"\n"
".ProgressBar #wBall_2 {\n"
"    animation-delay: 0.3s;\n"
"        -o-animation-delay: 0.3s;\n"
"        -ms-animation-delay: 0.3s;\n"
"        -webkit-animation-delay: 0.3s;\n"
"        -moz-animation-delay: 0.3s;\n"
"}\n"
"\n"
".ProgressBar #wBall_3 {\n"
"    animation-delay: 0.61s;\n"
"        -o-animation-delay: 0.61s;\n"
"        -ms-animation-delay: 0.61s;\n"
"        -webkit-animation-delay: 0.61s;\n"
"        -moz-animation-delay: 0.61s;\n"
"}\n"
"\n"
".ProgressBar #wBall_4 {\n"
"    animation-delay: 0.91s;\n"
"        -o-animation-delay: 0.91s;\n"
"        -ms-animation-delay: 0.91s;\n"
"        -webkit-animation-delay: 0.91s;\n"
"        -moz-animation-delay: 0.91s;\n"
"}\n"
"\n"
".ProgressBar #wBall_5 {\n"
"    animation-delay: 1.22s;\n"
"        -o-animation-delay: 1.22s;\n"
"        -ms-animation-delay: 1.22s;\n"
"        -webkit-animation-delay: 1.22s;\n"
"        -moz-animation-delay: 1.22s;\n"
"}\n"
"\n"
"")
        self.progressBar_5.setProperty("value", 0)
        self.progressBar_5.setObjectName("progressBar_5")
        self.pushButton_22 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_22.setGeometry(QtCore.QRect(150, 460, 181, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(210, 190, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_14.setGeometry(QtCore.QRect(210, 330, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setText("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(570, 80, 51, 71))
        font = QtGui.QFont()
        font.setFamily("Jokerman")
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Playlist URL</span></p></body></html>"))
        self.pushButton_5.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "Start Download"))
        self.label_8.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Jokerman\'; font-size:39pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "MM  Downloader"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Save Location</span></p></body></html>"))
        self.pushButton_10.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_10.setText(_translate("MainWindow", "Browse"))
        self.pushButton_11.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_11.setText(_translate("MainWindow", "Stop and Exit"))
        self.label_16.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Jokerman\'; font-size:39pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "V 2.0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Playlist Youtube Downloader"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Video URL</span></p></body></html>"))
        self.pushButton_6.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_6.setText(_translate("MainWindow", "Start Download"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Choose Quality</span></p></body></html>"))
        self.pushButton_7.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
        self.pushButton_7.setText(_translate("MainWindow", "Search"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Save Location</span></p></body></html>"))
        self.pushButton_9.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_9.setText(_translate("MainWindow", "Browse"))
        self.label_14.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Jokerman\'; font-size:39pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "MM  Downloader"))
        self.pushButton_12.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_12.setText(_translate("MainWindow", "Stop and Exit"))
        self.label_15.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Jokerman\'; font-size:39pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "V 2.0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Youtube Video Downloader"))
        self.pushButton_19.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
        self.pushButton_19.setText(_translate("MainWindow", "Search"))
        self.pushButton_20.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_20.setText(_translate("MainWindow", "Browse"))
        self.label_23.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Jokerman\'; font-size:39pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "MM  Downloader"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Save Location</span></p></body></html>"))
        self.pushButton_21.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_21.setText(_translate("MainWindow", "Stop and Exit"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Audio Type</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Music Video URL</span></p></body></html>"))
        self.pushButton_22.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_22.setText(_translate("MainWindow", "Start Download"))
        self.label_17.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Jokerman\'; font-size:39pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "V 2.0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Youtube Music Downloader"))
