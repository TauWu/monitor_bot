# -*- coding: utf-8 -*-
# 定时任务模块封装

import time
import sched
from date import Time

# 待测函数
def foo(msg, starttime):
    print(Time.now_str(), msg, starttime)

def sched_foo():
    s = sched.scheduler(time.time, time.sleep)
    s.enter(1, 1, foo, ("测试1", Time.now_str()))
    s.enter(3, 1, foo, ("测试2", Time.now_str()))
    s.run()

def sched_foo_loop():
    s = sched.scheduler(time.time, time.sleep)
    s.enter(4, 1, sched_foo, ())
    s.enter(5, 1, sched_foo, ())
    s.run()

if __name__ == "__main__":
    sched_foo_loop()