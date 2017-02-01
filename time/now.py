#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# 显示时间
# 当前日期&时间&周几
# 当前日期
# 当前时间
# 当前周几
# 当前天数/年
# 当前周数

# author by star
import sys
from workflow import Workflow
from time import gmtime,strftime

ICON_DEFAULT = 'icon.png'
end = "[by star]"

def delZero(num):
    return num.replace("0","")

def showTime():
    now = gmtime()
    full = strftime("%Y-%m-%d %H:%M:%S %A",now)
    date = strftime("%Y-%m-%d",now)
    time = strftime("%H:%M:%S",now)
    day = strftime("%A",now)
    currentDay = delZero(strftime("%j",now))
    currentWeek = delZero(strftime("%U",now))
    wf.add_item(
        title=full,
        subtitle="time for now"+end,
        arg=u"" + full,
        valid=True,
        icon=ICON_DEFAULT)
    wf.add_item(
        title=u"当前日期"+ date,
        subtitle="time for date" + end,
        arg=u"" + date,
        valid=True,
        icon=ICON_DEFAULT)
    wf.add_item(
        title=u"当前时间"+ time,
        subtitle="time for time" + end,
        arg=u"" + time,
        valid=True,
        icon=ICON_DEFAULT)
    wf.add_item(
        title=u"today is "+ day,
        subtitle="time for today" + end,
        arg=u"" + day,
        valid=True,
        icon=ICON_DEFAULT)
    wf.add_item(
        title=u"今天是一年中的第["+ currentDay +"]天".decode("utf-8"),
        subtitle="time for day" + end,
        arg=u"" + currentDay,
        valid=True,
        icon=ICON_DEFAULT)
    wf.add_item(
        title=u"今天是一年中的第["+ currentWeek +"]周".decode("utf-8"),
        subtitle="time for now" + end,
        arg=u"" + currentWeek,
        valid=True,
        icon=ICON_DEFAULT)
    wf.send_feedback()

def main(wf):
    showTime()

if __name__ == u"__main__":
    update_settings = {'version': '1.0.0','github_slug':'star1989/alfred_workflow'}
    wf = Workflow(update_settings=update_settings)
    sys.exit(wf.run(main))