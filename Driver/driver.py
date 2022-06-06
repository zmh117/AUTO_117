from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,os,pymssql
from  LOG.testlog import  InfoLog as ilog
from  LOG.testlog import  ErrorLog  as elog


class app():

    def __init__(self):
        # appium服务监听地址
        self.server='http://127.0.0.1:4723/wd/hub'
        # app启动参数
        self.desired_caps={
            "platformName": "Android",
            #安卓版本
            "appium:platformVersion": "11",
            #设备id
            "appium:deviceName":"172.16.209.150:5555",#127.0.0.1:62001  11PAAB8A0NXP21E0328 RN303Z0478
            "appium:noReset": True,
            "appium:newCommandTimeout": 60000,
            #找开发要
            "appium:appPackage": "com.wisdom.mingdu.operation",
            "appium:appActivity": "com.wisdom.mingdu.operation.module.guide.GuideActivity"
            }
        # 驱动
        self.driver = webdriver.Remote(self.server, self.desired_caps)



        #等待15s
        self.wait = WebDriverWait(self.driver, 15)


    def width_height(self):

        screen = self.driver.get_window_size()
        #返回平板的分辨率
        #{'width': 1280, 'height': 728}


        return screen

    #按坐标点击 coordinate =[(0, 1), (560, 2)]
    def point_click(self,coordinate):
        self.driver(coordinate,500)

    #截屏
    def screenshots(self,iv,page_name):
        #等待加载完成2s
        if iv!=0:
            time.sleep(iv)
        try:
        #获取screenshots的目录
            img_folder=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))+'\\screenshots\\'
        #print (img_folder)
        #获取时间
            screenshot_time = time.strftime('%Y%m%d%H%M%S')
        #page_name 功能名称，页面名称
            screenshot_save_path = img_folder + page_name +'-'+ screenshot_time  + '.png'
        #print (screenshot_save_path)
            self.driver.get_screenshot_as_file(screenshot_save_path)
        except Exception :
            elog(page_name).WriteLogtoFile("{}-截图失败".format(page_name))

            return False
        ilog(page_name).WriteLogtoFile("{}-截图成功".format(page_name))
        return True




    #滑动屏幕
    #a,b,c,d 表示屏幕占比
    def swipe(self,a,b,c,d):
        page_name="滑动屏幕"
        try:
            size = self.driver.get_window_size()
            x=size["width"]
            y=size["height"]
            x1=x*a
            y1=x*b
            x2=y*c
            y2=y*d
        #从(x1,y1)滑动到(x2,y2)
            self.driver.swipe(x1,y1,x2,y2)
        except Exception :
            elog(page_name).WriteLogtoFile("{}-失败".format(page_name))

            return False
        ilog(page_name).WriteLogtoFile("{}-成功".format(page_name))
        return True

        # 判断按钮是不是灰色
    def is_element_work(self, element):
        return element.is_enabled()


class get_data():
    #记录间隔interval 5s
    def __init__(self,Flag,interval=3):
        self.interval=interval
        self.Flag=Flag

    def get_cpu_info(self,page_name):

        # 获取日志的目录
        cpu_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '\\CPU_info\\'
        # 获取时间
        cpu_file_time = time.strftime('%Y%m%d')
        text=cpu_folder+cpu_file_time+".txt"
        #print (text)
        while (self.Flag):
                with open(text,'a+') as w:
                # os.popen(a,'r',1)
                # 找到对应的app的资源占用
                    cpu_time = time.strftime('%Y%m%d%H%M%S')
                    cmd = 'adb shell top -n 1 | findstr  com.wisdom.mi'
                    cpu_info = os.popen(cmd)
                    for i in cpu_info:
                        #print (i)
                        line=page_name+"-"+cpu_time+","+i
                        #print("2"+line,type(line))
                        w.write(line)
                        #print("1"+line)
                        break
                #没过3s，读一次
                time.sleep(self.interval)
        w.close()


class  get_sql_server():
    def __init__(self):
        self.conn=pymssql.connect(
    server="192.168.88.124",
    user="sa",
    password="ZMH11.",
    database="MDEBR",
    autocommit=True,
    port='1433',
    as_dict=True
)


    def cur(self):
        try:

            cur=self.conn.cursor()
        except Exception:
            elog("数据库").WriteLogtoFile("数据库连接失败，请检查配置！")
        if cur:
            ilog("数据库").WriteLogtoFile("数据库连接成功！")
            return cur

    def sql_check_one(self,sql,col_name):
        time.sleep(4)
        a=self.cur()
        sql_=sql
        a.execute(sql_)
        result=a.fetchone()
        a.close()
        self.conn.close()
        return result[col_name]
    def sql_check_all(self,sql,col_name):
        time.sleep(4)

        results=[]
        a=self.cur()
        sql_=sql
        a.execute(sql_)
        result=a.fetchall()
        for i in result:
            results.append(i[col_name])
        a.close()
        self.conn.close()
        return results

    def sql_check_all_args(self,sql,*col_name):
        time.sleep(4)
        results_list=[]
        a=self.cur()
        sql_=sql
        a.execute(sql_)
        result=a.fetchall()
        for i in result:
            results = {}
            for j in col_name:
                results[j]=i[j]
                results_list.append(results)
                #results_list.sort()
        a.close()
        self.conn.close()
        return results_list




if __name__ == "__main__":
    s= app()

    s.screenshots("sss")
    # g.get_cpu_info("登录")
    #
    #
    # a=s.width_height()
    # # 返回平板的分辨率
    # print(a["width"],a["height"])
    # s=get_sql_server()
    # g=s.sql_check_all_args("select * from XPHARMA_USER_CERT_FILES;","C_USER_ID","C_USER_NAME")
    # print(g,type(g))
