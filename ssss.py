from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
# appium服务监听地址
server='http://127.0.0.1:4723/wd/hub'
# app启动参数
desired_caps={
   "platformName": "Android",
  "appium:platformVersion": "11",
  "appium:deviceName":"11PAAB8A0NXP21E0328",#华为9YYNU20809406590  工业平板16QAC4670NXP21F0627
  "appium:noReset": True,
  "appium:newCommandTimeout": 60000,
  "appium:appPackage": "com.wisdom.mingdu.operation",
  "appium:appActivity": "com.wisdom.mingdu.operation.module.guide.GuideActivity"
}#com.wisdom.mingdu.operation.module.guide.GuideActivity

# 驱动
driver = webdriver.Remote(server,desired_caps)
wait = WebDriverWait(driver,15)
# 获取用户名



# 获取用户名
login_name = wait.until(EC.presence_of_element_located((By.ID,"com.wisdom.mingdu.operation:id/et_login_name")))
login_name.send_keys("ZMH")
# 获取密码文本框
phone_pwd = wait.until(EC.presence_of_element_located((By.ID,"com.wisdom.mingdu.operation:id/et_login_password")))
phone_pwd.send_keys("1111")
# 点击登录按钮
login_btn = wait.until(EC.presence_of_element_located((By.ID,"com.wisdom.mingdu.operation:id/ll_login")))
login_btn.click()


# print(type(login_btn),login_btn)
# //wo20211100001
for i in range(300):
    print ("i=",i)
    i=i%10
    print("i%10=",i)
    a=139+82*i
    b=219+82*i
    print ("点击前",a,b)
    wait.until(EC.presence_of_element_located((By.ID,"com.wisdom.mingdu.operation:id/iv_show_list"))).click()
    wait.until(EC.presence_of_element_located((By.ID,"com.wisdom.mingdu.operation:id/tv_dealt"))).click()
    driver.tap([(0, a), (560, b)], 500)
    print("点击后", a, b)
#[0, 221][560, 301]

       # [0, 139][560, 219]
       # [0, 221][560, 301]
#[0, 959][560, 1039]
#[0,1041][560,1104]
    try:
        button=wait.until(EC.presence_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView")))
        button.click()

    except Exception:
        print("pass")
        continue
    try:
        wait.until(EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/tv_work_start_ok"))).click()
    except Exception:
        print("pass")
        continue
    '''
    currentTime = time.strftime('%Y-%m-%m %H:%M:%S')
    # 执行获取电量的命令
    result = os.popen("adb shell dumpsys battery")
    # 获取电量的 level
    for line in result:
        if "level" in line:
            power = line.split(":")[1]
    print(currentTime + "," + power)
    with open("battery.csv", "a+") as w:
        w.write(currentTime + "," + power)
    w.close()

'''
#
# while(True):
#     time.sleep(30)
#     currentTime = time.strftime('%Y-%m-%m %H:%M:%S')
#     # 执行获取电量的命令
#     result = os.popen("adb shell dumpsys battery")
#     # 获取电量的 level
#     for line in result:
#         if "level" in line:
#             power = line.split(":")[1]
#     print(currentTime + "," + power)
#     with open("battery.csv", "a+") as w:
#         w.write(currentTime + "," + power )
#     w.close()