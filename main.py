# main.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-10 11:57
# @Software: PyCharm
# @Project: KFC-Calendar

"""
None
"""
import os
import sys
import datetime
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_calendar import Ui_MainWindow

ONLY_SHOW_THURSDAY = False


def get_days(year: int, month: int) -> int:
    """
    获取指定月份的天数

    :param year: 年
    :param month: 月
    :return: 天数
    """
    if 0 < month < 12:
        return (datetime.datetime(year, month + 1, 1) - datetime.datetime(year, month, 1)).days
    elif month == 0:
        return (datetime.datetime(year, 1, 1) - datetime.datetime(year - 1, 12, 1)).days
    else:
        return (datetime.datetime(year + 1, 1, 1) - datetime.datetime(year, 12, 1)).days


def get_datetime(year: int, month: int, day: int) -> datetime.datetime:
    """
    获取合法的datetime

    :param year: 年
    :param month: 月
    :param day: 日
    :return: 合法的datetime
    """
    if month == 13:
        month = 1
        year += 1
    elif month == 0:
        month = 12
        year -= 1

    if day == get_days(year, month) + 1:
        day = 1
        month += 1
    elif day == 0:
        day = get_days(year, month - 1)
        month -= 1

    if month == 13:
        month = 1
        year += 1
    elif month == 0:
        month = 12
        year -= 1

    return datetime.datetime(year, month, day)


class Calendar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.widget_connect()
        self.update_calendar()

    def setupUi(self, MainWindow: QMainWindow):
        super().setupUi(MainWindow)
        self.setupQSS()
        self.label_calendar: list[list[QLabel]] = [[eval("self.label_{}_{}".format(x, y),
                                                         {"self": self}) for y in range(7)] for x in range(6)]
        date = datetime.datetime.now()
        self.month_edit.setValue(date.month)
        self.year_edit.setValue(date.year)

    def setupQSS(self):
        """
        初始化QSS

        :return: None
        """

    def widget_connect(self):
        """
        进行槽和信号的链接

        :return: None
        """

        def f_month_change(month: int):
            """
            临时函数

            :param month: 月
            :return: None
            """
            if month == 0:
                self.month_edit.setValue(12)
                self.year_edit.setValue(self.get_year() - 1)
            elif month == 13:
                self.month_edit.setValue(1)
                self.year_edit.setValue(self.get_year() + 1)
            else:
                self.month_edit.setValue(month)
                self.update_calendar()

        self.year_edit.valueChanged.connect(self.update_calendar)

        self.month_edit.valueChanged.connect(f_month_change)

        self.next_button.clicked.connect(lambda: self.month_edit.setValue(self.get_month() + 1))

        self.left_button.clicked.connect(lambda: self.month_edit.setValue(self.get_month() - 1))

    def update_calendar(self):
        """
        更新当前日历显示

        :return: None
        """

        weeks = 0
        flag = 0

        days = get_days(self.get_year(), self.get_month() - 1)
        weekday = get_datetime(self.get_year(), self.get_month() - 1, days).weekday()
        for i in range(days - weekday - 1, days):  # 上月日历
            flag += 1
            weekday = get_datetime(self.get_year(), self.get_month() - 1, i + 1).weekday()
            label = self.label_calendar[weeks][weekday]
            label.setNum(i + 1)
            label.setEnabled(False)
            label.setVisible(any([weekday == 3, not ONLY_SHOW_THURSDAY]))
            weeks += int(weekday == 6)

        days = get_days(self.get_year(), self.get_month())
        for i in range(days):  # 本月日历
            flag += 1
            weekday = datetime.datetime(self.get_year(), self.get_month(), i + 1).weekday()
            label = self.label_calendar[weeks][weekday]
            label.setNum(i + 1)
            label.setEnabled(True)
            label.setVisible(any([weekday == 3, not ONLY_SHOW_THURSDAY]))
            weeks += int(weekday == 6)

        for i in range(42 - flag):  # 下月日历
            weekday = get_datetime(self.get_year(), self.get_month() + 1, i + 1).weekday()
            label = self.label_calendar[weeks][weekday]
            label.setNum(i + 1)
            label.setEnabled(False)
            label.setVisible(any([weekday == 3, not ONLY_SHOW_THURSDAY]))
            weeks += int(weekday == 6)

    def get_year(self) -> int:
        """
        获取当前年份

        :return: 年
        """
        return self.year_edit.value()

    def get_month(self) -> int:
        """
        获取当前月份

        :return: 月
        """
        return self.month_edit.value()


def main():
    """
    主程序

    :return: None
    """
    plugin_path = r"C:\Users\王建华\AppData\Local\Programs\Python\Python310\Lib\site-packages\PySide2\plugins\platforms"
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path   # 添加系统变量

    app = QApplication(sys.argv)
    print(QStyleFactory.keys())
    app.setStyle(QStyleFactory.create('fusion'))
    print(QStyleFactory.mro()[1])
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    window = Calendar()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
