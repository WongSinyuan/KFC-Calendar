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
import datetime
import json
import os
import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_calendar import Ui_MainWindow

crazyDay: int = 3
"""你的疯狂星期四，又何必是星期四？（0 表示星期一，6 表示星期天）"""
onlyShowCrazyDay: bool = True
"""是否只显示疯狂星期四"""
weekFirstDay: int = 0
"""每周的第一天（0 表示星期一，6 表示星期天）"""
weekStyleIndex: int = 0
"""星期样式（0 表示星期X， 1表示周X）"""

weekStyle: tuple[list[str]] = (["星期" + k for k in ["一", "二", "三", "四", "五", "六", "天"]],
                               ["星期" + k for k in ["壹", "贰", "叁", "肆", "伍", "陆", "天"]],
                               ["星期" + k for k in ["一", "二", "三", "四", "五", "六", "日"]],
                               ["星期" + k for k in ["壹", "贰", "叁", "肆", "伍", "陆", "日"]],
                               ["星期" + k for k in ["一", "二", "三", "四", "五", "六", "七"]],
                               ["星期" + k for k in ["壹", "贰", "叁", "肆", "伍", "陆", "柒"]],
                               ["周" + k for k in ["一", "二", "三", "四", "五", "六", "日"]],
                               ["周" + k for k in ["壹", "贰", "叁", "肆", "伍", "陆", "日"]],
                               ["周" + k for k in ["一", "二", "三", "四", "五", "六", "天"]],
                               ["周" + k for k in ["壹", "贰", "叁", "肆", "伍", "陆", "天"]],
                               ["周" + k for k in ["一", "二", "三", "四", "五", "六", "七"]],
                               ["周" + k for k in ["壹", "贰", "叁", "肆", "伍", "陆", "柒"]],
                               ["一", "二", "三", "四", "五", "六", "日"],
                               ["壹", "贰", "叁", "肆", "伍", "陆", "日"],
                               ["一", "二", "三", "四", "五", "六", "天"],
                               ["壹", "贰", "叁", "肆", "伍", "陆", "天"],
                               ["一", "二", "三", "四", "五", "六", "七"],
                               ["壹", "贰", "叁", "肆", "伍", "陆", "柒"],
                               ["1", "2", "3", "4", "5", "6", "7"],
                               ["Mon.", "Tue.", "Wed.", "Thur.", "Fri.", "Sat.", "Sun."],
                               ["Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ", "Ⅴ", "Ⅵ", "Ⅶ"])


def getDays(date: datetime.datetime | None = None,
            year: int = 0,
            month: int = 0) -> int:
    """
    获取指定月份的天数

    :param date: 日期
    :param year: 年
    :param month: 月
    :return: 天数
    """
    year, month = (date.year, date.month) if date else (year, month)
    if 0 < month < 12:
        return (datetime.datetime(year, month + 1, 1) - datetime.datetime(year, month, 1)).days
    elif month == 0:
        return (datetime.datetime(year, 1, 1) - datetime.datetime(year - 1, 12, 1)).days
    else:
        return (datetime.datetime(year + 1, 1, 1) - datetime.datetime(year, 12, 1)).days


def getDateTime(year: int, month: int, day: int) -> datetime.datetime:
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

    if day > getDays(year=year, month=month):
        day = 1
        month += 1
    elif day < 1:
        day = getDays(year=year, month=month - 1)
        month -= 1

    if month == 13:
        month = 1
        year += 1
    elif month == 0:
        month = 12
        year -= 1

    return datetime.datetime(year, month, day)


def getFuture(today: datetime.datetime) -> int:
    """
    距下一个疯狂星期四

    :param today: 本日日期
    :return: 距离
    """
    days = 6 - today.weekday() + crazyDay + 1
    return days if days < 7 else crazyDay - today.weekday()


def getPast(today: datetime.datetime) -> int:
    """
    距上一个疯狂星期四

    :param today: 本日日期
    :return: 距离
    """
    days = today.weekday() + 6 - crazyDay if today.weekday() - crazyDay < 1 else today.weekday() - crazyDay
    return days if days != 6 else 0


