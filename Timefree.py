#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1.引入 ActionChains 类
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import schedule
import random
import os
os.environ['WDM_LOG'] = "false"
import main

def job():
    main.boom()


# 程序主入口
if __name__ == "__main__":
    print("正在运行定时任务中....")
    schedule.every().day.at("17:41").do(job)
    # number = random.randint(0, 2)
    # print(number)
    # if number == 0:
    #     schedule.every().day.at("9:30").do(job)
    #
    # if number == 1:
    #     schedule.every().day.at("13:30").do(job)
    #
    # if number == 2:
    #     schedule.every().day.at("15:30").do(job)

    # 每十分钟执行任务
    # schedule.every(1).minutes.do(job)
    # # 每个小时执行任务
    # schedule.every().hour.do(job)
    # # 每天的10:30执行任务
    # schedule.every().day.at("10:30").do(job)
    # # 每个月执行任务
    # schedule.every().monday.do(job)
    # # 每个星期三的13:15分执行任务
    # schedule.every().wednesday.at("13:15").do(job)
    # # 每分钟的第17秒执行任务
    # schedule.every().minute.at(":17").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
