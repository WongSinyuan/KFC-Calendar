# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_calendar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(819, 601)
        icon = QIcon()
        iconThemeName = u"12"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.horizontalLayoutWidget = QWidget(self.central_widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(190, 60, 411, 30))
        self.top_date_layout = QHBoxLayout(self.horizontalLayoutWidget)
        self.top_date_layout.setObjectName(u"top_date_layout")
        self.top_date_layout.setContentsMargins(0, 0, 0, 0)
        self.left_button = QPushButton(self.horizontalLayoutWidget)
        self.left_button.setObjectName(u"left_button")
        self.left_button.setFocusPolicy(Qt.NoFocus)
        self.left_button.setCheckable(False)
        self.left_button.setChecked(False)
        self.left_button.setAutoRepeat(False)
        self.left_button.setAutoExclusive(False)

        self.top_date_layout.addWidget(self.left_button)

        self.year_edit = QSpinBox(self.horizontalLayoutWidget)
        self.year_edit.setObjectName(u"year_edit")
        self.year_edit.setFocusPolicy(Qt.NoFocus)
        self.year_edit.setAlignment(Qt.AlignCenter)
        self.year_edit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.year_edit.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.year_edit.setMinimum(0)
        self.year_edit.setMaximum(9999)
        self.year_edit.setStepType(QAbstractSpinBox.DefaultStepType)
        self.year_edit.setValue(0)

        self.top_date_layout.addWidget(self.year_edit)

        self.month_edit = QSpinBox(self.horizontalLayoutWidget)
        self.month_edit.setObjectName(u"month_edit")
        self.month_edit.setEnabled(True)
        self.month_edit.setFocusPolicy(Qt.NoFocus)
        self.month_edit.setAcceptDrops(False)
        self.month_edit.setWrapping(True)
        self.month_edit.setFrame(True)
        self.month_edit.setAlignment(Qt.AlignCenter)
        self.month_edit.setReadOnly(False)
        self.month_edit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.month_edit.setAccelerated(False)
        self.month_edit.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.month_edit.setProperty("showGroupSeparator", False)
        self.month_edit.setMinimum(0)
        self.month_edit.setMaximum(13)
        self.month_edit.setSingleStep(1)
        self.month_edit.setStepType(QAbstractSpinBox.DefaultStepType)
        self.month_edit.setValue(0)
        self.month_edit.setDisplayIntegerBase(10)

        self.top_date_layout.addWidget(self.month_edit)

        self.next_button = QPushButton(self.horizontalLayoutWidget)
        self.next_button.setObjectName(u"next_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy)
        self.next_button.setCursor(QCursor(Qt.ArrowCursor))
        self.next_button.setMouseTracking(False)
        self.next_button.setFocusPolicy(Qt.NoFocus)
        self.next_button.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.next_button.setStyleSheet(u"brushstyle: solidpattern;")
        self.next_button.setCheckable(False)
        self.next_button.setChecked(False)
        self.next_button.setAutoRepeat(False)
        self.next_button.setAutoDefault(False)
        self.next_button.setFlat(False)

        self.top_date_layout.addWidget(self.next_button)

        self.calendar = QFrame(self.central_widget)
        self.calendar.setObjectName(u"calendar")
        self.calendar.setGeometry(QRect(210, 90, 370, 340))
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.calendar.sizePolicy().hasHeightForWidth())
        self.calendar.setSizePolicy(sizePolicy1)
        self.calendar.setMinimumSize(QSize(0, 0))
        self.calendar.setBaseSize(QSize(650, 400))
        self.calendar.setFrameShape(QFrame.Box)
        self.calendar.setFrameShadow(QFrame.Plain)
        self.calendar.setLineWidth(1)
        self.calendar.setMidLineWidth(0)
        self.gridLayout = QGridLayout(self.calendar)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(2, 0, 2, 2)
        self.date_button_1_0 = QPushButton(self.calendar)
        self.date_button_1_0.setObjectName(u"date_button_1_0")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.date_button_1_0.sizePolicy().hasHeightForWidth())
        self.date_button_1_0.setSizePolicy(sizePolicy2)
        self.date_button_1_0.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_1_0.setCheckable(True)
        self.date_button_1_0.setChecked(False)
        self.date_button_1_0.setAutoRepeatDelay(300)
        self.date_button_1_0.setAutoDefault(False)
        self.date_button_1_0.setFlat(False)
        self.date_button_1_0.setProperty("toMonth", True)
        self.date_button_1_0.setProperty("toDay", False)
        self.date_button_1_0.setProperty("Month", 0)
        self.date_button_1_0.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_1_0, 2, 0, 1, 1)

        self.date_button_0_5 = QPushButton(self.calendar)
        self.date_button_0_5.setObjectName(u"date_button_0_5")
        sizePolicy2.setHeightForWidth(self.date_button_0_5.sizePolicy().hasHeightForWidth())
        self.date_button_0_5.setSizePolicy(sizePolicy2)
        self.date_button_0_5.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_0_5.setCheckable(True)
        self.date_button_0_5.setChecked(False)
        self.date_button_0_5.setAutoRepeatDelay(300)
        self.date_button_0_5.setAutoDefault(False)
        self.date_button_0_5.setFlat(False)
        self.date_button_0_5.setProperty("toMonth", True)
        self.date_button_0_5.setProperty("toDay", False)
        self.date_button_0_5.setProperty("Month", 0)
        self.date_button_0_5.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_0_5, 1, 6, 1, 1)

        self.date_button_4_4 = QPushButton(self.calendar)
        self.date_button_4_4.setObjectName(u"date_button_4_4")
        sizePolicy2.setHeightForWidth(self.date_button_4_4.sizePolicy().hasHeightForWidth())
        self.date_button_4_4.setSizePolicy(sizePolicy2)
        self.date_button_4_4.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_4_4.setCheckable(True)
        self.date_button_4_4.setChecked(False)
        self.date_button_4_4.setAutoRepeatDelay(300)
        self.date_button_4_4.setAutoDefault(False)
        self.date_button_4_4.setFlat(False)
        self.date_button_4_4.setProperty("toMonth", True)
        self.date_button_4_4.setProperty("toDay", False)
        self.date_button_4_4.setProperty("Month", 0)
        self.date_button_4_4.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_4_4, 5, 5, 1, 1)

        self.date_button_0_4 = QPushButton(self.calendar)
        self.date_button_0_4.setObjectName(u"date_button_0_4")
        sizePolicy2.setHeightForWidth(self.date_button_0_4.sizePolicy().hasHeightForWidth())
        self.date_button_0_4.setSizePolicy(sizePolicy2)
        self.date_button_0_4.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_0_4.setCheckable(True)
        self.date_button_0_4.setChecked(False)
        self.date_button_0_4.setAutoRepeatDelay(300)
        self.date_button_0_4.setAutoDefault(False)
        self.date_button_0_4.setFlat(False)
        self.date_button_0_4.setProperty("toMonth", True)
        self.date_button_0_4.setProperty("toDay", False)
        self.date_button_0_4.setProperty("Month", 0)
        self.date_button_0_4.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_0_4, 1, 5, 1, 1)

        self.date_button_4_5 = QPushButton(self.calendar)
        self.date_button_4_5.setObjectName(u"date_button_4_5")
        sizePolicy2.setHeightForWidth(self.date_button_4_5.sizePolicy().hasHeightForWidth())
        self.date_button_4_5.setSizePolicy(sizePolicy2)
        self.date_button_4_5.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_4_5.setCheckable(True)
        self.date_button_4_5.setChecked(False)
        self.date_button_4_5.setAutoRepeatDelay(300)
        self.date_button_4_5.setAutoDefault(False)
        self.date_button_4_5.setFlat(False)
        self.date_button_4_5.setProperty("toMonth", True)
        self.date_button_4_5.setProperty("toDay", False)
        self.date_button_4_5.setProperty("Month", 0)
        self.date_button_4_5.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_4_5, 5, 6, 1, 1)

        self.date_button_3_2 = QPushButton(self.calendar)
        self.date_button_3_2.setObjectName(u"date_button_3_2")
        sizePolicy2.setHeightForWidth(self.date_button_3_2.sizePolicy().hasHeightForWidth())
        self.date_button_3_2.setSizePolicy(sizePolicy2)
        self.date_button_3_2.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_3_2.setCheckable(True)
        self.date_button_3_2.setChecked(False)
        self.date_button_3_2.setAutoRepeatDelay(300)
        self.date_button_3_2.setAutoDefault(False)
        self.date_button_3_2.setFlat(False)
        self.date_button_3_2.setProperty("toMonth", True)
        self.date_button_3_2.setProperty("toDay", False)
        self.date_button_3_2.setProperty("Month", 0)
        self.date_button_3_2.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_3_2, 4, 3, 1, 1)

        self.week_3 = QLabel(self.calendar)
        self.week_3.setObjectName(u"week_3")
        sizePolicy2.setHeightForWidth(self.week_3.sizePolicy().hasHeightForWidth())
        self.week_3.setSizePolicy(sizePolicy2)
        self.week_3.setMinimumSize(QSize(40, 50))
        self.week_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.week_3, 0, 4, 1, 1)

        self.date_button_2_5 = QPushButton(self.calendar)
        self.date_button_2_5.setObjectName(u"date_button_2_5")
        sizePolicy2.setHeightForWidth(self.date_button_2_5.sizePolicy().hasHeightForWidth())
        self.date_button_2_5.setSizePolicy(sizePolicy2)
        self.date_button_2_5.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_2_5.setCheckable(True)
        self.date_button_2_5.setChecked(False)
        self.date_button_2_5.setAutoRepeatDelay(300)
        self.date_button_2_5.setAutoDefault(False)
        self.date_button_2_5.setFlat(False)
        self.date_button_2_5.setProperty("toMonth", True)
        self.date_button_2_5.setProperty("toDay", False)
        self.date_button_2_5.setProperty("Month", 0)
        self.date_button_2_5.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_2_5, 3, 6, 1, 1)

        self.date_button_3_6 = QPushButton(self.calendar)
        self.date_button_3_6.setObjectName(u"date_button_3_6")
        sizePolicy2.setHeightForWidth(self.date_button_3_6.sizePolicy().hasHeightForWidth())
        self.date_button_3_6.setSizePolicy(sizePolicy2)
        self.date_button_3_6.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_3_6.setCheckable(True)
        self.date_button_3_6.setChecked(False)
        self.date_button_3_6.setAutoRepeatDelay(300)
        self.date_button_3_6.setAutoDefault(False)
        self.date_button_3_6.setFlat(False)
        self.date_button_3_6.setProperty("toMonth", True)
        self.date_button_3_6.setProperty("toDay", False)
        self.date_button_3_6.setProperty("Month", 0)
        self.date_button_3_6.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_3_6, 4, 7, 1, 1)

        self.week_4 = QLabel(self.calendar)
        self.week_4.setObjectName(u"week_4")
        sizePolicy2.setHeightForWidth(self.week_4.sizePolicy().hasHeightForWidth())
        self.week_4.setSizePolicy(sizePolicy2)
        self.week_4.setMinimumSize(QSize(40, 50))
        self.week_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.week_4, 0, 5, 1, 1)

        self.date_button_2_4 = QPushButton(self.calendar)
        self.date_button_2_4.setObjectName(u"date_button_2_4")
        sizePolicy2.setHeightForWidth(self.date_button_2_4.sizePolicy().hasHeightForWidth())
        self.date_button_2_4.setSizePolicy(sizePolicy2)
        self.date_button_2_4.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_2_4.setCheckable(True)
        self.date_button_2_4.setChecked(False)
        self.date_button_2_4.setAutoRepeatDelay(300)
        self.date_button_2_4.setAutoDefault(False)
        self.date_button_2_4.setFlat(False)
        self.date_button_2_4.setProperty("toMonth", True)
        self.date_button_2_4.setProperty("toDay", False)
        self.date_button_2_4.setProperty("Month", 0)
        self.date_button_2_4.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_2_4, 3, 5, 1, 1)

        self.week_6 = QLabel(self.calendar)
        self.week_6.setObjectName(u"week_6")
        self.week_6.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.week_6.sizePolicy().hasHeightForWidth())
        self.week_6.setSizePolicy(sizePolicy3)
        self.week_6.setMinimumSize(QSize(40, 50))
        self.week_6.setStyleSheet(u"color: red")
        self.week_6.setScaledContents(False)
        self.week_6.setAlignment(Qt.AlignCenter)
        self.week_6.setWordWrap(False)
        self.week_6.setMargin(2)

        self.gridLayout.addWidget(self.week_6, 0, 7, 1, 1)

        self.week_5 = QLabel(self.calendar)
        self.week_5.setObjectName(u"week_5")
        sizePolicy2.setHeightForWidth(self.week_5.sizePolicy().hasHeightForWidth())
        self.week_5.setSizePolicy(sizePolicy2)
        self.week_5.setMinimumSize(QSize(40, 50))
        self.week_5.setStyleSheet(u"color: red")
        self.week_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.week_5, 0, 6, 1, 1)

        self.date_button_2_0 = QPushButton(self.calendar)
        self.date_button_2_0.setObjectName(u"date_button_2_0")
        sizePolicy2.setHeightForWidth(self.date_button_2_0.sizePolicy().hasHeightForWidth())
        self.date_button_2_0.setSizePolicy(sizePolicy2)
        self.date_button_2_0.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_2_0.setCheckable(True)
        self.date_button_2_0.setChecked(False)
        self.date_button_2_0.setAutoRepeatDelay(300)
        self.date_button_2_0.setAutoDefault(False)
        self.date_button_2_0.setFlat(False)
        self.date_button_2_0.setProperty("toMonth", True)
        self.date_button_2_0.setProperty("toDay", False)
        self.date_button_2_0.setProperty("Month", 0)
        self.date_button_2_0.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_2_0, 3, 0, 1, 1)

        self.date_button_3_4 = QPushButton(self.calendar)
        self.date_button_3_4.setObjectName(u"date_button_3_4")
        sizePolicy2.setHeightForWidth(self.date_button_3_4.sizePolicy().hasHeightForWidth())
        self.date_button_3_4.setSizePolicy(sizePolicy2)
        self.date_button_3_4.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_3_4.setCheckable(True)
        self.date_button_3_4.setChecked(False)
        self.date_button_3_4.setAutoRepeatDelay(300)
        self.date_button_3_4.setAutoDefault(False)
        self.date_button_3_4.setFlat(False)
        self.date_button_3_4.setProperty("toMonth", True)
        self.date_button_3_4.setProperty("toDay", False)
        self.date_button_3_4.setProperty("Month", 0)
        self.date_button_3_4.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_3_4, 4, 5, 1, 1)

        self.date_button_0_6 = QPushButton(self.calendar)
        self.date_button_0_6.setObjectName(u"date_button_0_6")
        sizePolicy2.setHeightForWidth(self.date_button_0_6.sizePolicy().hasHeightForWidth())
        self.date_button_0_6.setSizePolicy(sizePolicy2)
        self.date_button_0_6.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_0_6.setCheckable(True)
        self.date_button_0_6.setChecked(False)
        self.date_button_0_6.setAutoRepeatDelay(300)
        self.date_button_0_6.setAutoDefault(False)
        self.date_button_0_6.setFlat(False)
        self.date_button_0_6.setProperty("toMonth", True)
        self.date_button_0_6.setProperty("toDay", False)
        self.date_button_0_6.setProperty("Month", 0)
        self.date_button_0_6.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_0_6, 1, 7, 1, 1)

        self.date_button_3_0 = QPushButton(self.calendar)
        self.date_button_3_0.setObjectName(u"date_button_3_0")
        sizePolicy2.setHeightForWidth(self.date_button_3_0.sizePolicy().hasHeightForWidth())
        self.date_button_3_0.setSizePolicy(sizePolicy2)
        self.date_button_3_0.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_3_0.setCheckable(True)
        self.date_button_3_0.setChecked(False)
        self.date_button_3_0.setAutoRepeatDelay(300)
        self.date_button_3_0.setAutoDefault(False)
        self.date_button_3_0.setFlat(False)
        self.date_button_3_0.setProperty("toMonth", True)
        self.date_button_3_0.setProperty("toDay", False)
        self.date_button_3_0.setProperty("Month", 0)
        self.date_button_3_0.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_3_0, 4, 0, 1, 1)

        self.date_button_1_4 = QPushButton(self.calendar)
        self.date_button_1_4.setObjectName(u"date_button_1_4")
        sizePolicy2.setHeightForWidth(self.date_button_1_4.sizePolicy().hasHeightForWidth())
        self.date_button_1_4.setSizePolicy(sizePolicy2)
        self.date_button_1_4.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_1_4.setCheckable(True)
        self.date_button_1_4.setChecked(False)
        self.date_button_1_4.setAutoRepeatDelay(300)
        self.date_button_1_4.setAutoDefault(False)
        self.date_button_1_4.setFlat(False)
        self.date_button_1_4.setProperty("toMonth", True)
        self.date_button_1_4.setProperty("toDay", False)
        self.date_button_1_4.setProperty("Month", 0)
        self.date_button_1_4.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_1_4, 2, 5, 1, 1)

        self.date_button_1_6 = QPushButton(self.calendar)
        self.date_button_1_6.setObjectName(u"date_button_1_6")
        sizePolicy2.setHeightForWidth(self.date_button_1_6.sizePolicy().hasHeightForWidth())
        self.date_button_1_6.setSizePolicy(sizePolicy2)
        self.date_button_1_6.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_1_6.setCheckable(True)
        self.date_button_1_6.setChecked(False)
        self.date_button_1_6.setAutoRepeatDelay(300)
        self.date_button_1_6.setAutoDefault(False)
        self.date_button_1_6.setFlat(False)
        self.date_button_1_6.setProperty("toMonth", True)
        self.date_button_1_6.setProperty("toDay", False)
        self.date_button_1_6.setProperty("Month", 0)
        self.date_button_1_6.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_1_6, 2, 7, 1, 1)

        self.date_button_0_3 = QPushButton(self.calendar)
        self.date_button_0_3.setObjectName(u"date_button_0_3")
        sizePolicy2.setHeightForWidth(self.date_button_0_3.sizePolicy().hasHeightForWidth())
        self.date_button_0_3.setSizePolicy(sizePolicy2)
        self.date_button_0_3.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_0_3.setCheckable(True)
        self.date_button_0_3.setChecked(False)
        self.date_button_0_3.setAutoRepeatDelay(300)
        self.date_button_0_3.setAutoDefault(False)
        self.date_button_0_3.setFlat(False)
        self.date_button_0_3.setProperty("toMonth", True)
        self.date_button_0_3.setProperty("toDay", False)
        self.date_button_0_3.setProperty("Month", 0)
        self.date_button_0_3.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_0_3, 1, 4, 1, 1)

        self.date_button_3_1 = QPushButton(self.calendar)
        self.date_button_3_1.setObjectName(u"date_button_3_1")
        sizePolicy2.setHeightForWidth(self.date_button_3_1.sizePolicy().hasHeightForWidth())
        self.date_button_3_1.setSizePolicy(sizePolicy2)
        self.date_button_3_1.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_3_1.setCheckable(True)
        self.date_button_3_1.setChecked(False)
        self.date_button_3_1.setAutoRepeatDelay(300)
        self.date_button_3_1.setAutoDefault(False)
        self.date_button_3_1.setFlat(False)
        self.date_button_3_1.setProperty("toMonth", True)
        self.date_button_3_1.setProperty("toDay", False)
        self.date_button_3_1.setProperty("Month", 0)
        self.date_button_3_1.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_3_1, 4, 2, 1, 1)

        self.date_button_2_6 = QPushButton(self.calendar)
        self.date_button_2_6.setObjectName(u"date_button_2_6")
        sizePolicy2.setHeightForWidth(self.date_button_2_6.sizePolicy().hasHeightForWidth())
        self.date_button_2_6.setSizePolicy(sizePolicy2)
        self.date_button_2_6.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_2_6.setCheckable(True)
        self.date_button_2_6.setChecked(False)
        self.date_button_2_6.setAutoRepeatDelay(300)
        self.date_button_2_6.setAutoDefault(False)
        self.date_button_2_6.setFlat(False)
        self.date_button_2_6.setProperty("toMonth", True)
        self.date_button_2_6.setProperty("toDay", False)
        self.date_button_2_6.setProperty("Month", 0)
        self.date_button_2_6.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_2_6, 3, 7, 1, 1)

        self.date_button_4_1 = QPushButton(self.calendar)
        self.date_button_4_1.setObjectName(u"date_button_4_1")
        sizePolicy2.setHeightForWidth(self.date_button_4_1.sizePolicy().hasHeightForWidth())
        self.date_button_4_1.setSizePolicy(sizePolicy2)
        self.date_button_4_1.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_4_1.setCheckable(True)
        self.date_button_4_1.setChecked(False)
        self.date_button_4_1.setAutoRepeatDelay(300)
        self.date_button_4_1.setAutoDefault(False)
        self.date_button_4_1.setFlat(False)
        self.date_button_4_1.setProperty("toMonth", True)
        self.date_button_4_1.setProperty("toDay", False)
        self.date_button_4_1.setProperty("Month", 0)
        self.date_button_4_1.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_4_1, 5, 2, 1, 1)

        self.date_button_1_3 = QPushButton(self.calendar)
        self.date_button_1_3.setObjectName(u"date_button_1_3")
        sizePolicy2.setHeightForWidth(self.date_button_1_3.sizePolicy().hasHeightForWidth())
        self.date_button_1_3.setSizePolicy(sizePolicy2)
        self.date_button_1_3.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_1_3.setCheckable(True)
        self.date_button_1_3.setChecked(False)
        self.date_button_1_3.setAutoRepeatDelay(300)
        self.date_button_1_3.setAutoDefault(False)
        self.date_button_1_3.setFlat(False)
        self.date_button_1_3.setProperty("toMonth", True)
        self.date_button_1_3.setProperty("toDay", False)
        self.date_button_1_3.setProperty("Month", 0)
        self.date_button_1_3.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_1_3, 2, 4, 1, 1)

        self.date_button_5_0 = QPushButton(self.calendar)
        self.date_button_5_0.setObjectName(u"date_button_5_0")
        sizePolicy2.setHeightForWidth(self.date_button_5_0.sizePolicy().hasHeightForWidth())
        self.date_button_5_0.setSizePolicy(sizePolicy2)
        self.date_button_5_0.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_5_0.setCheckable(True)
        self.date_button_5_0.setChecked(False)
        self.date_button_5_0.setAutoRepeatDelay(300)
        self.date_button_5_0.setAutoDefault(False)
        self.date_button_5_0.setFlat(False)
        self.date_button_5_0.setProperty("toMonth", True)
        self.date_button_5_0.setProperty("toDay", False)
        self.date_button_5_0.setProperty("Month", 0)
        self.date_button_5_0.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_5_0, 6, 0, 1, 1)

        self.date_button_5_3 = QPushButton(self.calendar)
        self.date_button_5_3.setObjectName(u"date_button_5_3")
        sizePolicy2.setHeightForWidth(self.date_button_5_3.sizePolicy().hasHeightForWidth())
        self.date_button_5_3.setSizePolicy(sizePolicy2)
        self.date_button_5_3.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_5_3.setCheckable(True)
        self.date_button_5_3.setChecked(False)
        self.date_button_5_3.setAutoRepeatDelay(300)
        self.date_button_5_3.setAutoDefault(False)
        self.date_button_5_3.setFlat(False)
        self.date_button_5_3.setProperty("toMonth", True)
        self.date_button_5_3.setProperty("toDay", False)
        self.date_button_5_3.setProperty("Month", 0)
        self.date_button_5_3.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_5_3, 6, 4, 1, 1)

        self.date_button_3_5 = QPushButton(self.calendar)
        self.date_button_3_5.setObjectName(u"date_button_3_5")
        sizePolicy2.setHeightForWidth(self.date_button_3_5.sizePolicy().hasHeightForWidth())
        self.date_button_3_5.setSizePolicy(sizePolicy2)
        self.date_button_3_5.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_3_5.setCheckable(True)
        self.date_button_3_5.setChecked(False)
        self.date_button_3_5.setAutoRepeatDelay(300)
        self.date_button_3_5.setAutoDefault(False)
        self.date_button_3_5.setFlat(False)
        self.date_button_3_5.setProperty("toMonth", True)
        self.date_button_3_5.setProperty("toDay", False)
        self.date_button_3_5.setProperty("Month", 0)
        self.date_button_3_5.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_3_5, 4, 6, 1, 1)

        self.week_1 = QLabel(self.calendar)
        self.week_1.setObjectName(u"week_1")
        sizePolicy2.setHeightForWidth(self.week_1.sizePolicy().hasHeightForWidth())
        self.week_1.setSizePolicy(sizePolicy2)
        self.week_1.setMinimumSize(QSize(40, 50))
        self.week_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.week_1, 0, 2, 1, 1)

        self.date_button_0_1 = QPushButton(self.calendar)
        self.date_button_0_1.setObjectName(u"date_button_0_1")
        sizePolicy2.setHeightForWidth(self.date_button_0_1.sizePolicy().hasHeightForWidth())
        self.date_button_0_1.setSizePolicy(sizePolicy2)
        self.date_button_0_1.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_0_1.setCheckable(True)
        self.date_button_0_1.setChecked(False)
        self.date_button_0_1.setAutoRepeatDelay(300)
        self.date_button_0_1.setAutoDefault(False)
        self.date_button_0_1.setFlat(False)
        self.date_button_0_1.setProperty("toMonth", True)
        self.date_button_0_1.setProperty("toDay", False)
        self.date_button_0_1.setProperty("Month", 0)
        self.date_button_0_1.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_0_1, 1, 2, 1, 1)

        self.week_2 = QLabel(self.calendar)
        self.week_2.setObjectName(u"week_2")
        sizePolicy2.setHeightForWidth(self.week_2.sizePolicy().hasHeightForWidth())
        self.week_2.setSizePolicy(sizePolicy2)
        self.week_2.setMinimumSize(QSize(40, 50))
        self.week_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.week_2, 0, 3, 1, 1)

        self.date_button_3_3 = QPushButton(self.calendar)
        self.date_button_3_3.setObjectName(u"date_button_3_3")
        sizePolicy2.setHeightForWidth(self.date_button_3_3.sizePolicy().hasHeightForWidth())
        self.date_button_3_3.setSizePolicy(sizePolicy2)
        self.date_button_3_3.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_3_3.setCheckable(True)
        self.date_button_3_3.setChecked(False)
        self.date_button_3_3.setAutoRepeatDelay(300)
        self.date_button_3_3.setAutoDefault(False)
        self.date_button_3_3.setFlat(False)
        self.date_button_3_3.setProperty("toMonth", True)
        self.date_button_3_3.setProperty("toDay", False)
        self.date_button_3_3.setProperty("Month", 0)
        self.date_button_3_3.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_3_3, 4, 4, 1, 1)

        self.date_button_5_5 = QPushButton(self.calendar)
        self.date_button_5_5.setObjectName(u"date_button_5_5")
        sizePolicy2.setHeightForWidth(self.date_button_5_5.sizePolicy().hasHeightForWidth())
        self.date_button_5_5.setSizePolicy(sizePolicy2)
        self.date_button_5_5.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_5_5.setCheckable(True)
        self.date_button_5_5.setChecked(False)
        self.date_button_5_5.setAutoRepeatDelay(300)
        self.date_button_5_5.setAutoDefault(False)
        self.date_button_5_5.setFlat(False)
        self.date_button_5_5.setProperty("toMonth", True)
        self.date_button_5_5.setProperty("toDay", False)
        self.date_button_5_5.setProperty("Month", 0)
        self.date_button_5_5.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_5_5, 6, 6, 1, 1)

        self.date_button_4_3 = QPushButton(self.calendar)
        self.date_button_4_3.setObjectName(u"date_button_4_3")
        sizePolicy2.setHeightForWidth(self.date_button_4_3.sizePolicy().hasHeightForWidth())
        self.date_button_4_3.setSizePolicy(sizePolicy2)
        self.date_button_4_3.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_4_3.setCheckable(True)
        self.date_button_4_3.setChecked(False)
        self.date_button_4_3.setAutoRepeatDelay(300)
        self.date_button_4_3.setAutoDefault(False)
        self.date_button_4_3.setFlat(False)
        self.date_button_4_3.setProperty("toMonth", True)
        self.date_button_4_3.setProperty("toDay", False)
        self.date_button_4_3.setProperty("Month", 0)
        self.date_button_4_3.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_4_3, 5, 4, 1, 1)

        self.date_button_5_1 = QPushButton(self.calendar)
        self.date_button_5_1.setObjectName(u"date_button_5_1")
        sizePolicy2.setHeightForWidth(self.date_button_5_1.sizePolicy().hasHeightForWidth())
        self.date_button_5_1.setSizePolicy(sizePolicy2)
        self.date_button_5_1.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_5_1.setCheckable(True)
        self.date_button_5_1.setChecked(False)
        self.date_button_5_1.setAutoRepeatDelay(300)
        self.date_button_5_1.setAutoDefault(False)
        self.date_button_5_1.setFlat(False)
        self.date_button_5_1.setProperty("toMonth", True)
        self.date_button_5_1.setProperty("toDay", False)
        self.date_button_5_1.setProperty("Month", 0)
        self.date_button_5_1.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_5_1, 6, 2, 1, 1)

        self.date_button_1_5 = QPushButton(self.calendar)
        self.date_button_1_5.setObjectName(u"date_button_1_5")
        sizePolicy2.setHeightForWidth(self.date_button_1_5.sizePolicy().hasHeightForWidth())
        self.date_button_1_5.setSizePolicy(sizePolicy2)
        self.date_button_1_5.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_1_5.setCheckable(True)
        self.date_button_1_5.setChecked(False)
        self.date_button_1_5.setAutoRepeatDelay(300)
        self.date_button_1_5.setAutoDefault(False)
        self.date_button_1_5.setFlat(False)
        self.date_button_1_5.setProperty("toMonth", True)
        self.date_button_1_5.setProperty("toDay", False)
        self.date_button_1_5.setProperty("Month", 0)
        self.date_button_1_5.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_1_5, 2, 6, 1, 1)

        self.date_button_2_3 = QPushButton(self.calendar)
        self.date_button_2_3.setObjectName(u"date_button_2_3")
        sizePolicy2.setHeightForWidth(self.date_button_2_3.sizePolicy().hasHeightForWidth())
        self.date_button_2_3.setSizePolicy(sizePolicy2)
        self.date_button_2_3.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_2_3.setCheckable(True)
        self.date_button_2_3.setChecked(False)
        self.date_button_2_3.setAutoRepeatDelay(300)
        self.date_button_2_3.setAutoDefault(False)
        self.date_button_2_3.setFlat(False)
        self.date_button_2_3.setProperty("toMonth", True)
        self.date_button_2_3.setProperty("toDay", False)
        self.date_button_2_3.setProperty("Month", 0)
        self.date_button_2_3.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_2_3, 3, 4, 1, 1)

        self.date_button_5_2 = QPushButton(self.calendar)
        self.date_button_5_2.setObjectName(u"date_button_5_2")
        sizePolicy2.setHeightForWidth(self.date_button_5_2.sizePolicy().hasHeightForWidth())
        self.date_button_5_2.setSizePolicy(sizePolicy2)
        self.date_button_5_2.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_5_2.setCheckable(True)
        self.date_button_5_2.setChecked(False)
        self.date_button_5_2.setAutoRepeatDelay(300)
        self.date_button_5_2.setAutoDefault(False)
        self.date_button_5_2.setFlat(False)
        self.date_button_5_2.setProperty("toMonth", True)
        self.date_button_5_2.setProperty("toDay", False)
        self.date_button_5_2.setProperty("Month", 0)
        self.date_button_5_2.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_5_2, 6, 3, 1, 1)

        self.date_button_1_2 = QPushButton(self.calendar)
        self.date_button_1_2.setObjectName(u"date_button_1_2")
        sizePolicy2.setHeightForWidth(self.date_button_1_2.sizePolicy().hasHeightForWidth())
        self.date_button_1_2.setSizePolicy(sizePolicy2)
        self.date_button_1_2.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_1_2.setCheckable(True)
        self.date_button_1_2.setChecked(False)
        self.date_button_1_2.setAutoRepeatDelay(300)
        self.date_button_1_2.setAutoDefault(False)
        self.date_button_1_2.setFlat(False)
        self.date_button_1_2.setProperty("toMonth", True)
        self.date_button_1_2.setProperty("toDay", False)
        self.date_button_1_2.setProperty("Month", 0)
        self.date_button_1_2.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_1_2, 2, 3, 1, 1)

        self.date_button_2_2 = QPushButton(self.calendar)
        self.date_button_2_2.setObjectName(u"date_button_2_2")
        sizePolicy2.setHeightForWidth(self.date_button_2_2.sizePolicy().hasHeightForWidth())
        self.date_button_2_2.setSizePolicy(sizePolicy2)
        self.date_button_2_2.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_2_2.setCheckable(True)
        self.date_button_2_2.setChecked(False)
        self.date_button_2_2.setAutoRepeatDelay(300)
        self.date_button_2_2.setAutoDefault(False)
        self.date_button_2_2.setFlat(False)
        self.date_button_2_2.setProperty("toMonth", True)
        self.date_button_2_2.setProperty("toDay", False)
        self.date_button_2_2.setProperty("Month", 0)
        self.date_button_2_2.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_2_2, 3, 3, 1, 1)

        self.date_button_0_0 = QPushButton(self.calendar)
        self.date_button_0_0.setObjectName(u"date_button_0_0")
        sizePolicy2.setHeightForWidth(self.date_button_0_0.sizePolicy().hasHeightForWidth())
        self.date_button_0_0.setSizePolicy(sizePolicy2)
        self.date_button_0_0.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_0_0.setCheckable(True)
        self.date_button_0_0.setChecked(False)
        self.date_button_0_0.setAutoRepeatDelay(300)
        self.date_button_0_0.setAutoDefault(False)
        self.date_button_0_0.setFlat(False)
        self.date_button_0_0.setProperty("toMonth", True)
        self.date_button_0_0.setProperty("toDay", False)
        self.date_button_0_0.setProperty("Month", 0)
        self.date_button_0_0.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_0_0, 1, 0, 1, 1)

        self.date_button_4_0 = QPushButton(self.calendar)
        self.date_button_4_0.setObjectName(u"date_button_4_0")
        sizePolicy2.setHeightForWidth(self.date_button_4_0.sizePolicy().hasHeightForWidth())
        self.date_button_4_0.setSizePolicy(sizePolicy2)
        self.date_button_4_0.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_4_0.setCheckable(True)
        self.date_button_4_0.setChecked(False)
        self.date_button_4_0.setAutoRepeatDelay(300)
        self.date_button_4_0.setAutoDefault(False)
        self.date_button_4_0.setFlat(False)
        self.date_button_4_0.setProperty("toMonth", True)
        self.date_button_4_0.setProperty("toDay", False)
        self.date_button_4_0.setProperty("Month", 0)
        self.date_button_4_0.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_4_0, 5, 0, 1, 1)

        self.date_button_5_6 = QPushButton(self.calendar)
        self.date_button_5_6.setObjectName(u"date_button_5_6")
        sizePolicy2.setHeightForWidth(self.date_button_5_6.sizePolicy().hasHeightForWidth())
        self.date_button_5_6.setSizePolicy(sizePolicy2)
        self.date_button_5_6.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_5_6.setCheckable(True)
        self.date_button_5_6.setChecked(False)
        self.date_button_5_6.setAutoRepeatDelay(300)
        self.date_button_5_6.setAutoDefault(False)
        self.date_button_5_6.setFlat(False)
        self.date_button_5_6.setProperty("toMonth", True)
        self.date_button_5_6.setProperty("toDay", False)
        self.date_button_5_6.setProperty("Month", 0)
        self.date_button_5_6.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_5_6, 6, 7, 1, 1)

        self.date_button_1_1 = QPushButton(self.calendar)
        self.date_button_1_1.setObjectName(u"date_button_1_1")
        sizePolicy2.setHeightForWidth(self.date_button_1_1.sizePolicy().hasHeightForWidth())
        self.date_button_1_1.setSizePolicy(sizePolicy2)
        self.date_button_1_1.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_1_1.setCheckable(True)
        self.date_button_1_1.setChecked(False)
        self.date_button_1_1.setAutoRepeatDelay(300)
        self.date_button_1_1.setAutoDefault(False)
        self.date_button_1_1.setFlat(False)
        self.date_button_1_1.setProperty("toMonth", True)
        self.date_button_1_1.setProperty("toDay", False)
        self.date_button_1_1.setProperty("Month", 0)
        self.date_button_1_1.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_1_1, 2, 2, 1, 1)

        self.date_button_0_2 = QPushButton(self.calendar)
        self.date_button_0_2.setObjectName(u"date_button_0_2")
        sizePolicy2.setHeightForWidth(self.date_button_0_2.sizePolicy().hasHeightForWidth())
        self.date_button_0_2.setSizePolicy(sizePolicy2)
        self.date_button_0_2.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_0_2.setCheckable(True)
        self.date_button_0_2.setChecked(False)
        self.date_button_0_2.setAutoRepeatDelay(300)
        self.date_button_0_2.setAutoDefault(False)
        self.date_button_0_2.setFlat(False)
        self.date_button_0_2.setProperty("toMonth", True)
        self.date_button_0_2.setProperty("toDay", False)
        self.date_button_0_2.setProperty("Month", 0)
        self.date_button_0_2.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_0_2, 1, 3, 1, 1)

        self.date_button_2_1 = QPushButton(self.calendar)
        self.date_button_2_1.setObjectName(u"date_button_2_1")
        sizePolicy2.setHeightForWidth(self.date_button_2_1.sizePolicy().hasHeightForWidth())
        self.date_button_2_1.setSizePolicy(sizePolicy2)
        self.date_button_2_1.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_2_1.setCheckable(True)
        self.date_button_2_1.setChecked(False)
        self.date_button_2_1.setAutoRepeatDelay(300)
        self.date_button_2_1.setAutoDefault(False)
        self.date_button_2_1.setFlat(False)
        self.date_button_2_1.setProperty("toMonth", True)
        self.date_button_2_1.setProperty("toDay", False)
        self.date_button_2_1.setProperty("Month", 0)
        self.date_button_2_1.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_2_1, 3, 2, 1, 1)

        self.date_button_5_4 = QPushButton(self.calendar)
        self.date_button_5_4.setObjectName(u"date_button_5_4")
        sizePolicy2.setHeightForWidth(self.date_button_5_4.sizePolicy().hasHeightForWidth())
        self.date_button_5_4.setSizePolicy(sizePolicy2)
        self.date_button_5_4.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_5_4.setCheckable(True)
        self.date_button_5_4.setChecked(False)
        self.date_button_5_4.setAutoRepeatDelay(300)
        self.date_button_5_4.setAutoDefault(False)
        self.date_button_5_4.setFlat(False)
        self.date_button_5_4.setProperty("toMonth", True)
        self.date_button_5_4.setProperty("toDay", False)
        self.date_button_5_4.setProperty("Month", 0)
        self.date_button_5_4.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_5_4, 6, 5, 1, 1)

        self.date_button_4_6 = QPushButton(self.calendar)
        self.date_button_4_6.setObjectName(u"date_button_4_6")
        sizePolicy2.setHeightForWidth(self.date_button_4_6.sizePolicy().hasHeightForWidth())
        self.date_button_4_6.setSizePolicy(sizePolicy2)
        self.date_button_4_6.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_4_6.setCheckable(True)
        self.date_button_4_6.setChecked(False)
        self.date_button_4_6.setAutoRepeatDelay(300)
        self.date_button_4_6.setAutoDefault(False)
        self.date_button_4_6.setFlat(False)
        self.date_button_4_6.setProperty("toMonth", True)
        self.date_button_4_6.setProperty("toDay", False)
        self.date_button_4_6.setProperty("Month", 0)
        self.date_button_4_6.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_4_6, 5, 7, 1, 1)

        self.date_button_4_2 = QPushButton(self.calendar)
        self.date_button_4_2.setObjectName(u"date_button_4_2")
        sizePolicy2.setHeightForWidth(self.date_button_4_2.sizePolicy().hasHeightForWidth())
        self.date_button_4_2.setSizePolicy(sizePolicy2)
        self.date_button_4_2.setStyleSheet(u"QPushButton:hover {\n"
                                           "	background-color: rgba(0, 0, 0, 20);\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	border:0px solid;\n"
                                           "	background-color: rgba(255, 255, 255, 0);\n"
                                           "	margin: 3px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toMonth=\"false\"]{\n"
                                           "	color: grey;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]{\n"
                                           "	background-color: rgba(20, 165, 255, 255);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:hover{\n"
                                           "	background-color:rgba(20, 165, 255, 200);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:pressed{\n"
                                           "	background-color:rgba(20, 165, 255, 180);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton[toDay=\"true\"]:focus{\n"
                                           "	border:1px solid rgb(4, 80, 173);\n"
                                           "	color: white;\n"
                                           "	border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "	background-color: rgba(0, 0, 0, 15);\n"
                                           "	color:rgba(0, 0, 0, 180);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:focus{\n"
                                           "	border:1px solid rgba(0, 0, 0, 150);\n"
                                           "	border-radius: "
                                           "7px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.date_button_4_2.setCheckable(True)
        self.date_button_4_2.setChecked(False)
        self.date_button_4_2.setAutoRepeatDelay(300)
        self.date_button_4_2.setAutoDefault(False)
        self.date_button_4_2.setFlat(False)
        self.date_button_4_2.setProperty("toMonth", True)
        self.date_button_4_2.setProperty("toDay", False)
        self.date_button_4_2.setProperty("Month", 0)
        self.date_button_4_2.setProperty("Year", 0)

        self.gridLayout.addWidget(self.date_button_4_2, 5, 3, 1, 1)

        self.week_0 = QLabel(self.calendar)
        self.week_0.setObjectName(u"week_0")
        self.week_0.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.week_0.sizePolicy().hasHeightForWidth())
        self.week_0.setSizePolicy(sizePolicy4)
        self.week_0.setMinimumSize(QSize(40, 50))
        self.week_0.setLayoutDirection(Qt.LeftToRight)
        self.week_0.setAlignment(Qt.AlignCenter)
        self.week_0.setWordWrap(False)
        self.week_0.setOpenExternalLinks(False)

        self.gridLayout.addWidget(self.week_0, 0, 0, 1, 1)

        self.gridLayout.setColumnMinimumWidth(7, 40)
        self.gridLayout.setRowMinimumHeight(6, 40)
        self.label_past = QLabel(self.central_widget)
        self.label_past.setObjectName(u"label_past")
        self.label_past.setGeometry(QRect(110, 440, 511, 41))
        self.label_past.setTextFormat(Qt.AutoText)
        self.label_future = QLabel(self.central_widget)
        self.label_future.setObjectName(u"label_future")
        self.label_future.setGeometry(QRect(110, 490, 511, 41))
        self.label_future.setTextFormat(Qt.AutoText)
        self.horizontalLayoutWidget_2 = QWidget(self.central_widget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(170, 0, 481, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_nowtime = QLabel(self.horizontalLayoutWidget_2)
        self.label_nowtime.setObjectName(u"label_nowtime")
        font = QFont()
        font.setPointSize(13)
        self.label_nowtime.setFont(font)
        self.label_nowtime.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_nowtime)

        self.goback_button = QPushButton(self.horizontalLayoutWidget_2)
        self.goback_button.setObjectName(u"goback_button")
        self.goback_button.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout.addWidget(self.goback_button)

        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 819, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.goback_button, self.left_button)
        QWidget.setTabOrder(self.left_button, self.year_edit)
        QWidget.setTabOrder(self.year_edit, self.month_edit)
        QWidget.setTabOrder(self.month_edit, self.next_button)
        QWidget.setTabOrder(self.next_button, self.date_button_0_0)
        QWidget.setTabOrder(self.date_button_0_0, self.date_button_0_1)
        QWidget.setTabOrder(self.date_button_0_1, self.date_button_0_2)
        QWidget.setTabOrder(self.date_button_0_2, self.date_button_0_3)
        QWidget.setTabOrder(self.date_button_0_3, self.date_button_0_4)
        QWidget.setTabOrder(self.date_button_0_4, self.date_button_0_5)
        QWidget.setTabOrder(self.date_button_0_5, self.date_button_0_6)
        QWidget.setTabOrder(self.date_button_0_6, self.date_button_1_0)
        QWidget.setTabOrder(self.date_button_1_0, self.date_button_1_1)
        QWidget.setTabOrder(self.date_button_1_1, self.date_button_1_2)
        QWidget.setTabOrder(self.date_button_1_2, self.date_button_1_3)
        QWidget.setTabOrder(self.date_button_1_3, self.date_button_1_4)
        QWidget.setTabOrder(self.date_button_1_4, self.date_button_1_5)
        QWidget.setTabOrder(self.date_button_1_5, self.date_button_1_6)
        QWidget.setTabOrder(self.date_button_1_6, self.date_button_2_0)
        QWidget.setTabOrder(self.date_button_2_0, self.date_button_2_1)
        QWidget.setTabOrder(self.date_button_2_1, self.date_button_2_2)
        QWidget.setTabOrder(self.date_button_2_2, self.date_button_2_3)
        QWidget.setTabOrder(self.date_button_2_3, self.date_button_2_4)
        QWidget.setTabOrder(self.date_button_2_4, self.date_button_2_5)
        QWidget.setTabOrder(self.date_button_2_5, self.date_button_2_6)
        QWidget.setTabOrder(self.date_button_2_6, self.date_button_3_0)
        QWidget.setTabOrder(self.date_button_3_0, self.date_button_3_1)
        QWidget.setTabOrder(self.date_button_3_1, self.date_button_3_2)
        QWidget.setTabOrder(self.date_button_3_2, self.date_button_3_3)
        QWidget.setTabOrder(self.date_button_3_3, self.date_button_3_4)
        QWidget.setTabOrder(self.date_button_3_4, self.date_button_3_5)
        QWidget.setTabOrder(self.date_button_3_5, self.date_button_3_6)
        QWidget.setTabOrder(self.date_button_3_6, self.date_button_4_0)
        QWidget.setTabOrder(self.date_button_4_0, self.date_button_4_1)
        QWidget.setTabOrder(self.date_button_4_1, self.date_button_4_2)
        QWidget.setTabOrder(self.date_button_4_2, self.date_button_4_3)
        QWidget.setTabOrder(self.date_button_4_3, self.date_button_4_4)
        QWidget.setTabOrder(self.date_button_4_4, self.date_button_4_5)
        QWidget.setTabOrder(self.date_button_4_5, self.date_button_4_6)
        QWidget.setTabOrder(self.date_button_4_6, self.date_button_5_0)
        QWidget.setTabOrder(self.date_button_5_0, self.date_button_5_1)
        QWidget.setTabOrder(self.date_button_5_1, self.date_button_5_2)
        QWidget.setTabOrder(self.date_button_5_2, self.date_button_5_3)
        QWidget.setTabOrder(self.date_button_5_3, self.date_button_5_4)
        QWidget.setTabOrder(self.date_button_5_4, self.date_button_5_5)
        QWidget.setTabOrder(self.date_button_5_5, self.date_button_5_6)

        self.retranslateUi(MainWindow)

        self.next_button.setDefault(False)
        self.date_button_1_0.setDefault(False)
        self.date_button_0_5.setDefault(False)
        self.date_button_4_4.setDefault(False)
        self.date_button_0_4.setDefault(False)
        self.date_button_4_5.setDefault(False)
        self.date_button_3_2.setDefault(False)
        self.date_button_2_5.setDefault(False)
        self.date_button_3_6.setDefault(False)
        self.date_button_2_4.setDefault(False)
        self.date_button_2_0.setDefault(False)
        self.date_button_3_4.setDefault(False)
        self.date_button_0_6.setDefault(False)
        self.date_button_3_0.setDefault(False)
        self.date_button_1_4.setDefault(False)
        self.date_button_1_6.setDefault(False)
        self.date_button_0_3.setDefault(False)
        self.date_button_3_1.setDefault(False)
        self.date_button_2_6.setDefault(False)
        self.date_button_4_1.setDefault(False)
        self.date_button_1_3.setDefault(False)
        self.date_button_5_0.setDefault(False)
        self.date_button_5_3.setDefault(False)
        self.date_button_3_5.setDefault(False)
        self.date_button_0_1.setDefault(False)
        self.date_button_3_3.setDefault(False)
        self.date_button_5_5.setDefault(False)
        self.date_button_4_3.setDefault(False)
        self.date_button_5_1.setDefault(False)
        self.date_button_1_5.setDefault(False)
        self.date_button_2_3.setDefault(False)
        self.date_button_5_2.setDefault(False)
        self.date_button_1_2.setDefault(False)
        self.date_button_2_2.setDefault(False)
        self.date_button_0_0.setDefault(False)
        self.date_button_4_0.setDefault(False)
        self.date_button_5_6.setDefault(False)
        self.date_button_1_1.setDefault(False)
        self.date_button_0_2.setDefault(False)
        self.date_button_2_1.setDefault(False)
        self.date_button_5_4.setDefault(False)
        self.date_button_4_6.setDefault(False)
        self.date_button_4_2.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"KFC Calendar", None))
        self.left_button.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.year_edit.setSuffix(QCoreApplication.translate("MainWindow", u"\u5e74", None))
        self.month_edit.setSuffix(QCoreApplication.translate("MainWindow", u"\u6708", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.date_button_1_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_0_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_4_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_0_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_4_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_3_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.week_3.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u56db", None))
        self.date_button_2_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_3_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.week_4.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e94", None))
        self.date_button_2_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.week_6.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u5929", None))
        self.week_5.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u516d", None))
        self.date_button_2_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_3_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_0_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_3_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_1_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_1_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_0_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_3_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_2_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_4_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_1_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_5_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_5_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_3_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.week_1.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e8c", None))
        self.date_button_0_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.week_2.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e09", None))
        self.date_button_3_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_5_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_4_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_5_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_1_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_2_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_5_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_1_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_2_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_0_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_4_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_5_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_1_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_0_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_2_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_5_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_4_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_4_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.week_0.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e00", None))
        self.label_past.setText(QCoreApplication.translate("MainWindow",
                                                           u"\u56de\u9996\u8fc7\u53bb\uff1a\u8ddd\u79bb\u4e0a\u4e2a\u75af\u72c2\u661f\u671f\u56db\u5df2\u7ecf\u8fc7\u4e860\u5929",
                                                           None))
        self.label_future.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u5c55\u671b\u672a\u6765\uff1a\u8fd8\u67090\u5929\u5230\u4e0b\u4e00\u4e2a\u75af\u72c2\u661f\u671f\u56db",
                                                             None))
        self.label_nowtime.setText(
            QCoreApplication.translate("MainWindow", u"\u516c\u51430000\u5e74 00\u670800\u65e5 \u661f\u671f0 00:00:00",
                                       None))
        self.goback_button.setText(QCoreApplication.translate("MainWindow", u"\u56de\u5230\u4eca\u5929", None))
    # retranslateUi
