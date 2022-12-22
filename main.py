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


def get_future(today: datetime.datetime) -> int:
    """
    距下一个疯狂星期四

    :param today: 本日日期
    :return: 距离
    """
    days = 6 - today.weekday() + 4
    return days if days < 7 else 3 - today.weekday()


def get_past(today: datetime.datetime) -> int:
    """
    距上一个疯狂星期四

    :param today: 本日日期
    :return: 距离
    """
    days = today.weekday() + 3 if today.weekday() + 3 < 7 else today.weekday() - 3
    return days if days != 6 else 0


class Calendar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.widget_connect()
        self.update_calendar()  # 初始化日历
        self.set_future_past()

    def setupUi(self, MainWindow: QMainWindow):
        super().setupUi(MainWindow)
        self.setupQSS()
        self.label_calendar: list[list[QPushButton]] = [[eval("self.date_button_{}_{}".format(x, y),
                                                              {"self": self}) for y in range(7)] for x in range(6)]
        self.local_time = datetime.datetime.today()
        self.label_nowtime.setText(self.now_time.strftime("公元%Y年 %m月%d日 星期%w %H:%M:%S"))
        self.timer_update_local_time = QTimer(self)
        today = datetime.datetime.now()
        self.month_edit.setValue(today.month)
        self.year_edit.setValue(today.year)

        self.timer_update_local_time.timeout.connect(self.update_local_time)
        self.timer_update_local_time.start(250)

        self.get_date_button(self.local_time).setFocus()  # 使本日获得焦点

    @property
    def now_time(self):
        """
        返回当前时间

        :return: 返回当前时间
        """
        return datetime.datetime.today()

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
            if month == 0 and self.get_year() > 1:
                self.month_edit.setValue(12)
                self.year_edit.setValue(self.get_year() - 1)
            elif month == 13 and self.get_year() < 9999:
                self.month_edit.setValue(1)
                self.year_edit.setValue(self.get_year() + 1)
            else:
                self.month_edit.setValue(month)
                self.update_calendar()

        def f_go_back_today():
            """
            临时函数，回到今天

            :return: None
            """
            self.year_edit.setValue(self.now_time.year)
            self.month_edit.setValue(self.now_time.month)
            self.update_calendar()
            self.get_date_button(self.local_time).setFocus()

        def mouseDoubleClickEvent(_: QMouseEvent):
            """
            临时函数，双击

            :param _: 事件
            :return: None
            """
            focus_button = self.get_focus_button()
            if not focus_button.property("toMonth") and focus_button.text() != "":
                [self.left_button, self.next_button][int(focus_button.text()) <= 15].click()

        self.year_edit.valueChanged.connect(self.update_calendar)

        self.month_edit.valueChanged.connect(f_month_change)

        self.next_button.clicked.connect(lambda: self.month_edit.setValue(self.get_month() + 1))

        self.left_button.clicked.connect(lambda: self.month_edit.setValue(self.get_month() - 1))

        self.goback_button.clicked.connect(f_go_back_today)

        for x in range(6):
            for y in range(7):
                self.label_calendar[x][y].mouseDoubleClickEvent = mouseDoubleClickEvent

    def update_calendar(self):
        """
        更新当前日历显示

        :return: None
        """
        weeks = 0
        flag = 0

        self.reset_focus()

        days = get_days(self.get_year(), self.get_month() - 1)
        weekday = get_datetime(self.get_year(), self.get_month() - 1, days).weekday()
        for i in range(days - weekday - 1, days):  # 上月日历
            flag += 1
            weekday = get_datetime(self.get_year(), self.get_month() - 1, i + 1).weekday()
            button = self.label_calendar[weeks][weekday]
            button.setText(["", str(i + 1)][any([weekday == 3, not ONLY_SHOW_THURSDAY])])
            button.setProperty("toMonth", False)
            button.setProperty("Month", get_datetime(self.get_year(), self.get_month() - 1, 1).month)
            button.setProperty("Year", get_datetime(self.get_year(), self.get_month() - 1, 1).year)
            button.setStyleSheet(button.styleSheet())  # 更改自定义变量后需重设style sheet
            weeks += int(weekday == 6)

        days = get_days(self.get_year(), self.get_month())
        for i in range(days):  # 本月日历
            flag += 1
            weekday = datetime.datetime(self.get_year(), self.get_month(), i + 1).weekday()
            button = self.label_calendar[weeks][weekday]
            button.setText(["", str(i + 1)][any([weekday == 3, not ONLY_SHOW_THURSDAY])])
            button.setProperty("toMonth", True)
            button.setProperty("Month", get_datetime(self.get_year(), self.get_month() + 1, 1).month)
            button.setProperty("Year", get_datetime(self.get_year(), self.get_month() + 1, 1).year)
            button.setProperty("toDay",
                               datetime.datetime(self.get_year(),
                                                 self.get_month(), i + 1).date() == datetime.datetime.today().date())
            button.setStyleSheet(button.styleSheet())  # 更改自定义变量后需重设style sheet
            weeks += int(weekday == 6)

        for i in range(42 - flag):  # 下月日历
            weekday = get_datetime(self.get_year(), self.get_month() + 1, i + 1).weekday()
            button = self.label_calendar[weeks][weekday]
            button.setText(["", str(i + 1)][any([weekday == 3, not ONLY_SHOW_THURSDAY])])
            button.setProperty("toMonth", False)
            button.setProperty("Month", get_datetime(self.get_year(), self.get_month() + 1, 1).month)
            button.setProperty("Year", get_datetime(self.get_year(), self.get_month() + 1, 1).year)
            button.setStyleSheet(button.styleSheet())  # 更改自定义变量后需重设style sheet
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

    def update_local_time(self):
        """
        更新当前时间

        :return: None
        """

        if self.local_time != self.now_time:
            self.label_nowtime.setText(self.now_time.strftime("公元%Y年 %m月%d日 星期%w %H:%M:%S"))
            if self.local_time.date() != self.now_time.date():
                self.update_calendar()
                self.set_future_past()

            self.local_time = self.now_time

    def set_future_past(self):
        """
        设置过去和未来

        :return: None
        """
        if self.now_time.weekday() != 3:
            self.label_future.setText(f"展望未来：还有{get_future(self.now_time)}天到下一个疯狂星期四")
            self.label_past.setText(f"回首过去：距离上个疯狂星期四已经过了{get_past(self.now_time)}天")
        else:
            self.label_past.setText("回首过去：逝者如斯夫，要珍惜当下")
            self.label_future.setText("展望未来：未来仍然遥远，要把握今朝")

    def get_index(self,
                  date: datetime.datetime = None,
                  year: int = None,
                  month: int = None,
                  day: int = None,
                  toMonth: bool = True) -> tuple[int, int]:
        """
        获取某日在日历里的索引号

        :param toMonth: 是否为本月
        :param year: 年
        :param month: 月
        :param day: 日
        :param date: 日期
        :return: 索引号
        """
        if date:
            first_day = datetime.datetime(date.year, date.month, 1)  # 某月一日
        else:
            first_day = datetime.datetime(year, month, 1)  # 某月一日
            date = datetime.datetime(year, month, day)

        return (first_day.weekday() + date.day) // 7, date.weekday()

    def get_date_button(self,
                        date: datetime.datetime | None = None,
                        year: int = 0,
                        month: int = 0,
                        day: int = 0,
                        toMonth: bool = True) -> QPushButton:
        """
        获取某日在日历里的实例（上个月的也能）

        :param toMonth: 是否本月
        :param year: 年
        :param month: 月
        :param day: 日
        :param date: 日期
        :return: 按钮
        """
        if not date:
            date = get_datetime(year, month, day)
        first_day = get_datetime(date.year, date.month - int(not toMonth), 1)  # 某月一日
        days = (first_day.weekday() + get_days(get_datetime(date.year, date.month - 1, 1).year,
                                               get_datetime(date.year, date.month - 1, 1).month) * int(not toMonth)
                + date.day - 1) // 7 + int(first_day.weekday() == 0) if date.day <= 15 or toMonth else 0
        return self.label_calendar[days][date.weekday()]

    def get_focus_button(self) -> QPushButton:
        """
        焦点按钮

        :return: 焦点按钮
        """
        return ([item for sub in list(map(lambda j: list(filter(lambda but: but.hasFocus(),
                                                                self.label_calendar[j])),
                                          range(6))) for item in sub] + [
                    self.get_date_button(self.local_time)])[0]

    def reset_focus(self):
        """
        重设焦点

        :return: None
        """

        focus_button = self.get_focus_button()

        # 重设焦点
        if focus_button.text() == "0" or focus_button.text() == "" or \
                self.get_date_button(year=self.get_year(), month=self.get_month(),
                                     day=int(focus_button.text())).text() == "":
            return
        if (focus_button.property("toMonth") or
                int(focus_button.text()) <= 15 or
                self.get_date_button(year=self.get_year(),
                                     month=self.get_month(),
                                     day=int(focus_button.text()),
                                     toMonth=False) == focus_button):
            if int(focus_button.text()) <= get_days(self.get_year(), self.get_month()):
                self.get_date_button(year=self.get_year(),
                                     month=self.get_month(),
                                     day=int(focus_button.text())).setFocus()
            else:
                self.get_date_button(year=self.get_year(),
                                     month=self.get_month(),
                                     day=get_days(self.get_year(), self.get_month())).setFocus()
        else:
            self.get_date_button(year=self.get_year(),
                                 month=self.get_month(),
                                 day=1).setFocus()


def main():
    """
    主程序

    :return: None
    """
    plugin_path = r"C:\Users\王建华\AppData\Local\Programs\Python\Python310\Lib\site-packages\PySide2\plugins\platforms"
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path  # 添加系统变量

    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('fusion'))
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    window = Calendar()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
