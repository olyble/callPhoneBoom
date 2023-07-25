#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By


def visit_website(url, i, queue,phone):
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com/")
        driver.get(url)

        try:
            # 等待弹窗出现并点击关闭按钮
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "imlp-component-captcha-close"))).click()
        except:
            # 如果弹窗没有出现，就什么都不做
            pass
        time.sleep(30)
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])

        # driver.find_element(By.CLASS_NAME, 'pc-icon-leave-tel').click()
        # time.sleep(3)
        # driver.find_element(By.CLASS_NAME, 'leavetel-input').send_keys(phone)
        # time.sleep(3)
        # driver.find_element(By.CLASS_NAME, 'leavetel-callback').click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.pc-icon-leave-tel'))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'leavetel-input'))).send_keys(phone)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'leavetel-callback'))).click()

        time.sleep(1)
        driver.quit()

        # 将执行结果添加到共享列表
        queue.put((i, True))

    except Exception as exc:
        # 如果发生错误，将执行结果添加到共享列表
        queue.put((i, False))


def boom(phone):
    """模仿浏览器，请求api信息"""
    with open('api.txt', 'r') as file:
        urls = file.readlines()
        # 计算链接地址条数
        n_urls = len(urls)

    processes = []
    queue = Queue()
    # 遍历链接地址
    for i, url in enumerate(urls):
        processes.append(Process(target=visit_website, args=(url.strip(), i, queue,phone)))
    # 启动所有线程
    for p in processes:
        p.start()

    # 等待所有线程结束
    for p in processes:
        p.join()
    n = 0
    while not queue.empty():
        i, j = queue.get()
        if j:
            n += 1
    print(f"一共成功：{n}/{n_urls}")


# 程序主入口
if __name__ == "__main__":
    # get_cookie()
    boom("phone1")
    boom("phone2")

