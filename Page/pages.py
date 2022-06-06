import Element.elements as el
from  LOG.testlog import  InfoLog as ilog
from  LOG.testlog import  ErrorLog  as elog
import time
class page(el.all_element):
    def __init__(self):
        super().__init__()
    #签名 名字 密码 原因
    def single_sign(self,name,pwd,reason):
        page_name="单签"
        try:
            self.get_et_user_name().send_keys(name)
            self.get_et_user_password().send_keys(pwd)
            self.get_et_sign_reason().send_keys(reason)
            self.get_tv_sign_confirm().click()
        except Exception:
            elog(page_name).WriteLogtoFile("单签失败")
            return None
        ilog(page_name).WriteLogtoFile("单签成功")

    def login_page(self,name,password):
        page_name="登录"
        try:
            self.get_login_name().send_keys(name)
        except Exception:
            elog(page_name).WriteLogtoFile("登录输入框输入失败")
            return None

        ilog(page_name).WriteLogtoFile("登录输入框输入成功")
        try:
            self.get_login_password().send_keys(password)

        except Exception:
            elog(page_name).WriteLogtoFile("密码输入框输入失败")
            return None

        ilog(page_name).WriteLogtoFile("密码输入框输入成功")
        try:
            self.get_login_button().click()
        except Exception:
            ilog(page_name).WriteLogtoFile("登录按钮点击失败")
            return None
        ilog(page_name).WriteLogtoFile("登录按钮点击成功")
        #截图

        # if self.get_toast_message_info("用户名"):
        #     elog(page_name).WriteLogtoFile(self.get_toast_message_info("用户名"))
        # else :
        #     pass
        self.screenshots(0,page_name)
        return page_name

    def start_wo(self,wo_name):
        page_name="开始工单"
        try:

            #开始工单
            self.get_list_button().click()
            self.get_dealt_list_button().click()
            self.get_list_choose_wo(wo_name).click()
            self.get_tv_operation_name("工单开始").click()
            self.get_tv_work_start_ok().click()

        except Exception:
            elog(page_name).WriteLogtoFile("{}-失败".format(page_name))
            return None
        ilog(page_name).WriteLogtoFile("{}-成功,等待50s".format(page_name))
        time.sleep(50)

    #定位任务 任务名称 工单位置
    def task(self,task_name,wo_name):
        page_name="定位任务"+task_name
        try:
            # 定位工单，任务
            self.get_list_button().click()
            self.get_production_list_button().click()

            while not self.get_list_choose_wo(wo_name):
                self.swipe(0.1,0.5,0.1,0.1)

            self.get_list_choose_wo(wo_name).click()
            self.get_back_button().click()
            button=self.get_wo_task_button()
            #print(button.get_attribute("checked"))
            if   button.get_attribute("checked") == "false":
                button.click()
            else:

                pass
            self.get_task_name_search().clear()
            self.get_task_name_search().send_keys(task_name)
            self.get_task_search_button().click()
            # 执行任务
            time.sleep(2)
            self.get_tv_task_execute(0).click()
            self.screenshots(5,page_name)
        except Exception:
            elog(page_name).WriteLogtoFile("{}-失败".format(page_name))
            return None
        ilog(page_name).WriteLogtoFile("{}-成功".format(page_name))

    #称量步  ，称量值w1-w5
    def weight(self,w1,w2,w3,w4,w5):
        page_name = "称量任务"
        try:

            #称量结束
            if self.is_element_work(self.get_tv_weigh_wg_finish()):
                self.get_tv_weigh_wg_finish().click()
            else:
                elog(page_name).WriteLogtoFile("称量结束按钮置灰")
                return None
            #签名
            self.single_sign("admin","1111","1234")
        except Exception:
            elog(page_name).WriteLogtoFile("称量步执行失败")
            return None
        ilog(page_name).WriteLogtoFile("称量成功")

    def  text_control(self,text):
        page_name="文本控件"
        try:

            self.screenshots(2,page_name)
            #获取初值
            time.sleep(2)
            first=self.get_input_box().text
            self.get_input_box().clear()
            self.get_input_box().send_keys(text)
            self.screenshots(2,page_name)
            #输出初值和新值
            self.get_next().click()
        except Exception:
            elog(page_name).WriteLogtoFile("{}执行失败".format(page_name))
            return None
        ilog(page_name).WriteLogtoFile("{}执行成功".format(page_name))
        self.get_next().click()
        return [first,text]

    def  number_control(self,number):
        page_name="数值控件"
        try:

            self.screenshots(2,page_name)

            #获取初值
            first=self.get_input_box().text
            self.get_input_box().send_keys(number)
            #输出初值和新值
            self.screenshots(2,page_name)
            self.get_next().click()
        except Exception:
            elog(page_name).WriteLogtoFile("数值控件执行失败")
            return None
        ilog(page_name).WriteLogtoFile("数值控件执行成功")

        return [first,number]

    def mat_code(self,page_name,code):
        name="获取物料编码"
        try:
            self.get_et_mat_select_get_code().send_keys(code)
            self.get_ll_materiel_select_search().click()
            self.get_tv_whole_show(name,code).click()
            self.get_tv_mat_select_ok().click()

        except Exception:
            elog(page_name).WriteLogtoFile("{}执行失败".format(name))
            return None
        ilog(page_name).WriteLogtoFile("{}执行成功".format(name))

    def position_code(self, page_name, code):
        name = "获取存储位置"
        try:
            self.get_et_sp_position_code().send_keys(code)
            self.get_ll_sp_select_search().click()
            self.get_select_position(code).click()
            self.get_tv_save_position_ok().click()

        except Exception:
            elog(page_name).WriteLogtoFile("{}执行失败".format(name))
            return None
        ilog(page_name).WriteLogtoFile("{}执行成功".format(name))

        # 批次号 物料编码 ，数量，质量状态，存储位置，容器
    def inventory_creation(self,batch,code,num,status,position_code):
        page_name = "库存创建控件"
        try:
            self.get_next().click()
            self.screenshots(2,page_name)

            self.get_fun_button("库存创建").click()

            if batch !="":
                self.get_et_ine_batch_no().send_keys(batch)
            if code !="":
                self.get_tv_ine_mat_code().click()
                self.mat_code(page_name,code)
            if num!="":
                self.get_et_ine_mat_count().send_keys(str(num))

            if status !="":
                self.get_tv_ine_quality_status().click()
                self.get_tv_item_value(status).click()

            if position_code!="":
                self.get_tv_ine_save_position().click()
                self.position_code(page_name,position_code)

            self.screenshots(2,page_name)
            # 库存创建确认按钮
            self.get_tv_ine_save_confirm().click()


        except Exception:
            elog(page_name).WriteLogtoFile("库存创建控件执行失败")
            return None
        ilog(page_name).WriteLogtoFile("库存创建控件执行成功")

    def start_next(self):

        self.get_next().click()
        ilog("工序记录").WriteLogtoFile("工序记录步开始")


    def change_work_station(self,centre,unit):
        page_name="切换工作中心"
        self.screenshots(1,"切换工作中心前")

        self.get_iv_order_to_operation().click()
        self.get_tv_operation_name("展开").click()
        self.get_tv_operation_name("设置").click()
        self.get_tv_work_center_select().click()
        self.get_tv_item_value(centre).click()
        self.get_tv_work_center_unit_select().click()
        self.get_tv_item_value(unit).click()
        self.get_tv_switch_work_center_ok().click()
        self.single_sign("admin","1111","sss")




        self.screenshots(1, "切换工作中心后")



if __name__=="__main__":
    pages=page()
    pages.login_page("admin","1111")
    #pages.start_wo("A7")
    # pages.start_wo("SSSS4")
    # pages.task("库存创建控件","SSSS20")
    # # pages.text_control("SOS")
    # pages.inventory_creation("GTX1080","M006",13.888,"合格","ZC_001")
    pages.change_work_station("104","104-2")

    # pages.task("称量","A7")
    #pages.get_wo_task_button().click()
    #s = pages.get_wo_task_button().get_attribute("checked")
    #print(s,dir(s) )
    # pages.weight(1000.1001,80.2830,110.4167,59.9999,99.9720)
    # pages.task("库存创建控件",8)
    # a=pages.text_control("225")
    # print(a)
    # pages.inventory_creation("","","","","ZC_001")

