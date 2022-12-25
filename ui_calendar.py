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
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(819, 601)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(False)
        icon = QIcon()
        iconThemeName = u"12"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setAnimated(False)
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.horizontalLayout_7 = QHBoxLayout(self.central_widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.main_widget = QTabWidget(self.central_widget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setEnabled(True)
        self.main_widget.setTabPosition(QTabWidget.North)
        self.main_widget.setTabShape(QTabWidget.Rounded)
        self.main_widget.setUsesScrollButtons(True)
        self.main_widget.setDocumentMode(False)
        self.main_widget.setTabsClosable(False)
        self.main_widget.setMovable(False)
        self.main_widget.setTabBarAutoHide(False)
        self.tab_home = QWidget()
        self.tab_home.setObjectName(u"tab_home")
        self.tab_home_verticalLayout = QVBoxLayout(self.tab_home)
        self.tab_home_verticalLayout.setObjectName(u"tab_home_verticalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(189, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.label_nowtime = QLabel(self.tab_home)
        self.label_nowtime.setObjectName(u"label_nowtime")
        font = QFont()
        font.setPointSize(13)
        self.label_nowtime.setFont(font)
        self.label_nowtime.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_nowtime)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.goback_button = QPushButton(self.tab_home)
        self.goback_button.setObjectName(u"goback_button")
        self.goback_button.setMinimumSize(QSize(100, 28))
        self.goback_button.setMaximumSize(QSize(120, 16777215))
        self.goback_button.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_10.addWidget(self.goback_button)


        self.horizontalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalSpacer_7 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.top_date_layout = QHBoxLayout()
        self.top_date_layout.setSpacing(7)
        self.top_date_layout.setObjectName(u"top_date_layout")
        self.left_button = QPushButton(self.tab_home)
        self.left_button.setObjectName(u"left_button")
        self.left_button.setFocusPolicy(Qt.NoFocus)
        self.left_button.setCheckable(False)
        self.left_button.setChecked(False)
        self.left_button.setAutoRepeat(False)
        self.left_button.setAutoExclusive(False)

        self.top_date_layout.addWidget(self.left_button)

        self.year_edit = QSpinBox(self.tab_home)
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

        self.month_edit = QSpinBox(self.tab_home)
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

        self.next_button = QPushButton(self.tab_home)
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
        self.next_button.setStyleSheet(u"brushstyle:\n"
"                                                                                solidpattern;\n"
"                                                                            ")
        self.next_button.setCheckable(False)
        self.next_button.setChecked(False)
        self.next_button.setAutoRepeat(False)
        self.next_button.setAutoDefault(False)
        self.next_button.setFlat(False)

        self.top_date_layout.addWidget(self.next_button)


        self.verticalLayout_3.addLayout(self.top_date_layout)

        self.calendar = QFrame(self.tab_home)
        self.calendar.setObjectName(u"calendar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.calendar.sizePolicy().hasHeightForWidth())
        self.calendar.setSizePolicy(sizePolicy1)
        self.calendar.setMinimumSize(QSize(380, 345))
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
        self.date_button_4_6 = QPushButton(self.calendar)
        self.date_button_4_6.setObjectName(u"date_button_4_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.date_button_4_6.sizePolicy().hasHeightForWidth())
        self.date_button_4_6.setSizePolicy(sizePolicy2)
        self.date_button_4_6.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_2_0 = QPushButton(self.calendar)
        self.date_button_2_0.setObjectName(u"date_button_2_0")
        sizePolicy2.setHeightForWidth(self.date_button_2_0.sizePolicy().hasHeightForWidth())
        self.date_button_2_0.setSizePolicy(sizePolicy2)
        self.date_button_2_0.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_3_6 = QPushButton(self.calendar)
        self.date_button_3_6.setObjectName(u"date_button_3_6")
        sizePolicy2.setHeightForWidth(self.date_button_3_6.sizePolicy().hasHeightForWidth())
        self.date_button_3_6.setSizePolicy(sizePolicy2)
        self.date_button_3_6.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_2_6 = QPushButton(self.calendar)
        self.date_button_2_6.setObjectName(u"date_button_2_6")
        sizePolicy2.setHeightForWidth(self.date_button_2_6.sizePolicy().hasHeightForWidth())
        self.date_button_2_6.setSizePolicy(sizePolicy2)
        self.date_button_2_6.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_1_6 = QPushButton(self.calendar)
        self.date_button_1_6.setObjectName(u"date_button_1_6")
        sizePolicy2.setHeightForWidth(self.date_button_1_6.sizePolicy().hasHeightForWidth())
        self.date_button_1_6.setSizePolicy(sizePolicy2)
        self.date_button_1_6.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_0_1 = QPushButton(self.calendar)
        self.date_button_0_1.setObjectName(u"date_button_0_1")
        sizePolicy2.setHeightForWidth(self.date_button_0_1.sizePolicy().hasHeightForWidth())
        self.date_button_0_1.setSizePolicy(sizePolicy2)
        self.date_button_0_1.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_0_4 = QPushButton(self.calendar)
        self.date_button_0_4.setObjectName(u"date_button_0_4")
        sizePolicy2.setHeightForWidth(self.date_button_0_4.sizePolicy().hasHeightForWidth())
        self.date_button_0_4.setSizePolicy(sizePolicy2)
        self.date_button_0_4.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_1_0 = QPushButton(self.calendar)
        self.date_button_1_0.setObjectName(u"date_button_1_0")
        sizePolicy2.setHeightForWidth(self.date_button_1_0.sizePolicy().hasHeightForWidth())
        self.date_button_1_0.setSizePolicy(sizePolicy2)
        self.date_button_1_0.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_0_0 = QPushButton(self.calendar)
        self.date_button_0_0.setObjectName(u"date_button_0_0")
        sizePolicy2.setHeightForWidth(self.date_button_0_0.sizePolicy().hasHeightForWidth())
        self.date_button_0_0.setSizePolicy(sizePolicy2)
        self.date_button_0_0.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_3_5 = QPushButton(self.calendar)
        self.date_button_3_5.setObjectName(u"date_button_3_5")
        sizePolicy2.setHeightForWidth(self.date_button_3_5.sizePolicy().hasHeightForWidth())
        self.date_button_3_5.setSizePolicy(sizePolicy2)
        self.date_button_3_5.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.week_5 = QLabel(self.calendar)
        self.week_5.setObjectName(u"week_5")
        sizePolicy2.setHeightForWidth(self.week_5.sizePolicy().hasHeightForWidth())
        self.week_5.setSizePolicy(sizePolicy2)
        self.week_5.setMinimumSize(QSize(40, 50))
        self.week_5.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.week_5.setStyleSheet(u"QLabel[isWeekEnd=\"true\"]{\n"
"                                                                                    color: red;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QLabel[isWeekEnd=\"false\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"                                                                                ")
        self.week_5.setAlignment(Qt.AlignCenter)
        self.week_5.setProperty("isWeekEnd", True)
        self.week_5.setProperty("Weekly", 5)

        self.gridLayout.addWidget(self.week_5, 0, 6, 1, 1)

        self.date_button_4_1 = QPushButton(self.calendar)
        self.date_button_4_1.setObjectName(u"date_button_4_1")
        sizePolicy2.setHeightForWidth(self.date_button_4_1.sizePolicy().hasHeightForWidth())
        self.date_button_4_1.setSizePolicy(sizePolicy2)
        self.date_button_4_1.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_1_4 = QPushButton(self.calendar)
        self.date_button_1_4.setObjectName(u"date_button_1_4")
        sizePolicy2.setHeightForWidth(self.date_button_1_4.sizePolicy().hasHeightForWidth())
        self.date_button_1_4.setSizePolicy(sizePolicy2)
        self.date_button_1_4.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_2_2 = QPushButton(self.calendar)
        self.date_button_2_2.setObjectName(u"date_button_2_2")
        sizePolicy2.setHeightForWidth(self.date_button_2_2.sizePolicy().hasHeightForWidth())
        self.date_button_2_2.setSizePolicy(sizePolicy2)
        self.date_button_2_2.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_3_0 = QPushButton(self.calendar)
        self.date_button_3_0.setObjectName(u"date_button_3_0")
        sizePolicy2.setHeightForWidth(self.date_button_3_0.sizePolicy().hasHeightForWidth())
        self.date_button_3_0.setSizePolicy(sizePolicy2)
        self.date_button_3_0.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_3_3 = QPushButton(self.calendar)
        self.date_button_3_3.setObjectName(u"date_button_3_3")
        sizePolicy2.setHeightForWidth(self.date_button_3_3.sizePolicy().hasHeightForWidth())
        self.date_button_3_3.setSizePolicy(sizePolicy2)
        self.date_button_3_3.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_5_4 = QPushButton(self.calendar)
        self.date_button_5_4.setObjectName(u"date_button_5_4")
        sizePolicy2.setHeightForWidth(self.date_button_5_4.sizePolicy().hasHeightForWidth())
        self.date_button_5_4.setSizePolicy(sizePolicy2)
        self.date_button_5_4.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_1_2 = QPushButton(self.calendar)
        self.date_button_1_2.setObjectName(u"date_button_1_2")
        sizePolicy2.setHeightForWidth(self.date_button_1_2.sizePolicy().hasHeightForWidth())
        self.date_button_1_2.setSizePolicy(sizePolicy2)
        self.date_button_1_2.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_5_0 = QPushButton(self.calendar)
        self.date_button_5_0.setObjectName(u"date_button_5_0")
        sizePolicy2.setHeightForWidth(self.date_button_5_0.sizePolicy().hasHeightForWidth())
        self.date_button_5_0.setSizePolicy(sizePolicy2)
        self.date_button_5_0.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_0_3 = QPushButton(self.calendar)
        self.date_button_0_3.setObjectName(u"date_button_0_3")
        sizePolicy2.setHeightForWidth(self.date_button_0_3.sizePolicy().hasHeightForWidth())
        self.date_button_0_3.setSizePolicy(sizePolicy2)
        self.date_button_0_3.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_0_2 = QPushButton(self.calendar)
        self.date_button_0_2.setObjectName(u"date_button_0_2")
        sizePolicy2.setHeightForWidth(self.date_button_0_2.sizePolicy().hasHeightForWidth())
        self.date_button_0_2.setSizePolicy(sizePolicy2)
        self.date_button_0_2.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.week_4 = QLabel(self.calendar)
        self.week_4.setObjectName(u"week_4")
        sizePolicy2.setHeightForWidth(self.week_4.sizePolicy().hasHeightForWidth())
        self.week_4.setSizePolicy(sizePolicy2)
        self.week_4.setMinimumSize(QSize(40, 50))
        self.week_4.setStyleSheet(u"QLabel[isWeekEnd=\"true\"]{\n"
"                                                                                    color: red;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QLabel[isWeekEnd=\"false\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"                                                                                ")
        self.week_4.setAlignment(Qt.AlignCenter)
        self.week_4.setProperty("isWeekEnd", False)
        self.week_4.setProperty("Weekly", 4)

        self.gridLayout.addWidget(self.week_4, 0, 5, 1, 1)

        self.date_button_5_1 = QPushButton(self.calendar)
        self.date_button_5_1.setObjectName(u"date_button_5_1")
        sizePolicy2.setHeightForWidth(self.date_button_5_1.sizePolicy().hasHeightForWidth())
        self.date_button_5_1.setSizePolicy(sizePolicy2)
        self.date_button_5_1.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_0_6 = QPushButton(self.calendar)
        self.date_button_0_6.setObjectName(u"date_button_0_6")
        sizePolicy2.setHeightForWidth(self.date_button_0_6.sizePolicy().hasHeightForWidth())
        self.date_button_0_6.setSizePolicy(sizePolicy2)
        self.date_button_0_6.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_1_1 = QPushButton(self.calendar)
        self.date_button_1_1.setObjectName(u"date_button_1_1")
        sizePolicy2.setHeightForWidth(self.date_button_1_1.sizePolicy().hasHeightForWidth())
        self.date_button_1_1.setSizePolicy(sizePolicy2)
        self.date_button_1_1.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_5_2 = QPushButton(self.calendar)
        self.date_button_5_2.setObjectName(u"date_button_5_2")
        sizePolicy2.setHeightForWidth(self.date_button_5_2.sizePolicy().hasHeightForWidth())
        self.date_button_5_2.setSizePolicy(sizePolicy2)
        self.date_button_5_2.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.week_3 = QLabel(self.calendar)
        self.week_3.setObjectName(u"week_3")
        sizePolicy2.setHeightForWidth(self.week_3.sizePolicy().hasHeightForWidth())
        self.week_3.setSizePolicy(sizePolicy2)
        self.week_3.setMinimumSize(QSize(40, 50))
        self.week_3.setStyleSheet(u"QLabel[isWeekEnd=\"true\"]{\n"
"                                                                                    color: red;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QLabel[isWeekEnd=\"false\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"                                                                                ")
        self.week_3.setAlignment(Qt.AlignCenter)
        self.week_3.setProperty("isWeekEnd", False)
        self.week_3.setProperty("Weekly", 3)

        self.gridLayout.addWidget(self.week_3, 0, 4, 1, 1)

        self.date_button_2_5 = QPushButton(self.calendar)
        self.date_button_2_5.setObjectName(u"date_button_2_5")
        sizePolicy2.setHeightForWidth(self.date_button_2_5.sizePolicy().hasHeightForWidth())
        self.date_button_2_5.setSizePolicy(sizePolicy2)
        self.date_button_2_5.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_4_2 = QPushButton(self.calendar)
        self.date_button_4_2.setObjectName(u"date_button_4_2")
        sizePolicy2.setHeightForWidth(self.date_button_4_2.sizePolicy().hasHeightForWidth())
        self.date_button_4_2.setSizePolicy(sizePolicy2)
        self.date_button_4_2.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_5_6 = QPushButton(self.calendar)
        self.date_button_5_6.setObjectName(u"date_button_5_6")
        sizePolicy2.setHeightForWidth(self.date_button_5_6.sizePolicy().hasHeightForWidth())
        self.date_button_5_6.setSizePolicy(sizePolicy2)
        self.date_button_5_6.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_5_3 = QPushButton(self.calendar)
        self.date_button_5_3.setObjectName(u"date_button_5_3")
        sizePolicy2.setHeightForWidth(self.date_button_5_3.sizePolicy().hasHeightForWidth())
        self.date_button_5_3.setSizePolicy(sizePolicy2)
        self.date_button_5_3.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_1_5 = QPushButton(self.calendar)
        self.date_button_1_5.setObjectName(u"date_button_1_5")
        sizePolicy2.setHeightForWidth(self.date_button_1_5.sizePolicy().hasHeightForWidth())
        self.date_button_1_5.setSizePolicy(sizePolicy2)
        self.date_button_1_5.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_4_5 = QPushButton(self.calendar)
        self.date_button_4_5.setObjectName(u"date_button_4_5")
        sizePolicy2.setHeightForWidth(self.date_button_4_5.sizePolicy().hasHeightForWidth())
        self.date_button_4_5.setSizePolicy(sizePolicy2)
        self.date_button_4_5.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_4_0 = QPushButton(self.calendar)
        self.date_button_4_0.setObjectName(u"date_button_4_0")
        sizePolicy2.setHeightForWidth(self.date_button_4_0.sizePolicy().hasHeightForWidth())
        self.date_button_4_0.setSizePolicy(sizePolicy2)
        self.date_button_4_0.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_0_5 = QPushButton(self.calendar)
        self.date_button_0_5.setObjectName(u"date_button_0_5")
        sizePolicy2.setHeightForWidth(self.date_button_0_5.sizePolicy().hasHeightForWidth())
        self.date_button_0_5.setSizePolicy(sizePolicy2)
        self.date_button_0_5.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_3_4 = QPushButton(self.calendar)
        self.date_button_3_4.setObjectName(u"date_button_3_4")
        sizePolicy2.setHeightForWidth(self.date_button_3_4.sizePolicy().hasHeightForWidth())
        self.date_button_3_4.setSizePolicy(sizePolicy2)
        self.date_button_3_4.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_3_2 = QPushButton(self.calendar)
        self.date_button_3_2.setObjectName(u"date_button_3_2")
        sizePolicy2.setHeightForWidth(self.date_button_3_2.sizePolicy().hasHeightForWidth())
        self.date_button_3_2.setSizePolicy(sizePolicy2)
        self.date_button_3_2.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.week_6 = QLabel(self.calendar)
        self.week_6.setObjectName(u"week_6")
        self.week_6.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.week_6.sizePolicy().hasHeightForWidth())
        self.week_6.setSizePolicy(sizePolicy3)
        self.week_6.setMinimumSize(QSize(40, 50))
        self.week_6.setStyleSheet(u"QLabel[isWeekEnd=\"true\"]{\n"
"                                                                                    color: red;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QLabel[isWeekEnd=\"false\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"                                                                                ")
        self.week_6.setScaledContents(False)
        self.week_6.setAlignment(Qt.AlignCenter)
        self.week_6.setWordWrap(False)
        self.week_6.setMargin(2)
        self.week_6.setProperty("isWeekEnd", True)
        self.week_6.setProperty("Weekly", 7)

        self.gridLayout.addWidget(self.week_6, 0, 7, 1, 1)

        self.date_button_3_1 = QPushButton(self.calendar)
        self.date_button_3_1.setObjectName(u"date_button_3_1")
        sizePolicy2.setHeightForWidth(self.date_button_3_1.sizePolicy().hasHeightForWidth())
        self.date_button_3_1.setSizePolicy(sizePolicy2)
        self.date_button_3_1.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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
        self.week_0.setStyleSheet(u"QLabel[isWeekEnd=\"true\"]{\n"
"                                                                                    color: red;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QLabel[isWeekEnd=\"false\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"                                                                                ")
        self.week_0.setAlignment(Qt.AlignCenter)
        self.week_0.setWordWrap(False)
        self.week_0.setOpenExternalLinks(False)
        self.week_0.setProperty("isWeekEnd", False)
        self.week_0.setProperty("Weekly", 0)

        self.gridLayout.addWidget(self.week_0, 0, 0, 1, 1)

        self.date_button_5_5 = QPushButton(self.calendar)
        self.date_button_5_5.setObjectName(u"date_button_5_5")
        sizePolicy2.setHeightForWidth(self.date_button_5_5.sizePolicy().hasHeightForWidth())
        self.date_button_5_5.setSizePolicy(sizePolicy2)
        self.date_button_5_5.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_2_1 = QPushButton(self.calendar)
        self.date_button_2_1.setObjectName(u"date_button_2_1")
        sizePolicy2.setHeightForWidth(self.date_button_2_1.sizePolicy().hasHeightForWidth())
        self.date_button_2_1.setSizePolicy(sizePolicy2)
        self.date_button_2_1.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_2_3 = QPushButton(self.calendar)
        self.date_button_2_3.setObjectName(u"date_button_2_3")
        sizePolicy2.setHeightForWidth(self.date_button_2_3.sizePolicy().hasHeightForWidth())
        self.date_button_2_3.setSizePolicy(sizePolicy2)
        self.date_button_2_3.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.week_2 = QLabel(self.calendar)
        self.week_2.setObjectName(u"week_2")
        sizePolicy2.setHeightForWidth(self.week_2.sizePolicy().hasHeightForWidth())
        self.week_2.setSizePolicy(sizePolicy2)
        self.week_2.setMinimumSize(QSize(40, 50))
        self.week_2.setStyleSheet(u"QLabel[isWeekEnd=\"true\"]{\n"
"                                                                                    color: red;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QLabel[isWeekEnd=\"false\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"                                                                                ")
        self.week_2.setAlignment(Qt.AlignCenter)
        self.week_2.setProperty("isWeekEnd", False)
        self.week_2.setProperty("Weekly", 2)

        self.gridLayout.addWidget(self.week_2, 0, 3, 1, 1)

        self.date_button_4_4 = QPushButton(self.calendar)
        self.date_button_4_4.setObjectName(u"date_button_4_4")
        sizePolicy2.setHeightForWidth(self.date_button_4_4.sizePolicy().hasHeightForWidth())
        self.date_button_4_4.setSizePolicy(sizePolicy2)
        self.date_button_4_4.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.date_button_1_3 = QPushButton(self.calendar)
        self.date_button_1_3.setObjectName(u"date_button_1_3")
        sizePolicy2.setHeightForWidth(self.date_button_1_3.sizePolicy().hasHeightForWidth())
        self.date_button_1_3.setSizePolicy(sizePolicy2)
        self.date_button_1_3.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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

        self.week_1 = QLabel(self.calendar)
        self.week_1.setObjectName(u"week_1")
        sizePolicy2.setHeightForWidth(self.week_1.sizePolicy().hasHeightForWidth())
        self.week_1.setSizePolicy(sizePolicy2)
        self.week_1.setMinimumSize(QSize(40, 50))
        self.week_1.setStyleSheet(u"QLabel[isWeekEnd=\"true\"]{\n"
"                                                                                    color: red;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QLabel[isWeekEnd=\"false\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"                                                                                ")
        self.week_1.setAlignment(Qt.AlignCenter)
        self.week_1.setProperty("isWeekEnd", False)
        self.week_1.setProperty("Weekly", 1)

        self.gridLayout.addWidget(self.week_1, 0, 2, 1, 1)

        self.date_button_2_4 = QPushButton(self.calendar)
        self.date_button_2_4.setObjectName(u"date_button_2_4")
        sizePolicy2.setHeightForWidth(self.date_button_2_4.sizePolicy().hasHeightForWidth())
        self.date_button_2_4.setSizePolicy(sizePolicy2)
        self.date_button_2_4.setStyleSheet(u"QPushButton:hover {\n"
"                                                                                    background-color: rgba(0, 0, 0, 20);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton{\n"
"                                                                                    border:0px solid;\n"
"                                                                                    background-color: rgba(255, 255,\n"
"                                                                                    255, 0);\n"
"                                                                                    margin: 3px\n"
"                                                                                    }\n"
"\n"
"                                                     "
                        "                               QPushButton[toMonth=\"false\"]{\n"
"                                                                                    color: grey;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toMonth=\"true\"]{\n"
"                                                                                    color: black;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]{\n"
"                                                                                    background-color: rgba(20, 165, 255,\n"
"                                                                                    255);\n"
"                                                                                    color: white;\n"
"        "
                        "                                                                            border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:hover{\n"
"                                                                                    background-color:rgba(20, 165, 255,\n"
"                                                                                    200);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:pressed{\n"
"                                                           "
                        "                         background-color:rgba(20, 165, 255,\n"
"                                                                                    180);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton[toDay=\"true\"]:focus{\n"
"                                                                                    border:1px solid rgb(4, 80, 173);\n"
"                                                                                    color: white;\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"           "
                        "                                                                         QPushButton:pressed{\n"
"                                                                                    background-color: rgba(0, 0, 0, 15);\n"
"                                                                                    color:rgba(0, 0, 0, 180);\n"
"                                                                                    }\n"
"\n"
"                                                                                    QPushButton:focus{\n"
"                                                                                    border:1px solid rgba(0, 0, 0, 150);\n"
"                                                                                    border-radius: 7px;\n"
"                                                                                    }\n"
"\n"
"                                                                                ")
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


        self.verticalLayout_3.addWidget(self.calendar)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(41, 4, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.tab_home_verticalLayout.addLayout(self.verticalLayout_4)

        self.label_future = QLabel(self.tab_home)
        self.label_future.setObjectName(u"label_future")
        self.label_future.setTextFormat(Qt.AutoText)

        self.tab_home_verticalLayout.addWidget(self.label_future)

        self.label_past = QLabel(self.tab_home)
        self.label_past.setObjectName(u"label_past")
        self.label_past.setTextFormat(Qt.AutoText)

        self.tab_home_verticalLayout.addWidget(self.label_past)

        self.main_widget.addTab(self.tab_home, "")
        self.tab_calculte = QWidget()
        self.tab_calculte.setObjectName(u"tab_calculte")
        self.tab_calculte.setEnabled(True)
        self.tab_calculte_verticalLayout = QVBoxLayout(self.tab_calculte)
        self.tab_calculte_verticalLayout.setObjectName(u"tab_calculte_verticalLayout")
        self.tab_calculte_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tab_calculte_scrollArea = QScrollArea(self.tab_calculte)
        self.tab_calculte_scrollArea.setObjectName(u"tab_calculte_scrollArea")
        self.tab_calculte_scrollArea.setFrameShape(QFrame.NoFrame)
        self.tab_calculte_scrollArea.setLineWidth(0)
        self.tab_calculte_scrollArea.setWidgetResizable(True)
        self.tab_calculte_scrollAreaWidgetContents = QWidget()
        self.tab_calculte_scrollAreaWidgetContents.setObjectName(u"tab_calculte_scrollAreaWidgetContents")
        self.tab_calculte_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 770, 580))
        self.verticalLayout = QVBoxLayout(self.tab_calculte_scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(40, -1, -1, -1)
        self.date_delta_verticalLayout = QVBoxLayout()
        self.date_delta_verticalLayout.setSpacing(5)
        self.date_delta_verticalLayout.setObjectName(u"date_delta_verticalLayout")
        self.date_delta_title_label = QLabel(self.tab_calculte_scrollAreaWidgetContents)
        self.date_delta_title_label.setObjectName(u"date_delta_title_label")
        self.date_delta_title_label.setMinimumSize(QSize(0, 35))
        self.date_delta_title_label.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.date_delta_title_label.setFont(font1)

        self.date_delta_verticalLayout.addWidget(self.date_delta_title_label)

        self.date_delta_beginning_horizontalLayout = QHBoxLayout()
        self.date_delta_beginning_horizontalLayout.setSpacing(25)
        self.date_delta_beginning_horizontalLayout.setObjectName(u"date_delta_beginning_horizontalLayout")
        self.date_delta_beginning_horizontalLayout.setContentsMargins(25, 10, -1, -1)
        self.date_delta_beginning_label = QLabel(self.tab_calculte_scrollAreaWidgetContents)
        self.date_delta_beginning_label.setObjectName(u"date_delta_beginning_label")
        self.date_delta_beginning_label.setMinimumSize(QSize(150, 35))
        self.date_delta_beginning_label.setMaximumSize(QSize(150, 16777215))

        self.date_delta_beginning_horizontalLayout.addWidget(self.date_delta_beginning_label)

        self.date_delta_beginning_setter = QDateEdit(self.tab_calculte_scrollAreaWidgetContents)
        self.date_delta_beginning_setter.setObjectName(u"date_delta_beginning_setter")
        self.date_delta_beginning_setter.setMinimumSize(QSize(120, 0))
        self.date_delta_beginning_setter.setCalendarPopup(True)
        self.date_delta_beginning_setter.setTimeSpec(Qt.LocalTime)
        self.date_delta_beginning_setter.setDate(QDate(2001, 1, 1))

        self.date_delta_beginning_horizontalLayout.addWidget(self.date_delta_beginning_setter)

        self.date_delta_beginning_crazyDay_label = QLabel(self.tab_calculte_scrollAreaWidgetContents)
        self.date_delta_beginning_crazyDay_label.setObjectName(u"date_delta_beginning_crazyDay_label")

        self.date_delta_beginning_horizontalLayout.addWidget(self.date_delta_beginning_crazyDay_label)

        self.date_delta_beginning_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.date_delta_beginning_horizontalLayout.addItem(self.date_delta_beginning_horizontalSpacer)


        self.date_delta_verticalLayout.addLayout(self.date_delta_beginning_horizontalLayout)

        self.date_delta_ending_horizontalLayout = QHBoxLayout()
        self.date_delta_ending_horizontalLayout.setSpacing(25)
        self.date_delta_ending_horizontalLayout.setObjectName(u"date_delta_ending_horizontalLayout")
        self.date_delta_ending_horizontalLayout.setContentsMargins(25, -1, -1, -1)
        self.date_delta_ending_label = QLabel(self.tab_calculte_scrollAreaWidgetContents)
        self.date_delta_ending_label.setObjectName(u"date_delta_ending_label")
        self.date_delta_ending_label.setMinimumSize(QSize(150, 35))
        self.date_delta_ending_label.setMaximumSize(QSize(150, 16777215))

        self.date_delta_ending_horizontalLayout.addWidget(self.date_delta_ending_label)

        self.date_delta_ending_setter = QDateEdit(self.tab_calculte_scrollAreaWidgetContents)
        self.date_delta_ending_setter.setObjectName(u"date_delta_ending_setter")
        self.date_delta_ending_setter.setMinimumSize(QSize(120, 0))
        self.date_delta_ending_setter.setMaximumSize(QSize(120, 16777215))
        self.date_delta_ending_setter.setWrapping(True)
        self.date_delta_ending_setter.setAccelerated(False)
        self.date_delta_ending_setter.setCalendarPopup(True)
        self.date_delta_ending_setter.setDate(QDate(2001, 1, 1))

        self.date_delta_ending_horizontalLayout.addWidget(self.date_delta_ending_setter)

        self.date_delta_ending_crazyDay_label = QLabel(self.tab_calculte_scrollAreaWidgetContents)
        self.date_delta_ending_crazyDay_label.setObjectName(u"date_delta_ending_crazyDay_label")

        self.date_delta_ending_horizontalLayout.addWidget(self.date_delta_ending_crazyDay_label)

        self.date_delta_ending_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.date_delta_ending_horizontalLayout.addItem(self.date_delta_ending_horizontalSpacer)


        self.date_delta_verticalLayout.addLayout(self.date_delta_ending_horizontalLayout)

        self.date_delta_result_horizontalLayout = QHBoxLayout()
        self.date_delta_result_horizontalLayout.setSpacing(25)
        self.date_delta_result_horizontalLayout.setObjectName(u"date_delta_result_horizontalLayout")
        self.date_delta_result_horizontalLayout.setContentsMargins(25, -1, -1, 10)
        self.date_delta_result_label = QLabel(self.tab_calculte_scrollAreaWidgetContents)
        self.date_delta_result_label.setObjectName(u"date_delta_result_label")
        self.date_delta_result_label.setMinimumSize(QSize(150, 35))
        self.date_delta_result_label.setMaximumSize(QSize(150, 16777215))

        self.date_delta_result_horizontalLayout.addWidget(self.date_delta_result_label)

        self.date_delta_result_shower = QSpinBox(self.tab_calculte_scrollAreaWidgetContents)
        self.date_delta_result_shower.setObjectName(u"date_delta_result_shower")
        self.date_delta_result_shower.setMinimumSize(QSize(120, 0))
        self.date_delta_result_shower.setFrame(True)
        self.date_delta_result_shower.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.date_delta_result_shower.setReadOnly(True)
        self.date_delta_result_shower.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date_delta_result_shower.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.date_delta_result_shower.setKeyboardTracking(True)
        self.date_delta_result_shower.setMaximum(999999999)
        self.date_delta_result_shower.setValue(0)

        self.date_delta_result_horizontalLayout.addWidget(self.date_delta_result_shower)

        self.date_delta_result_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.date_delta_result_horizontalLayout.addItem(self.date_delta_result_horizontalSpacer)


        self.date_delta_verticalLayout.addLayout(self.date_delta_result_horizontalLayout)


        self.verticalLayout.addLayout(self.date_delta_verticalLayout)

        self.date_add_sub_verticalLayout = QVBoxLayout()
        self.date_add_sub_verticalLayout.setSpacing(5)
        self.date_add_sub_verticalLayout.setObjectName(u"date_add_sub_verticalLayout")
        self.date_add_sub_title_label = QLabel(self.tab_calculte_scrollAreaWidgetContents)
        self.date_add_sub_title_label.setObjectName(u"date_add_sub_title_label")
        self.date_add_sub_title_label.setMinimumSize(QSize(0, 35))
        self.date_add_sub_title_label.setMaximumSize(QSize(16777215, 50))
        self.date_add_sub_title_label.setFont(font1)

        self.date_add_sub_verticalLayout.addWidget(self.date_add_sub_title_label)

        self.date_add_sub_begining_horizontalLayout = QHBoxLayout()
        self.date_add_sub_begining_horizontalLayout.setSpacing(25)
        self.date_add_sub_begining_horizontalLayout.setObjectName(u"date_add_sub_begining_horizontalLayout")
        self.date_add_sub_begining_horizontalLayout.setContentsMargins(25, 10, -1, -1)
        self.date_add_sub_begining_label = QLabel(self.tab_calculte_scrollAreaWidgetContents)
        self.date_add_sub_begining_label.setObjectName(u"date_add_sub_begining_label")
        self.date_add_sub_begining_label.setMinimumSize(QSize(150, 35))
        self.date_add_sub_begining_label.setMaximumSize(QSize(150, 16777215))

        self.date_add_sub_begining_horizontalLayout.addWidget(self.date_add_sub_begining_label)

        self.date_add_sub_begining_setter = QDateEdit(self.tab_calculte_scrollAreaWidgetContents)
        self.date_add_sub_begining_setter.setObjectName(u"date_add_sub_begining_setter")
        self.date_add_sub_begining_setter.setMinimumSize(QSize(120, 0))
        self.date_add_sub_begining_setter.setCalendarPopup(True)
        self.date_add_sub_begining_setter.setTimeSpec(Qt.LocalTime)
        self.date_add_sub_begining_setter.setDate(QDate(2001, 1, 1))

        self.date_add_sub_begining_horizontalLayout.addWidget(self.date_add_sub_begining_setter)

        self.date_add_sub_begining_crazyDay_label = QLabel(self.tab_calculte_scrollAreaWidgetContents)
        self.date_add_sub_begining_crazyDay_label.setObjectName(u"date_add_sub_begining_crazyDay_label")

        self.date_add_sub_begining_horizontalLayout.addWidget(self.date_add_sub_begining_crazyDay_label)

        self.date_add_sub_begining_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.date_add_sub_begining_horizontalLayout.addItem(self.date_add_sub_begining_horizontalSpacer)


        self.date_add_sub_verticalLayout.addLayout(self.date_add_sub_begining_horizontalLayout)

        self.date_add_sub_delta_day_horizontalLayout = QHBoxLayout()
        self.date_add_sub_delta_day_horizontalLayout.setSpacing(25)
        self.date_add_sub_delta_day_horizontalLayout.setObjectName(u"date_add_sub_delta_day_horizontalLayout")
        self.date_add_sub_delta_day_horizontalLayout.setContentsMargins(25, -1, -1, 0)
        self.date_add_sub_delta_day_label = QLabel(self.tab_calculte_scrollAreaWidgetContents)
        self.date_add_sub_delta_day_label.setObjectName(u"date_add_sub_delta_day_label")
        self.date_add_sub_delta_day_label.setMinimumSize(QSize(150, 35))
        self.date_add_sub_delta_day_label.setMaximumSize(QSize(150, 16777215))

        self.date_add_sub_delta_day_horizontalLayout.addWidget(self.date_add_sub_delta_day_label)

        self.date_add_sub_delta_day_setter = QSpinBox(self.tab_calculte_scrollAreaWidgetContents)
        self.date_add_sub_delta_day_setter.setObjectName(u"date_add_sub_delta_day_setter")
        sizePolicy4.setHeightForWidth(self.date_add_sub_delta_day_setter.sizePolicy().hasHeightForWidth())
        self.date_add_sub_delta_day_setter.setSizePolicy(sizePolicy4)
        self.date_add_sub_delta_day_setter.setMinimumSize(QSize(120, 0))
        self.date_add_sub_delta_day_setter.setFrame(True)
        self.date_add_sub_delta_day_setter.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.date_add_sub_delta_day_setter.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date_add_sub_delta_day_setter.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.date_add_sub_delta_day_setter.setKeyboardTracking(True)
        self.date_add_sub_delta_day_setter.setMinimum(-999999999)
        self.date_add_sub_delta_day_setter.setMaximum(999999999)
        self.date_add_sub_delta_day_setter.setValue(0)

        self.date_add_sub_delta_day_horizontalLayout.addWidget(self.date_add_sub_delta_day_setter)

        self.date_add_sub_delta_day_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.date_add_sub_delta_day_horizontalLayout.addItem(self.date_add_sub_delta_day_horizontalSpacer)


        self.date_add_sub_verticalLayout.addLayout(self.date_add_sub_delta_day_horizontalLayout)

        self.date_add_sub_ending_horizontalLayout = QHBoxLayout()
        self.date_add_sub_ending_horizontalLayout.setSpacing(25)
        self.date_add_sub_ending_horizontalLayout.setObjectName(u"date_add_sub_ending_horizontalLayout")
        self.date_add_sub_ending_horizontalLayout.setContentsMargins(25, -1, -1, 11)
        self.date_add_sub_ending_label = QLabel(self.tab_calculte_scrollAreaWidgetContents)
        self.date_add_sub_ending_label.setObjectName(u"date_add_sub_ending_label")
        self.date_add_sub_ending_label.setMinimumSize(QSize(150, 35))
        self.date_add_sub_ending_label.setMaximumSize(QSize(150, 16777215))

        self.date_add_sub_ending_horizontalLayout.addWidget(self.date_add_sub_ending_label)

        self.date_add_sub_ending_shower = QDateEdit(self.tab_calculte_scrollAreaWidgetContents)
        self.date_add_sub_ending_shower.setObjectName(u"date_add_sub_ending_shower")
        self.date_add_sub_ending_shower.setMinimumSize(QSize(120, 0))
        self.date_add_sub_ending_shower.setWrapping(True)
        self.date_add_sub_ending_shower.setReadOnly(True)
        self.date_add_sub_ending_shower.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date_add_sub_ending_shower.setAccelerated(False)
        self.date_add_sub_ending_shower.setCalendarPopup(False)
        self.date_add_sub_ending_shower.setDate(QDate(2001, 1, 1))

        self.date_add_sub_ending_horizontalLayout.addWidget(self.date_add_sub_ending_shower)

        self.date_add_sub_ending_crazyDay_label = QLabel(self.tab_calculte_scrollAreaWidgetContents)
        self.date_add_sub_ending_crazyDay_label.setObjectName(u"date_add_sub_ending_crazyDay_label")

        self.date_add_sub_ending_horizontalLayout.addWidget(self.date_add_sub_ending_crazyDay_label)

        self.date_add_sub_ending_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.date_add_sub_ending_horizontalLayout.addItem(self.date_add_sub_ending_horizontalSpacer)


        self.date_add_sub_verticalLayout.addLayout(self.date_add_sub_ending_horizontalLayout)


        self.verticalLayout.addLayout(self.date_add_sub_verticalLayout)

        self.crazyDay_verticalLayout = QVBoxLayout()
        self.crazyDay_verticalLayout.setSpacing(5)
        self.crazyDay_verticalLayout.setObjectName(u"crazyDay_verticalLayout")
        self.crazyDay_title_label = QLabel(self.tab_calculte_scrollAreaWidgetContents)
        self.crazyDay_title_label.setObjectName(u"crazyDay_title_label")
        self.crazyDay_title_label.setMinimumSize(QSize(0, 35))
        self.crazyDay_title_label.setMaximumSize(QSize(16777215, 50))
        self.crazyDay_title_label.setFont(font1)

        self.crazyDay_verticalLayout.addWidget(self.crazyDay_title_label)

        self.crazyDay_beginning_horizontalLayout = QHBoxLayout()
        self.crazyDay_beginning_horizontalLayout.setSpacing(25)
        self.crazyDay_beginning_horizontalLayout.setObjectName(u"crazyDay_beginning_horizontalLayout")
        self.crazyDay_beginning_horizontalLayout.setContentsMargins(25, 10, -1, -1)
        self.crazyDay_beginning_label = QLabel(self.tab_calculte_scrollAreaWidgetContents)
        self.crazyDay_beginning_label.setObjectName(u"crazyDay_beginning_label")
        self.crazyDay_beginning_label.setMinimumSize(QSize(150, 35))
        self.crazyDay_beginning_label.setMaximumSize(QSize(150, 16777215))

        self.crazyDay_beginning_horizontalLayout.addWidget(self.crazyDay_beginning_label)

        self.crazyDay_beginning_setter = QDateEdit(self.tab_calculte_scrollAreaWidgetContents)
        self.crazyDay_beginning_setter.setObjectName(u"crazyDay_beginning_setter")
        self.crazyDay_beginning_setter.setMinimumSize(QSize(120, 0))
        self.crazyDay_beginning_setter.setCalendarPopup(True)
        self.crazyDay_beginning_setter.setTimeSpec(Qt.LocalTime)
        self.crazyDay_beginning_setter.setDate(QDate(2001, 1, 1))

        self.crazyDay_beginning_horizontalLayout.addWidget(self.crazyDay_beginning_setter)

        self.crazyDay_beginning_crazyDay_label = QLabel(self.tab_calculte_scrollAreaWidgetContents)
        self.crazyDay_beginning_crazyDay_label.setObjectName(u"crazyDay_beginning_crazyDay_label")

        self.crazyDay_beginning_horizontalLayout.addWidget(self.crazyDay_beginning_crazyDay_label)

        self.crazyDay_beginning_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.crazyDay_beginning_horizontalLayout.addItem(self.crazyDay_beginning_horizontalSpacer)


        self.crazyDay_verticalLayout.addLayout(self.crazyDay_beginning_horizontalLayout)

        self.crazyDay_ending_horizontalLayout = QHBoxLayout()
        self.crazyDay_ending_horizontalLayout.setSpacing(25)
        self.crazyDay_ending_horizontalLayout.setObjectName(u"crazyDay_ending_horizontalLayout")
        self.crazyDay_ending_horizontalLayout.setContentsMargins(25, -1, -1, -1)
        self.crazyDay_ending_label = QLabel(self.tab_calculte_scrollAreaWidgetContents)
        self.crazyDay_ending_label.setObjectName(u"crazyDay_ending_label")
        self.crazyDay_ending_label.setMinimumSize(QSize(150, 35))
        self.crazyDay_ending_label.setMaximumSize(QSize(150, 16777215))

        self.crazyDay_ending_horizontalLayout.addWidget(self.crazyDay_ending_label)

        self.crazyDay_ending_setter = QDateEdit(self.tab_calculte_scrollAreaWidgetContents)
        self.crazyDay_ending_setter.setObjectName(u"crazyDay_ending_setter")
        self.crazyDay_ending_setter.setMinimumSize(QSize(120, 0))
        self.crazyDay_ending_setter.setMaximumSize(QSize(120, 16777215))
        self.crazyDay_ending_setter.setWrapping(True)
        self.crazyDay_ending_setter.setAccelerated(False)
        self.crazyDay_ending_setter.setCalendarPopup(True)
        self.crazyDay_ending_setter.setDate(QDate(2001, 1, 1))

        self.crazyDay_ending_horizontalLayout.addWidget(self.crazyDay_ending_setter)

        self.crazyDay_ending_crazyDay_label = QLabel(self.tab_calculte_scrollAreaWidgetContents)
        self.crazyDay_ending_crazyDay_label.setObjectName(u"crazyDay_ending_crazyDay_label")

        self.crazyDay_ending_horizontalLayout.addWidget(self.crazyDay_ending_crazyDay_label)

        self.crazyDay_ending_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.crazyDay_ending_horizontalLayout.addItem(self.crazyDay_ending_horizontalSpacer)


        self.crazyDay_verticalLayout.addLayout(self.crazyDay_ending_horizontalLayout)

        self.crazyDay_result_horizontalLayout = QHBoxLayout()
        self.crazyDay_result_horizontalLayout.setSpacing(25)
        self.crazyDay_result_horizontalLayout.setObjectName(u"crazyDay_result_horizontalLayout")
        self.crazyDay_result_horizontalLayout.setContentsMargins(25, -1, -1, 10)
        self.crazyDay_result_label = QLabel(self.tab_calculte_scrollAreaWidgetContents)
        self.crazyDay_result_label.setObjectName(u"crazyDay_result_label")
        self.crazyDay_result_label.setMinimumSize(QSize(150, 35))
        self.crazyDay_result_label.setMaximumSize(QSize(150, 16777215))

        self.crazyDay_result_horizontalLayout.addWidget(self.crazyDay_result_label)

        self.crazyDay_result_shower = QSpinBox(self.tab_calculte_scrollAreaWidgetContents)
        self.crazyDay_result_shower.setObjectName(u"crazyDay_result_shower")
        self.crazyDay_result_shower.setMinimumSize(QSize(120, 0))
        self.crazyDay_result_shower.setFrame(True)
        self.crazyDay_result_shower.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.crazyDay_result_shower.setReadOnly(True)
        self.crazyDay_result_shower.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.crazyDay_result_shower.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.crazyDay_result_shower.setKeyboardTracking(True)
        self.crazyDay_result_shower.setMaximum(999999999)
        self.crazyDay_result_shower.setValue(0)

        self.crazyDay_result_horizontalLayout.addWidget(self.crazyDay_result_shower)

        self.crazyDay_result_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.crazyDay_result_horizontalLayout.addItem(self.crazyDay_result_horizontalSpacer)


        self.crazyDay_verticalLayout.addLayout(self.crazyDay_result_horizontalLayout)


        self.verticalLayout.addLayout(self.crazyDay_verticalLayout)

        self.tab_calculte_scrollArea.setWidget(self.tab_calculte_scrollAreaWidgetContents)

        self.tab_calculte_verticalLayout.addWidget(self.tab_calculte_scrollArea)

        self.main_widget.addTab(self.tab_calculte, "")
        self.tab_setting = QWidget()
        self.tab_setting.setObjectName(u"tab_setting")
        self.tab_setting_verticalLayout = QVBoxLayout(self.tab_setting)
        self.tab_setting_verticalLayout.setObjectName(u"tab_setting_verticalLayout")
        self.tab_setting_verticalLayout.setContentsMargins(40, -1, 11, -1)
        self.onlyShowCrazyDay_setter_horizontalLayout = QHBoxLayout()
        self.onlyShowCrazyDay_setter_horizontalLayout.setSpacing(25)
        self.onlyShowCrazyDay_setter_horizontalLayout.setObjectName(u"onlyShowCrazyDay_setter_horizontalLayout")
        self.onlyShowCrazyDay_setter_label = QLabel(self.tab_setting)
        self.onlyShowCrazyDay_setter_label.setObjectName(u"onlyShowCrazyDay_setter_label")
        self.onlyShowCrazyDay_setter_label.setMinimumSize(QSize(150, 65))
        self.onlyShowCrazyDay_setter_label.setMaximumSize(QSize(150, 65))

        self.onlyShowCrazyDay_setter_horizontalLayout.addWidget(self.onlyShowCrazyDay_setter_label)

        self.onlyShowCrazyDay_setter = QCheckBox(self.tab_setting)
        self.onlyShowCrazyDay_setter.setObjectName(u"onlyShowCrazyDay_setter")
        self.onlyShowCrazyDay_setter.setChecked(True)

        self.onlyShowCrazyDay_setter_horizontalLayout.addWidget(self.onlyShowCrazyDay_setter)

        self.onlyShowCrazyDay_setter_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.onlyShowCrazyDay_setter_horizontalLayout.addItem(self.onlyShowCrazyDay_setter_horizontalSpacer)


        self.tab_setting_verticalLayout.addLayout(self.onlyShowCrazyDay_setter_horizontalLayout)

        self.weekStyle_setter_horizontalLayout = QHBoxLayout()
        self.weekStyle_setter_horizontalLayout.setSpacing(25)
        self.weekStyle_setter_horizontalLayout.setObjectName(u"weekStyle_setter_horizontalLayout")
        self.weekStyle_setter_label = QLabel(self.tab_setting)
        self.weekStyle_setter_label.setObjectName(u"weekStyle_setter_label")
        self.weekStyle_setter_label.setMinimumSize(QSize(150, 65))
        self.weekStyle_setter_label.setMaximumSize(QSize(150, 65))

        self.weekStyle_setter_horizontalLayout.addWidget(self.weekStyle_setter_label)

        self.weekStyle_setter = QComboBox(self.tab_setting)
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.addItem("")
        self.weekStyle_setter.setObjectName(u"weekStyle_setter")
        self.weekStyle_setter.setMinimumSize(QSize(200, 0))
        self.weekStyle_setter.setMaximumSize(QSize(200, 16777215))
        self.weekStyle_setter.setLayoutDirection(Qt.LeftToRight)
        self.weekStyle_setter.setAutoFillBackground(False)

        self.weekStyle_setter_horizontalLayout.addWidget(self.weekStyle_setter)

        self.weekStyle_setter_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.weekStyle_setter_horizontalLayout.addItem(self.weekStyle_setter_horizontalSpacer)


        self.tab_setting_verticalLayout.addLayout(self.weekStyle_setter_horizontalLayout)

        self.weekFirstDay_setter_layout = QHBoxLayout()
        self.weekFirstDay_setter_layout.setSpacing(25)
        self.weekFirstDay_setter_layout.setObjectName(u"weekFirstDay_setter_layout")
        self.weekFirstDay_setter_label = QLabel(self.tab_setting)
        self.weekFirstDay_setter_label.setObjectName(u"weekFirstDay_setter_label")
        self.weekFirstDay_setter_label.setMinimumSize(QSize(150, 65))
        self.weekFirstDay_setter_label.setMaximumSize(QSize(150, 65))

        self.weekFirstDay_setter_layout.addWidget(self.weekFirstDay_setter_label)

        self.weekFirstDay_setter = QComboBox(self.tab_setting)
        self.weekFirstDay_setter.addItem("")
        self.weekFirstDay_setter.addItem("")
        self.weekFirstDay_setter.addItem("")
        self.weekFirstDay_setter.addItem("")
        self.weekFirstDay_setter.addItem("")
        self.weekFirstDay_setter.addItem("")
        self.weekFirstDay_setter.addItem("")
        self.weekFirstDay_setter.setObjectName(u"weekFirstDay_setter")
        self.weekFirstDay_setter.setMinimumSize(QSize(120, 0))
        self.weekFirstDay_setter.setMaximumSize(QSize(100, 16777215))
        self.weekFirstDay_setter.setLayoutDirection(Qt.LeftToRight)
        self.weekFirstDay_setter.setAutoFillBackground(False)

        self.weekFirstDay_setter_layout.addWidget(self.weekFirstDay_setter)

        self.weekFirstDay_setter_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.weekFirstDay_setter_layout.addItem(self.weekFirstDay_setter_horizontalSpacer)


        self.tab_setting_verticalLayout.addLayout(self.weekFirstDay_setter_layout)

        self.crazyDay_setter_layout = QHBoxLayout()
        self.crazyDay_setter_layout.setSpacing(25)
        self.crazyDay_setter_layout.setObjectName(u"crazyDay_setter_layout")
        self.crazyDay_setter_label = QLabel(self.tab_setting)
        self.crazyDay_setter_label.setObjectName(u"crazyDay_setter_label")
        self.crazyDay_setter_label.setMinimumSize(QSize(150, 65))
        self.crazyDay_setter_label.setMaximumSize(QSize(150, 65))

        self.crazyDay_setter_layout.addWidget(self.crazyDay_setter_label)

        self.crazyDay_setter = QComboBox(self.tab_setting)
        self.crazyDay_setter.addItem("")
        self.crazyDay_setter.addItem("")
        self.crazyDay_setter.addItem("")
        self.crazyDay_setter.addItem("")
        self.crazyDay_setter.addItem("")
        self.crazyDay_setter.addItem("")
        self.crazyDay_setter.addItem("")
        self.crazyDay_setter.setObjectName(u"crazyDay_setter")
        self.crazyDay_setter.setMinimumSize(QSize(120, 0))
        self.crazyDay_setter.setMaximumSize(QSize(100, 16777215))
        self.crazyDay_setter.setLayoutDirection(Qt.LeftToRight)
        self.crazyDay_setter.setAutoFillBackground(False)

        self.crazyDay_setter_layout.addWidget(self.crazyDay_setter)

        self.crazyDay_setter_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.crazyDay_setter_layout.addItem(self.crazyDay_setter_horizontalSpacer)


        self.tab_setting_verticalLayout.addLayout(self.crazyDay_setter_layout)

        self.tab_setting_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.tab_setting_verticalLayout.addItem(self.tab_setting_verticalSpacer)

        self.main_widget.addTab(self.tab_setting, "")

        self.horizontalLayout_7.addWidget(self.main_widget)

        MainWindow.setCentralWidget(self.central_widget)
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

        self.main_widget.setCurrentIndex(1)
        self.next_button.setDefault(False)
        self.date_button_4_6.setDefault(False)
        self.date_button_2_0.setDefault(False)
        self.date_button_3_6.setDefault(False)
        self.date_button_2_6.setDefault(False)
        self.date_button_1_6.setDefault(False)
        self.date_button_0_1.setDefault(False)
        self.date_button_0_4.setDefault(False)
        self.date_button_1_0.setDefault(False)
        self.date_button_0_0.setDefault(False)
        self.date_button_3_5.setDefault(False)
        self.date_button_4_1.setDefault(False)
        self.date_button_1_4.setDefault(False)
        self.date_button_2_2.setDefault(False)
        self.date_button_3_0.setDefault(False)
        self.date_button_3_3.setDefault(False)
        self.date_button_5_4.setDefault(False)
        self.date_button_1_2.setDefault(False)
        self.date_button_5_0.setDefault(False)
        self.date_button_0_3.setDefault(False)
        self.date_button_0_2.setDefault(False)
        self.date_button_5_1.setDefault(False)
        self.date_button_0_6.setDefault(False)
        self.date_button_1_1.setDefault(False)
        self.date_button_5_2.setDefault(False)
        self.date_button_2_5.setDefault(False)
        self.date_button_4_2.setDefault(False)
        self.date_button_5_6.setDefault(False)
        self.date_button_5_3.setDefault(False)
        self.date_button_1_5.setDefault(False)
        self.date_button_4_5.setDefault(False)
        self.date_button_4_0.setDefault(False)
        self.date_button_0_5.setDefault(False)
        self.date_button_3_4.setDefault(False)
        self.date_button_3_2.setDefault(False)
        self.date_button_3_1.setDefault(False)
        self.date_button_5_5.setDefault(False)
        self.date_button_4_3.setDefault(False)
        self.date_button_2_1.setDefault(False)
        self.date_button_2_3.setDefault(False)
        self.date_button_4_4.setDefault(False)
        self.date_button_1_3.setDefault(False)
        self.date_button_2_4.setDefault(False)
        self.weekStyle_setter.setCurrentIndex(0)
        self.weekFirstDay_setter.setCurrentIndex(0)
        self.crazyDay_setter.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"KFC Calendar", None))
        self.label_nowtime.setText(QCoreApplication.translate("MainWindow", u"\u516c\u51430000\u5e74 00\u670800\u65e5 \u661f\u671f0 00:00:00", None))
        self.goback_button.setText(QCoreApplication.translate("MainWindow", u"\u56de\u5230\u4eca\u5929", None))
        self.left_button.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.year_edit.setSuffix(QCoreApplication.translate("MainWindow", u"\u5e74", None))
        self.month_edit.setSuffix(QCoreApplication.translate("MainWindow", u"\u6708", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.date_button_4_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_2_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_3_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_2_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_1_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_0_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_0_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_1_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_0_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_3_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.week_5.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u516d", None))
        self.date_button_4_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_1_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_2_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_3_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_3_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_5_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_1_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_5_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_0_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_0_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.week_4.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e94", None))
        self.date_button_5_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_0_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_1_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_5_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.week_3.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u56db", None))
        self.date_button_2_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_4_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_5_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_5_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_1_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_4_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_4_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_0_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_3_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_3_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.week_6.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u5929", None))
        self.date_button_3_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.week_0.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e00", None))
        self.date_button_5_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_4_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_2_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_2_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.week_2.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e09", None))
        self.date_button_4_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.date_button_1_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.week_1.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e8c", None))
        self.date_button_2_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_future.setToolTip(QCoreApplication.translate("MainWindow", u"\u4eca\u5929\u4f60\u53c8\u79bb\u75af\u72c2\u661f\u671f\u56db\u66f4\u8fd1\u4e86\u4e00\u6b65", None))
#endif // QT_CONFIG(tooltip)
        self.label_future.setText(QCoreApplication.translate("MainWindow", u"\u5c55\u671b\u672a\u6765\uff1a\u8fd8\u67090\u5929\u5230\u4e0b\u4e00\u4e2a\u75af\u72c2\u661f\u671f\u56db", None))
#if QT_CONFIG(tooltip)
        self.label_past.setToolTip(QCoreApplication.translate("MainWindow", u"\u8fc7\u53bb\u4ece\u672a\u6d88\u901d\uff0c\u751a\u81f3\u4ece\u672a\u8fc7\u53bb\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.label_past.setText(QCoreApplication.translate("MainWindow", u"\u56de\u9996\u8fc7\u53bb\uff1a\u8ddd\u79bb\u4e0a\u4e2a\u75af\u72c2\u661f\u671f\u56db\u5df2\u7ecf\u8fc7\u4e860\u5929", None))
        self.main_widget.setTabText(self.main_widget.indexOf(self.tab_home), QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.date_delta_title_label.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u671f\u4e4b\u95f4\u7684\u95f4\u9694\u65f6\u95f4", None))
        self.date_delta_beginning_label.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65e5\u671f", None))
        self.date_delta_beginning_crazyDay_label.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u5929\u662f\u75af\u72c2\u661f\u671f\u56db\uff01\uff01", None))
        self.date_delta_ending_label.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u65e5\u671f", None))
        self.date_delta_ending_crazyDay_label.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u5929\u662f\u75af\u72c2\u661f\u671f\u56db\uff01\uff01", None))
        self.date_delta_result_label.setText(QCoreApplication.translate("MainWindow", u"\u5dee\u503c", None))
        self.date_delta_result_shower.setSuffix(QCoreApplication.translate("MainWindow", u"\u5929", None))
        self.date_add_sub_title_label.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6216\u51cf\u53bb\u5929\u6570", None))
        self.date_add_sub_begining_label.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65e5\u671f", None))
        self.date_add_sub_begining_crazyDay_label.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u5929\u662f\u75af\u72c2\u661f\u671f\u56db\uff01\uff01", None))
        self.date_add_sub_delta_day_label.setText(QCoreApplication.translate("MainWindow", u"\u5929\u6570", None))
        self.date_add_sub_delta_day_setter.setSuffix(QCoreApplication.translate("MainWindow", u"\u5929", None))
        self.date_add_sub_ending_label.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u65e5\u671f", None))
        self.date_add_sub_ending_crazyDay_label.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u5929\u662f\u75af\u72c2\u661f\u671f\u56db\uff01\uff01", None))
        self.crazyDay_title_label.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u671f\u4e4b\u95f4\u7684\u75af\u72c2\u661f\u671f\u56db", None))
        self.crazyDay_beginning_label.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65e5\u671f", None))
        self.crazyDay_beginning_crazyDay_label.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u5929\u662f\u75af\u72c2\u661f\u671f\u56db\uff01\uff01", None))
        self.crazyDay_ending_label.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u65e5\u671f", None))
        self.crazyDay_ending_crazyDay_label.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u5929\u662f\u75af\u72c2\u661f\u671f\u56db\uff01\uff01", None))
        self.crazyDay_result_label.setText(QCoreApplication.translate("MainWindow", u"\u75af\u72c2\u661f\u671f\u56db\u5929\u6570", None))
        self.crazyDay_result_shower.setSuffix(QCoreApplication.translate("MainWindow", u"\u5929", None))
        self.main_widget.setTabText(self.main_widget.indexOf(self.tab_calculte), QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
        self.onlyShowCrazyDay_setter_label.setText(QCoreApplication.translate("MainWindow", u"\u53ea\u663e\u793a\u75af\u72c2\u661f\u671f\u56db", None))
#if QT_CONFIG(tooltip)
        self.onlyShowCrazyDay_setter.setToolTip(QCoreApplication.translate("MainWindow", u"\u4e3a\u75af\u72c2\u661f\u671f\u56db\u732e\u4e0a\u5fc3\u810f\uff01\uff01\uff01\uff01\uff01\uff01", None))
#endif // QT_CONFIG(tooltip)
        self.onlyShowCrazyDay_setter.setText("")
        self.weekStyle_setter_label.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u6837\u5f0f", None))
        self.weekStyle_setter.setItemText(0, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e00,...,\u661f\u671f\u5929", None))
        self.weekStyle_setter.setItemText(1, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u58f9,...,\u661f\u671f\u5929", None))
        self.weekStyle_setter.setItemText(2, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e00,...,\u661f\u671f\u65e5", None))
        self.weekStyle_setter.setItemText(3, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u58f9,...,\u661f\u671f\u65e5", None))
        self.weekStyle_setter.setItemText(4, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e00,...,\u661f\u671f\u4e03", None))
        self.weekStyle_setter.setItemText(5, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u58f9,...,\u661f\u671f\u67d2", None))
        self.weekStyle_setter.setItemText(6, QCoreApplication.translate("MainWindow", u"\u5468\u4e00,...,\u5468\u65e5", None))
        self.weekStyle_setter.setItemText(7, QCoreApplication.translate("MainWindow", u"\u5468\u58f9,...,\u5468\u65e5", None))
        self.weekStyle_setter.setItemText(8, QCoreApplication.translate("MainWindow", u"\u5468\u4e00,...,\u5468\u5929", None))
        self.weekStyle_setter.setItemText(9, QCoreApplication.translate("MainWindow", u"\u5468\u58f9,...,\u5468\u5929", None))
        self.weekStyle_setter.setItemText(10, QCoreApplication.translate("MainWindow", u"\u5468\u4e00,...,\u5468\u4e03", None))
        self.weekStyle_setter.setItemText(11, QCoreApplication.translate("MainWindow", u"\u5468\u58f9,...,\u5468\u67d2", None))
        self.weekStyle_setter.setItemText(12, QCoreApplication.translate("MainWindow", u"\u4e00,...,\u65e5", None))
        self.weekStyle_setter.setItemText(13, QCoreApplication.translate("MainWindow", u"\u58f9,...,\u65e5", None))
        self.weekStyle_setter.setItemText(14, QCoreApplication.translate("MainWindow", u"\u4e00,...,\u5929", None))
        self.weekStyle_setter.setItemText(15, QCoreApplication.translate("MainWindow", u"\u58f9,...,\u5929", None))
        self.weekStyle_setter.setItemText(16, QCoreApplication.translate("MainWindow", u"\u4e00,...,\u4e03", None))
        self.weekStyle_setter.setItemText(17, QCoreApplication.translate("MainWindow", u"\u58f9,...,\u67d2", None))
        self.weekStyle_setter.setItemText(18, QCoreApplication.translate("MainWindow", u"1,...,7", None))
        self.weekStyle_setter.setItemText(19, QCoreApplication.translate("MainWindow", u"Mon.,...,Sun.", None))
        self.weekStyle_setter.setItemText(20, QCoreApplication.translate("MainWindow", u"\u2160,...,\u2166", None))

        self.weekFirstDay_setter_label.setText(QCoreApplication.translate("MainWindow", u"\u6bcf\u661f\u671f\u7684\u7b2c\u4e00\u5929", None))
        self.weekFirstDay_setter.setItemText(0, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e00", None))
        self.weekFirstDay_setter.setItemText(1, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e8c", None))
        self.weekFirstDay_setter.setItemText(2, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e09", None))
        self.weekFirstDay_setter.setItemText(3, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u56db", None))
        self.weekFirstDay_setter.setItemText(4, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e94", None))
        self.weekFirstDay_setter.setItemText(5, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u516d", None))
        self.weekFirstDay_setter.setItemText(6, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u5929", None))

        self.crazyDay_setter_label.setText(QCoreApplication.translate("MainWindow", u"\u6bcf\u661f\u671f\u7684\u75af\u72c2\u65e5", None))
        self.crazyDay_setter.setItemText(0, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e00", None))
        self.crazyDay_setter.setItemText(1, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e8c", None))
        self.crazyDay_setter.setItemText(2, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e09", None))
        self.crazyDay_setter.setItemText(3, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u56db", None))
        self.crazyDay_setter.setItemText(4, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e94", None))
        self.crazyDay_setter.setItemText(5, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u516d", None))
        self.crazyDay_setter.setItemText(6, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u5929", None))

#if QT_CONFIG(tooltip)
        self.crazyDay_setter.setToolTip(QCoreApplication.translate("MainWindow", u"\u4f60\u7684\u75af\u72c2\u661f\u671f\u56db\uff0c\u53c8\u4f55\u5fc5\u662f\u661f\u671f\u56db\uff1f", None))
#endif // QT_CONFIG(tooltip)
        self.main_widget.setTabText(self.main_widget.indexOf(self.tab_setting), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
    # retranslateUi

