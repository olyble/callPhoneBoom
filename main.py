#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import ast

def boom(phone):
    """模仿浏览器，请求api信息"""

    # 1.引入 ActionChains 类
    from selenium.webdriver.common.action_chains import ActionChains
    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options

    address = []
    with open('api.txt', 'r') as file:
        urls = file.readlines()
        # 计算链接地址条数
        n_urls = len(urls)

    # 遍历链接地址
    for i, url in enumerate(urls):
        try:
            # 1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
            # 无头模式(开启请删掉下面三行注释，然后注释原来的)
            # chrome_options = Options()
            # chrome_options.add_argument('--headless')
            # driver = webdriver.Chrome(chrome_options=chrome_options)
            driver = webdriver.Chrome()

            print("启动浏览器，打开Web界面")
            driver.get(url)
            # js = "window.open('" + url + "')"
            # driver.execute_script(js)

            handles = driver.window_handles
            driver.switch_to.window(handles[-1])

            # time.sleep(3)
            driver.find_element(By.CLASS_NAME, 'pc-icon-leave-tel').click()
            time.sleep(3)
            driver.find_element(By.CLASS_NAME, 'leavetel-input').send_keys(phone)
            time.sleep(3)
            # driver.find_element(By.CLASS_NAME, 'submit-disabled').click()
            driver.find_element(By.CLASS_NAME, 'leavetel-callback').click()

            time.sleep(1)
            driver.quit()
            # driver.close()
        except Exception as exc:
            print(exc)  # 如果需要打印出故障原因可以使用本行代码

# 程序主入口
if __name__ == "__main__":
    boom("phone")
