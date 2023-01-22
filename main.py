#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# 程序主入口
if __name__ == "__main__":
    """模仿浏览器，请求api信息"""

    # 1.引入 ActionChains 类
    from selenium.webdriver.common.action_chains import ActionChains
    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By



    address = [
        "https://ada.baidu.com/site/wjz9s9sb/xyl?imid=b3b028e65d4f5881554386c8a3393068?B?a1&bd_vid=nHD3nWn4P163Pj0dP1cznjDYrjPxnWcdg1wxnH0sg1wxPWnLrHbzn1DLPW0#back1665393576781",
        "https://ada.baidu.com/site/wjz9gbcv/xyl?imid=8cb27c8eea04a782eceda6b986b0694f#back1665393531949",
        "https://ada.baidu.com/site/wjz9s9sb/xyl?imid=b3b028e65d4f5881554386c8a3393068?B?a1&bd_vid=nHD3nWn4P163Pj0dP1cznjDYrjPxnWcdg1wxnH0sg1wxPWnLrHbzn1DLPW0#back1665393576781",
        "https://ada.baidu.com/site/wjzqlf20/xyl?imid=9a77260b6026231a457349a4f46bf074&source=baidu4&plan=4-Ayiyuanci【henan】&unit=henan&keyword=zhiliaoshenbingdezhuanyeyiyuan&e_adposition=cr1&e_keywordid=480876014216&bd_vid=nHD3nWn4P163Pj0dP1cznjDYrjPxnHfvnNtkg1Dsn7tYg1m1rHfYrHcdPWDv#back1665393598798",
        "https://ada.baidu.com/site/youhaogb.com/xyl?imid=34e8648782603147abd22d63f35fef50&bd_YH04_A_PP01_[PP]_11905&adaextra=eyJ2aWRlb19pZCI6IjEzMDI3MTk2NCJ9&bd_vid=nHfsnHmkrjmvP10znHb4PHnzP1PxnHfvnNtkg1Dsn7tYg1RdnWnvPjDvnHfL#back1665393837765",
        "https://ada.baidu.com/site/wjzte3v0/xyl?imid=d4a1f5777c07a100699a8d4aee4cd66c&TGGG2-XL0-C-108472-!N&bd_vid=nHnvPWT1PjcYP1c3rjTkPH6kPWIxnWcdg17xnH0sg1wxPWcvPjn3PjR1Pjc#back1665393883897",
        "https://ada.baidu.com/site/bdpc.yyyfuke120.com/xyl?imid=abf71be9e8ef8e13588265ce70864667&yyyjy2&shz&zigongjixian&L.1&bd_vid=nHmvn1bkrjb4PH0zPWbzrHR4Pj7xnWcdg17xnH0sg1wxPWfvPH61PjczP1c#back1665394121326",

        #
        # "https://group-live2.easyliao.com/live/chat.do?c=30989&g=33515&config=53325&ref=39yyk",
        # "https://sjh.baidu.com/site/zzeyeyy.com/f418b1dd-01a6-4d8d-b277-24383423105d?BD_ZZ_PPC&fid=nHcYnHnznj63nH6YnjbzP1c4PjPxnWcdg1D&ch=4&bd_vid=nHcYnHnznj63nH6YnjbzP1c4PjPxnWcdg17xnH0sg1wxnHc4PWDkPWD4rHf&ch=4&bd_bxst=EiaKUOmZ02XHw21900DD0ABfg6anZxcK0000001RqIZ41rZFOToHspm0000000000006nHf4PHTdfR77wjDvPHmkfHTLrj9Kwj-Knbu7njf3PHBB1r00-YE4Af000002C3_D0s000QydjutK0000j60000ofs_oHEXxwveOA7IjazVrq4qZUEtmVzn5DSoWtES1Qvf00rZDZv0&sdclkid=b52pALqD152NAJDGb-&bd_vid=10927831708070921180"
        ]

    for item in address:
        # 1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
        driver = webdriver.Chrome()

        print("启动浏览器，打开Web界面")
        # driver.get("https://www.baidu.com")
        js = "window.open('" + item +"')"
        driver.execute_script(js)

        handles = driver.window_handles
        driver.switch_to.window(handles[-1])

        # time.sleep(3)
        driver.find_element(By.CLASS_NAME, 'pc-icon-leave-tel').click()
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, 'leavetel-input').send_keys('phone')
        time.sleep(3)
        # driver.find_element(By.CLASS_NAME, 'submit-disabled').click()
        driver.find_element(By.CLASS_NAME, 'leavetel-callback').click()


        time.sleep(1)
        driver.quit()
        # driver.close()




