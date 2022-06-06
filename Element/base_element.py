from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import  Driver.driver as driver
#元素分类
#撰写公共方法
class Base_element(driver.app):

    def __init__(self):
        super().__init__()


#
# #按钮
# class Button(Base_element):
#     pass
#
# #输入框
# class Text_box(Base_element):
#     pass
#
#
# #多选框
# class Theck_box(Base_element):
#     pass
#
# #单选框
# class Radio(Base_element):
#     pass
#
# #下拉框
# class Select(Base_element):
#     pass
#
# #弹出框
# class Popup(Base_element):
#     pass
#
# #勾选
# class Tick (Base_element):
#
#     pass
#
# #表单列表
# class List(Base_element):
#     pass
#


if __name__ =="__main__":
    a=Base_element()
    s=a.wait()
    print (s)
