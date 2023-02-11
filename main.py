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
        
        # Contributed from tiaolaidage
        "https://ada.baidu.com/site/021bdf.com/xyl?imid=0df5cf5c8634012f7da6da8879c10124?bd-pc-nanke-127-zonghe-85038697968&bd_vid=nHnznHTsPHnsrHT4n1m4rjbkn1FxnWcdg17xnH0sg1wxnWD4PWT4PW0kPjn#back1676086355333"
        "https://ada.baidu.com/site/shhqykyy.cc/xyl?imid=f784fda28ae3b6ed7356be2abf079f3f&pbd02&JH449&HQPF-djpz&dijiapiza&&bd_vid=nH6kP1D3Pjf4nH04P1c3PW6vPj7xnWcdg1PxnH0sg1wxPHDkPj0znWm4rjm#back1676086423964"
        "https://ada.baidu.com/site/columbia-kyguke.com/xyl?imid=75775d67b0e681d604fdbf1130222972&bd_jh=bd_xgj&planid=15690380&unitid=475909484&keywordid=95471003416&creative=51884149232&matchtype=2&dongtai=0&trig_flag=nm&crowdid=4064040&kw_enc=%BC%E7%B9%D8%BD%DA%CD%D1%BE%CA&bd_vid=nHT3nHb3PH6vnH6vPjf4n1DkPWuxnWcdg17xnH0sg1wxPHD3rjfkPjbzn1c#back1676086504743"
        "https://ada.baidu.com/site/qianhu.wejianzhan.com/xyl?imid=d69bf166f0bfc33ca37fed0b3e43170e&hean-04-zhongyK-zhongxingc-2022.9.16&bd_vid=nH0krj0vPWmLrjn1rj0LPWfsrjKxnWcdg17xnH0sg1wxPWTkPW6YPHfYP10#back1676086588414"
        "https://ada.baidu.com/site/hesxg.com/xyl?imid=556953d9072fea9364f306a75ecc7d87&QD=baidu3&JH=naolei_naoleihouyizheng&DY=naoshuaishang&GJC=naobushuaishangdehouyizheng&e_creative=69441512505&bd_vid=nHfsP1fLPW0vnj04P1bznjmvPHKxnWcdg1PxnH0sg1wxPWbYPjDdnHcdnjR#back1676086635952"
        "https://ada.baidu.com/site/wjzsqmyf/xyl?imid=9e64b73ab273387a8e4d59fbd3cefdf8&mzxm_BD1_shanhai_smz_smz_fyc_&e_keywordid2=554129198910&bd_vid=nHfLnjRzP1n4nWfLnWfzrHb1PHwxnWcdg17xnH0sg1wxPWbLrHT3PjT3nW0&sdclkid=AL2z152GA6DibLApALA#back1676086662965"
        "https://ada.baidu.com/site/shneuro.com/xyl?imid=3fb0842c76e3261b0f200158293319dc&bd_vid=nHckrjcsn1DLPWRvnHR1rHndnW9xnWcdg17xnH0sg1wxn1c4nj6knH0kPHD#back1676086707161"
        "https://ada.baidu.com/site/xpzyyy.com/xyl?imid=91ba4b0d56aef40a06c90930bf37fead#PC-baidu&xpgck-E-23-25977!&bdkeyword=122475143682&bdcreative=31278902879&bd_vid=nHRLrjbznWmznWDLnWDvnH64rHwxnWcdg1PxnH0sg1wxn1DzP164njc3P1b"
        "https://ada.baidu.com/site/yiboyiyuan16.com/xyl?imid=e3b2baa1efab85db7548c3cd6b999bf0&baidu-PC-yb07-F-09-0127852!&bd_vid=nHRLrjbznWmznWDLnWDvnH64rHwxnWcdg1wxnH0sg1wxPjcznj6YPWTLnHT"
        "https://ada.baidu.com/site/wjz70c46/xyl?imid=6e491f01918e7a86b10de8266ffb9985&source=bdjj1&plan=%E3%80%90hx%E3%80%91zdll&unit=x-pf&keyword=pfzdssm&e_creative=69232040124&e_keywordid=539401234394&e_keywordid2=539401234394&bd_vid=nHn1PWb4nWmzP161rj0dnjc3nj7xnWcdg1PxnH0sg1wxPWbzn1csPj0knWf&sdclkid=AL2z152GA6DibLApALA#back1676086770499"
        "https://ada.baidu.com/site/wjzsg070/xyl?imid=6ef15aeedbb5b23d235cea459c538b3b&erbihou=%E8%80%B3%E9%83%A8-%E8%80%B3%E9%B8%A3-%E5%8C%BB%E9%99%A2&e_keywordid=532362053787&e_keywordid2=513432816635&bd_vid=nHc4P1fdnHDvrHf3nWD4PWRYn1PxnWcdg1FxnH0sg1wxPW6snW6YnjRzn1c#back1676086853089"
        "https://ada.baidu.com/site/wjzhrdyq/xyl?imid=ec4cced639e2f24915e4624c5258e966&baidu10_B02_LBXJ&bd_vid=nHRYnWf4njDLnWDsnj61n1TzPH7xnWcdg1PxnH0sg1wxPWcLnjDLnWnsrHR"
        "https://ada.baidu.com/site/wjzb7a1v/xyl?imid=77646e6fee9ab437765d0511e1f4cab3&fxxieai-06-zhongliu-linbl-llc-mc-0058497&bd_vid=nH6kP1D3Pjf4nH04P1c4PHn1nH9xnWcdg17xnH0sg1wxPHTkPWDkrj0zrH0"
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




