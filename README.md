
# callPhoneBoom
思路：通过爬取使用「莆田系医院」这一营销组件的企业,
我们可以得到数以万计真实企业的网址。
并通过程序模拟浏览，可以将攻击信息给到这些企业。最终达到「电话攻击」的目的。


## 声明
本项目仅供学习交流使用，勿作商业或非法用途。

所有用户个人行为与本项目无关。

## 爬取接口
感谢xdq2005adam提供的爬取脚本catchad

得益于此脚本，你可以本地运行爬取更多地址放入api.txt中，来增加威力

## 使用教程
1. 下载
    ```shell script
     $ git clone https://github.com/olyble/callPhoneBoom.git
    ```
2. 安装 Selenium
   ```shell script
   $ pip3 install selenium
   ```
   安装 Selenium 之后，**需要安装对应浏览器的 Driver** ，参见 Selenium 文档 [1.3 节](https://selenium-python.readthedocs.io/installation.html#drivers)。 
    >Seleium 具体的介绍及使用方法可参见 [Selenium 文档](https://selenium-python.readthedocs.io)。

3. 配置

  在main.py中填入需要轰炸的手机号
  
<!--     配置文件为`config.py`，参数说明如下：
   ```python
   """
   攻击对象信息
   """ 
   target = { 
       "phone": "13012345678",             # 手机号
       "name": "小小明",                    # 姓名
       "email": "xx@xx.xx",                # 邮箱
       "address": "宇宙银河太阳系地球村",     # 地址
       "comment": "你好 不会～"             # 留言信息
   }
   
   """
   参数设置
   """
   settings = {
       "times": 100,                 # 攻击次数
       "timeout": 5,                 # 超时
       "driver":webdriver.Firefox(), # 使用的 driver
   }
   ``` -->
   
   
  使用DrissionPage已合并到main2.只用使用set.py设置环境就可以使用



4. 运行程序
    ```shell script
    $ python3 main.py
    ```
5. Enjoy!

    运行截图：
    
    ![](https://res.cloudinary.com/dxl1idlr5/image/upload/v1675247958/2023/02/ce181419ab91f325ac208e188904538a.png)

## 目录说明


## TODO
1. 使用 PyQt5 实现用户界面。
2. 定时任务。
3. 使用 「HTTP 请求」替代「模拟浏览」。
4. 跳过验证码
5. 封装docker


## 许可
MIT
