# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

import time
# s_time = time.time()
#
# time.sleep(3)
#
# print(f"cost { time.time() - s_time}")

# print(time.localtime(1334444444444))
# print(time.gmtime())
#
# print(time.mktime( time.localtime()  ))
#
# print(time.strftime("%Y-%m-%d %H:%M:%S " ))  # 时间，转字符串
#
# time_str = time.strftime("%Y-%m-%d %H:%M:%S")
# print(time.strptime(time_str,"%Y-%m-%d %H:%M:%S"))



import datetime

d =datetime.datetime.now()
print(d.timetuple())
print(d + datetime.timedelta(-5,hours=5))

print(d.replace(year=2120, month=8))