def getIndexFromDate(date: datetime.datetime = None,
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
    date = date if date else getDateTime(year, month, day)
    first_day = getDateTime(date.year, date.month - (not toMonth), 1)  # 某月一日
    days = ((list(range(7))[first_day.weekday() - weekFirstDay] + date.day - 1
             + (not toMonth) * getDays(date=getDateTime(date.year, date.month - 1, date.day))) // 7
            + (list(range(7))[first_day.weekday() - weekFirstDay] == 0) * (weekFirstDay == 0)
            if toMonth or date.day <= 15 else 0)
    return days, date.weekday() - weekFirstDay


def QDateToDateTime(date: QDate) -> datetime.datetime:
    """
    将QDate转化为datetime

    :param date: 日期
    :return: 对应的日期
    """
    return datetime.datetime(date.year(), date.month(), date.day())


def DateTimeToQDate(date: datetime.datetime) -> QDate:
    """
    将datetime转化为QDate

    :param date: 日期
    :return: 对应的日期
    """
    return QDate(date.year, date.month, date.day)


class Calendar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connectWidget()
        self.updateCalender()  # 初始化日历
        self.setFuturePast()

    def setupUi(self, MainWindow: QMainWindow):
        super().setupUi(MainWindow)
        self.setupQSS()
        self.label_calendar: list[list[QPushButton]] = [[eval("self.date_button_{}_{}".format(x, y),
                                                              {"self": self}) for y in range(7)] for x in range(6)]
        self.label_week: list[QLabel] = [eval("self.week_{}".format(i), {'self': self}) for i in range(7)]
        self.local_time = datetime.datetime.today()
        self.dateEdit_label = {
            self.date_delta_beginning_setter: self.date_delta_beginning_crazyDay_label,
            self.date_delta_ending_setter: self.date_delta_ending_crazyDay_label,
            self.date_add_sub_begining_setter: self.date_add_sub_begining_crazyDay_label,
            self.date_add_sub_ending_shower: self.date_add_sub_ending_crazyDay_label,
            self.crazyDay_beginning_setter: self.crazyDay_beginning_crazyDay_label,
            self.crazyDay_ending_setter: self.crazyDay_ending_crazyDay_label,
        }
        self.label_nowtime.setText(
            self.now_time.strftime(
                "公元%Y年 %m月%d日 {} %H:%M:%S".format(weekStyle[weekStyleIndex][self.now_time.weekday()])
            )
        )
        self.timer_update_local_time = QTimer(self)
        today = datetime.datetime.now()
        self.month_edit.setValue(today.month)
        self.year_edit.setValue(today.year)

        self.timer_update_local_time.timeout.connect(self.updateLocalTime)
        self.timer_update_local_time.start(250)

        self.getButtonFromDate(self.local_time).setFocus()  # 使本日获得焦点

        self.main_widget.setCurrentIndex(0)

        self.date_delta_beginning_setter.setDate(DateTimeToQDate(self.local_time))
        self.date_delta_beginning_setter.setMaximumDate(DateTimeToQDate(self.local_time))
        self.date_delta_ending_setter.setDate(DateTimeToQDate(self.local_time))
        self.date_delta_ending_setter.setMinimumDate(DateTimeToQDate(self.local_time))
        self.calculateDateDelta()

        self.date_add_sub_begining_setter.setDate(DateTimeToQDate(self.local_time))
        self.date_add_sub_delta_day_setter.setValue(0)
        self.calculateAddSurDate()

        self.crazyDay_beginning_setter.setDate(DateTimeToQDate(self.local_time))
        self.crazyDay_beginning_setter.setMaximumDate(DateTimeToQDate(self.local_time))
        self.crazyDay_ending_setter.setDate(DateTimeToQDate(self.local_time))
        self.crazyDay_ending_setter.setMinimumDate(DateTimeToQDate(self.local_time))
        self.calculateCrazyDay()

    def setupQSS(self):
        """
        初始化QSS

        :return: None
        """
        self.tab_calculte_scrollArea.widget().setStyleSheet("background-color: rgb(249, 249, 249)")

    @property
    def now_time(self):
        """
        返回当前时间

        :return: 返回当前时间
        """
        return datetime.datetime.today()

    def connectWidget(self):
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
                self.updateCalender()

        def f_go_back_today():
            """
            临时函数，回到今天

            :return: None
            """
            self.year_edit.setValue(self.now_time.year)
            self.month_edit.setValue(self.now_time.month)
            self.updateCalender()
            self.getButtonFromDate(self.local_time).setFocus()

        def date_button_mouseDoubleClickEvent(_: QMouseEvent):
            """
            临时函数，按钮双击

            :param _: 事件
            :return: None
            """
            focus_button = self.getFocusButton()
            if not focus_button.property("toMonth") and focus_button.text() != "":
                [self.left_button, self.next_button][int(focus_button.text()) <= 15].click()

        def calendar_wheelEvent(event: QWheelEvent):
            """
            临时函数，日历滚动事件

            :param event: 事件
            :return: None
            """
            [self.left_button, self.next_button][event.angleDelta().toTuple()[1] < 0].click()

        self.year_edit.valueChanged.connect(self.updateCalender)

        self.month_edit.valueChanged.connect(f_month_change)

        self.next_button.clicked.connect(lambda: self.month_edit.setValue(self.get_month() + 1))

        self.left_button.clicked.connect(lambda: self.month_edit.setValue(self.get_month() - 1))

        self.goback_button.clicked.connect(f_go_back_today)

        for x, y in [(i, j) for i in range(6) for j in range(7)]:
            self.label_calendar[x][y].mouseDoubleClickEvent = date_button_mouseDoubleClickEvent

        self.calendar.wheelEvent = calendar_wheelEvent

        self.weekStyle_setter.currentIndexChanged.connect(self.setWeekStyle)

        self.onlyShowCrazyDay_setter.clicked.connect(self.setOnlyShowCrazyDay)

        self.crazyDay_setter.currentIndexChanged.connect(self.setCrazyDay)

        self.weekFirstDay_setter.currentIndexChanged.connect(self.setWeekFirstDay)

        self.date_delta_beginning_setter.dateChanged.connect(self.calculateDateDelta)
        self.date_delta_ending_setter.dateChanged.connect(self.calculateDateDelta)

        self.date_add_sub_begining_setter.dateChanged.connect(self.calculateAddSurDate)
        self.date_add_sub_delta_day_setter.valueChanged.connect(self.calculateAddSurDate)

        self.crazyDay_beginning_setter.dateChanged.connect(self.calculateCrazyDay)
        self.crazyDay_ending_setter.dateChanged.connect(self.calculateCrazyDay)

    def updateLocalTime(self):
        """
        更新当前时间

        :return: None
        """

        if self.local_time != self.now_time:
            self.label_nowtime.setText(
                self.now_time.strftime(
                    "公元%Y年 %m月%d日 {} %H:%M:%S".format(weekStyle[weekStyleIndex][self.now_time.weekday()])
                )
            )
            if self.local_time.date() != self.now_time.date():
                self.updateCalender()
                self.setFuturePast()

            self.local_time = self.now_time

    def updateCalender(self):
        """
        更新当前日历显示

        :return: None
        """
        weeks = 0
        flag = 0

        self.updateWeekStyle()
        self.resetFocus()

        # 上月日历
        days = getDays(year=self.get_year(), month=self.get_month() - 1)
        weekday = getDateTime(self.get_year(), self.get_month() - 1, days).weekday()
        _f = days - weekday - 1 + (weekFirstDay if weekday + 1 >= weekFirstDay else (weekFirstDay - 7))
        for i in range(_f, days):
            flag += 1
            weekday = getDateTime(self.get_year(), self.get_month() - 1, i + 1).weekday()
            button = self.label_calendar[weeks][weekday - weekFirstDay]
            button.setText(["", str(i + 1)][any([weekday == crazyDay, not onlyShowCrazyDay])])
            button.setProperty("toMonth", False)
            button.setProperty("Month", getDateTime(self.get_year(), self.get_month() - 1, 1).month)
            button.setProperty("Year", getDateTime(self.get_year(), self.get_month() - 1, 1).year)

            button.setStyleSheet(button.styleSheet())

            weeks += int(weekday == (6 if weekFirstDay == 0 else weekFirstDay - 1))

        # 本月日历
        days = getDays(year=self.get_year(), month=self.get_month())
        for i in range(days):
            flag += 1
            weekday = datetime.datetime(self.get_year(), self.get_month(), i + 1).weekday()
            button = self.label_calendar[weeks][weekday - weekFirstDay]
            button.setText(["", str(i + 1)][any([weekday == crazyDay, not onlyShowCrazyDay])])
            button.setProperty("toMonth", True)
            button.setProperty("Month", getDateTime(self.get_year(), self.get_month() + 1, 1).month)
            button.setProperty("Year", getDateTime(self.get_year(), self.get_month() + 1, 1).year)
            button.setProperty("toDay",
                               datetime.datetime(self.get_year(),
                                                 self.get_month(), i + 1).date() == datetime.datetime.today().date())

            button.setStyleSheet(button.styleSheet())

            weeks += int(weekday == (6 if weekFirstDay == 0 else weekFirstDay - 1))

        # 下月日历
        for i in range(42 - flag):
            weekday = getDateTime(self.get_year(), self.get_month() + 1, i + 1).weekday()
            button = self.label_calendar[weeks][weekday - weekFirstDay]
            button.setText(["", str(i + 1)][any([weekday == crazyDay, not onlyShowCrazyDay])])
            button.setProperty("toMonth", False)
            button.setProperty("Month", getDateTime(self.get_year(), self.get_month() + 1, 1).month)
            button.setProperty("Year", getDateTime(self.get_year(), self.get_month() + 1, 1).year)
            button.setStyleSheet(button.styleSheet())
            weeks += int(weekday == (6 if weekFirstDay == 0 else weekFirstDay - 1))

    def updateWeekStyle(self):
        """
        更新星期显示

        :return:
        """
        self.setFuturePast()
        self.updateDateEditTip()
        self.weekFirstDay_setter_label.setText(
            json.load(open("data/weekFirstDay_setter_label_text.json", encoding="utf-8"))[weekStyleIndex])
        self.crazyDay_setter_label.setText(
            json.load(open("data/crazyDay_setter_label_text.json", encoding="utf-8"))[weekStyleIndex])
        self.onlyShowCrazyDay_setter_label.setText(
            json.load(
                open("data/onlyShowCrazyDay_setter_label_text.json", encoding="utf-8")
            )[weekStyleIndex].format(weekStyle[weekStyleIndex][crazyDay]))
        self.weekStyle_setter_label.setText(
            json.load(open("data/weekStyle_setter_label_text.json", encoding="utf-8"))[weekStyleIndex])
        self.crazyDay_result_label.setText("疯狂{}天数".format(weekStyle[weekStyleIndex][crazyDay]))
        self.crazyDay_title_label.setText("日期之间的疯狂{}".format(weekStyle[weekStyleIndex][crazyDay]))
        for i in range(7):
            label = self.label_week[i - weekFirstDay]
            label.setText(weekStyle[weekStyleIndex][i])
            label.setProperty("isWeekEnd", i == 5 or i == 6)
            label.setStyleSheet(label.styleSheet())
            self.weekFirstDay_setter.setItemText(i, weekStyle[weekStyleIndex][i])
            self.crazyDay_setter.setItemText(i, weekStyle[weekStyleIndex][i])

    def updateDateEditTip(self):
        """
        更新dateEdit旁边的小提示

        :return: None
        """
        for edit, label in zip(self.dateEdit_label.keys(), self.dateEdit_label.values()):
            label.setText("这天是疯狂{}！！".format(weekStyle[weekStyleIndex][crazyDay]))
            label.setVisible(QDateToDateTime(edit.date()).weekday() == crazyDay)

    def calculateDateDelta(self):
        """
        计算时间差值，并更新显示

        :return: None
        """

        date1 = QDateToDateTime(self.date_delta_beginning_setter.date())
        date2 = QDateToDateTime(self.date_delta_ending_setter.date())
        self.date_delta_beginning_setter.setMaximumDate(self.date_delta_ending_setter.date())
        self.date_delta_ending_setter.setMinimumDate(self.date_delta_beginning_setter.date())
        delta = date2 - date1
        self.date_delta_result_shower.setValue(delta.days)
        self.updateDateEditTip()

    def calculateAddSurDate(self):
        """
        计算增减天数后的日期，并更新显示

        :return: None
        """
        date1 = self.date_add_sub_begining_setter.date()
        days = self.date_add_sub_delta_day_setter.value()
        date2 = date1.addDays(days)
        self.date_add_sub_ending_shower.setDate(date2)
        self.updateDateEditTip()

    def calculateCrazyDay(self):
        """
        计算日期之间有多少疯狂日，并更新显示

        :return: None
        """
        date1 = QDateToDateTime(self.crazyDay_beginning_setter.date())
        self.crazyDay_ending_setter.setMinimumDate(self.crazyDay_beginning_setter.date())
        date2 = QDateToDateTime(self.crazyDay_ending_setter.date())
        self.crazyDay_beginning_setter.setMaximumDate(self.crazyDay_ending_setter.date())

        days = (date2 - date1).days - (6 - date1.weekday()) - date2.weekday() - 1
        nums = days // 7 + int(date1.weekday() <= crazyDay) + int(date2.weekday() >= crazyDay)
        self.crazyDay_result_shower.setValue(nums)
        self.updateDateEditTip()

    def setFuturePast(self):
        """
        设置过去和未来

        :return: None
        """
        if self.now_time.weekday() != crazyDay:
            self.label_future.setText(
                f"展望未来：还有{getFuture(self.now_time)}天到下一个疯狂{weekStyle[weekStyleIndex][crazyDay]}")
            self.label_past.setText(
                f"回首过去：距离上个疯狂{weekStyle[weekStyleIndex][crazyDay]}已经过了{getPast(self.now_time)}天")
        else:
            self.label_past.setText("回首过去：逝者如斯夫，要珍惜当下")
            self.label_future.setText("展望未来：未来仍然遥远，要把握今朝")

    def setWeekFirstDay(self, value: int):
        """
        设置星期的第一天

        :param value: 值（0<=value<=6）
        :return: None
        """
        global weekFirstDay
        if 0 <= value <= 6:
            weekFirstDay = value
            self.updateCalender()
        else:
            raise ValueError("应在区间[0, 6]内")

    def setOnlyShowCrazyDay(self, value: bool):
        """
        设置是否只显示疯狂星期四

        :param value: 值（0<=value<=6）
        :return: None
        """
        global onlyShowCrazyDay
        if type(value) == bool:
            onlyShowCrazyDay = value
            self.updateCalender()

    def setCrazyDay(self, value: int):
        """
        设置疯狂日

        :param value: 值（0<=value<=6）
        :return: None
        """
        global crazyDay
        if 0 <= value <= 6:
            crazyDay = value
            self.updateCalender()
            self.calculateCrazyDay()
            self.updateDateEditTip()
            self.setFuturePast()
        else:
            raise ValueError("应在区间[0, 6]内")

    def setWeekStyle(self, value: int):
        """
        设置星期样式

        :param value: 值（0<=value<=1）
        :return: None
        """
        global weekStyleIndex
        if 0 <= value <= len(weekStyle):
            weekStyleIndex = value
            self.updateCalender()
        else:
            raise ValueError("应在之间[0, {}]之间".format(len(weekStyle)))

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

    def getButtonFromDate(self,
                          date: datetime.datetime | None = None,
                          year: int = 0,
                          month: int = 0,
                          day: int = 0,
                          toMonth: bool = True) -> QPushButton:
        """
        获取某日在日历里的实例

        :param toMonth: 是否本月
        :param year: 年
        :param month: 月
        :param day: 日
        :param date: 日期
        :return: 按钮
        """
        date = date if date else getDateTime(year, month, day)
        first_day = getDateTime(date.year, date.month - (not toMonth), 1)  # 某月一日
        days = ((list(range(7))[first_day.weekday() - weekFirstDay] + date.day - 1
                 + (not toMonth) * getDays(date=getDateTime(date.year, date.month - 1, date.day))) // 7
                + (list(range(7))[first_day.weekday() - weekFirstDay] == 0) * (weekFirstDay == 0)
                if toMonth or date.day <= 15 else 0)
        return self.label_calendar[days][date.weekday() - weekFirstDay]

    def getFocusButton(self) -> QPushButton:
        """
        焦点按钮

        :return: 焦点按钮
        """
        return ([item for sub in list(map(lambda j: list(filter(lambda but: but.hasFocus(),
                                                                self.label_calendar[j])),
                                          range(6))) for item in sub] + [
                    self.getButtonFromDate(self.local_time)])[0]

    def resetFocus(self):
        """
        重设焦点

        :return: None
        """

        focus_button = self.getFocusButton()

        # 重设焦点
        if focus_button.text() == "0" or focus_button.text() == "" or \
                self.getButtonFromDate(year=self.get_year(), month=self.get_month(),
                                       day=int(focus_button.text())).text() == "":
            return
        if (focus_button.property("toMonth") or
                int(focus_button.text()) <= 15 or
                self.getButtonFromDate(year=self.get_year(), month=self.get_month(), day=int(focus_button.text()),
                                       toMonth=False) == focus_button):
            if int(focus_button.text()) <= getDays(year=self.get_year(), month=self.get_month()):
                self.getButtonFromDate(year=self.get_year(), month=self.get_month(),
                                       day=int(focus_button.text())).setFocus()
            else:
                self.getButtonFromDate(year=self.get_year(), month=self.get_month(),
                                       day=getDays(year=self.get_year(), month=self.get_month())).setFocus()
        else:
            self.getButtonFromDate(year=self.get_year(), month=self.get_month(), day=1).setFocus()


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
