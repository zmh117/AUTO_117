from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from  LOG.testlog import  InfoLog as ilog
from  LOG.testlog import  ErrorLog  as elog

import Element.base_element as base_element
import time

class all_element(base_element.Base_element):
    def __init__(self):
        super().__init__()
    def get_login_name(self):
        functions = "登录"
        name = "用户名输入框"
        try:
            loginname=self.wait.until(EC.presence_of_element_located((By.ID,"com.wisdom.mingdu.operation:id/et_login_name")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return loginname



    def get_login_password(self):
        functions = "登录"
        name = "密码输入框"
        try:
            password= self.wait.until(EC.presence_of_element_located((By.ID,"com.wisdom.mingdu.operation:id/et_login_password")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return password

    def get_login_button(self):
        functions = "登录"
        name = "登录按钮"
        try:
            button= self.wait.until(EC.presence_of_element_located((By.ID,"com.wisdom.mingdu.operation:id/ll_login")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_list_button(self):
        functions = "工单列表"
        name = "列表按钮"
        try:
            button= self.wait.until(EC.presence_of_element_located((By.ID,"com.wisdom.mingdu.operation:id/iv_show_list")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_dealt_list_button(self):
        functions = "工单列表"
        name = "待办列表按钮"
        try:
            button= self.wait.until(EC.presence_of_element_located((By.ID,"com.wisdom.mingdu.operation:id/tv_dealt")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_production_list_button(self):
        functions = "工单列表"
        name = "生产中列表按钮"
        try:
            button= self.wait.until(EC.presence_of_element_located((By.ID,"com.wisdom.mingdu.operation:id/tv_production")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    #获取列表数据的位置  分辨率改变后，不适用了
    #[(a, b), (c, d)]  分辨率-{'width': 1280, 'height': 728}
    #   [0,105][420,165]
    #   [0, 167][420, 227]
    #index 表示从上到下第几个 数字
    def get_list_position(self,index):
        functions="工单列表"
        h=self.width_height()["height"]
        w=self.width_height()["width"]
        a1=0
        b1=int( (105+(index-1)* 62) *h/728)
        c1=int(420/1280 * w)
        d1=int( (165+(index-1)* 62) *h/728)
        pos=[(a1,b1),(c1,d1)]

        ilog(functions).WriteLogtoFile("列表记录定位成功{}".format(str(pos)))

        return pos
    #工单名 name
    def get_list_choose_wo(self,name):
        functions = "代办/进行工单列表"
        try:
            button = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                     "//*[@resource-id='com.wisdom.mingdu.operation:id/tv_whole_show'][@text=\'{}\']".format(name))))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到工单:{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("工单:{}定位成功".format(name))
        return button

        # 根据 name 选中获取块状列表的
    #称量列表可用  库存创建控件-物流查询页面-物料列表  存储位置列表
    def get_tv_whole_show(self, fun,title):

        functions = fun
        name=title
        try:
            button = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                         "//*[@resource-id='com.wisdom.mingdu.operation:id/tv_whole_show'][@text=\'{}\']".format(name))))
        except Exception:
            elog(functions).WriteLogtoFile("名字是{}的记录定位失败".format(name))
            return None
        ilog(functions).WriteLogtoFile("名字是{}的记录定位成功".format(name))
        return button


    def get_wo_start_button(self):
        functions = "工单开始"
        name = "工单开始按钮"
        try:
            button= self.wait.until(EC.presence_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_tv_work_start_ok(self):
        functions = "工单开始"
        name = "工单开始确定按钮"
        try:
            button= self.wait.until(EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/tv_work_start_ok")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    #获取任务列表任务执行按钮的位置
    def get_task_position(self,index):
        functions = "任务开始"
        try:
            button= self.wait.until(EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[{}]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView".format(str(index)))))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到第{}个任务的开始按钮".format(str(index)))
            return None
        ilog(functions).WriteLogtoFile("第{}个任务的开始按钮定位成功".format(str(index)))


        return button

        # 获取任务列表 的任务，0表示执行第一个
    def get_tv_task_execute(self, index):
        functions = "任务开始"
        try:
            button = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,"//*[@resource-id='com.wisdom.mingdu.operation:id/tv_task_execute'][@text='执行']"
                                                                         )))[index]
        except Exception:
            elog(functions).WriteLogtoFile("没有找到第{}个任务的开始按钮".format(str(index)))
            return None
        ilog(functions).WriteLogtoFile("第{}个任务的开始按钮定位成功".format(str(index)))

        return button

    #任务搜索，任务类型
    def get_task_type_search(self):
        pass

    # 任务搜索，任务状态
    def get_task_state_search(self):
        pass

    # 任务搜索，任务名称
    def get_task_name_search(self):
        functions = "任务搜索"
        name = "任务名称输入框"
        try:
            button= self.wait.until(EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/et_task_name")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button


    # 任务搜索，搜索按钮
    def get_task_search_button(self):
        functions = "任务搜索"
        name = "任务搜索按钮"
        try:
            button= self.wait.until(EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/ll_task_search")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    #当前工单按钮  #判断是否选中  self.is_selected()
    def get_wo_task_button(self):
        functions = "任务搜索"
        name = "当前工单按钮"
        try:
            button= self.wait.until(EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/cb_check_now")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button






    #回到任务列表
    def get_back_button(self):
        functions = "返回任务列表"
        name = "返回任务列表按钮"

        try:
            button= self.wait.until(EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/iv_logo")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button



    #获取称量物料列表
    #index 表示第几个物料
    #选中称量物料
    def get_weight_step_material_list(self,index):
        functions = "称量任务"

        try:
            button= self.wait.until(EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[{}]/android.widget.LinearLayout/android.widget.LinearLayout[8]".format(str(index)))))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到称量列表的第{}个物料".format(str(index)))
            return None
        ilog(functions).WriteLogtoFile("称量列表的第{}个物料定位成功".format(str(index)))

        return button
    #称量按钮
    def get_tv_weigh_wg_weigh(self):

        functions = "称量任务"
        name = "称量按钮"
        try:
            button= self.wait.until(EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/tv_weigh_wg_weigh")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    #结束称量按钮
    def get_tv_weigh_wg_finish(self):
        functions = "称量任务"
        name = "称量结束按钮"
        try:
            button= self.wait.until(EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/tv_weigh_wg_finish")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_tv_weigh_wg_force(self):
        functions = "称量任务"
        name = "称量结束按钮"
        try:
            button= self.wait.until(EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/tv_weigh_wg_force")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_tv_we_weigh_start(self,title):
        name=title
        functions = "称量任务"
        #name = "开始称量按钮/确认称量模式按钮/确认物料批次按钮/确认净重按钮"
        try:
            button= self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@resource-id='com.wisdom.mingdu.operation:id/tv_we_weigh_start'][@text=\'{}\']".format(title))))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button



    #开始称量按钮/确认称量模式按钮/确认物料批次按钮/确认净重按钮
    def get_weight_start_button(self):
        name="开始称量按钮"
        functions = "称量任务"
        #name = "开始称量按钮/确认称量模式按钮/确认物料批次按钮/确认净重按钮"
        try:
            button= self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@resource-id='com.wisdom.mingdu.operation:id/tv_we_weigh_start'][@text='开始称量']")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    # 开始称量按钮/确认称量模式按钮/确认物料批次按钮/确认净重按钮
    def get_weight_model_ok_button(self):
        name = "确认称量模式按钮"
        functions = "称量任务"
        # name = "开始称量按钮/确认称量模式按钮/确认物料批次按钮/确认净重按钮"
        try:
            button = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//*[@resource-id='com.wisdom.mingdu.operation:id/tv_we_weigh_start'][@text='确认称量模式']")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    # 开始称量按钮/确认称量模式按钮/确认物料批次按钮/确认净重按钮
    def get_weight_lot_ok_button(self):
        name = "确认物料批次按钮"
        functions = "称量任务"
        # name = "开始称量按钮/确认称量模式按钮/确认物料批次按钮/确认净重按钮"
        try:
            button = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//*[@resource-id='com.wisdom.mingdu.operation:id/tv_we_weigh_start'][@text='确认物料批次']")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    # 开始称量按钮/确认称量模式按钮/确认物料批次按钮/确认净重按钮
    def get_weight_ok_button(self):
        name = "确认净重按钮"
        functions = "称量任务"
        # name = "开始称量按钮/确认称量模式按钮/确认物料批次按钮/确认净重按钮"
        try:
            button = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//*[@resource-id='com.wisdom.mingdu.operation:id/tv_we_weigh_start'][@text='确认净重']")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button



    #称量步，确认物料批次提示的确认按钮
    def get_tv_notice_ok(self):
        functions = "称量任务"
        name = "确认物料批次提示的确认按钮"
        try:
            button= self.wait.until(EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/tv_notice_ok")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    #称量步，确认物料批次提示的取消按钮
    def get_tv_notice_cancel(self):
        functions = "称量任务"
        name = "确认物料批次提示的取消按钮"
        try:
            button= self.wait.until(EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/tv_notice_cancel")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    #称量步，净重输入框
    def get_et_wem_weight_3(self):
        functions = "称量任务"
        name = "净重输入框"
        try:
            button= self.wait.until(EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/et_wem_weight_3")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

        # 称量步，返回
    def get_tv_weigh_execute_back(self):
        functions = "称量任务"
        name = "返回按钮"
        try:
            button = self.wait.until(EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/tv_weigh_execute_back")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button


    def get_next(self):
        #"下一项"
        functions = "工序记录"
        name = "下一项按钮"
        try:
        # 显示等待检测元素  <android.widget.Button>
            button=  self.wait.until(EC.presence_of_element_located((By.XPATH,"//android.widget.Button[@text='下 一 项']")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_current(self):
        # "当 前 项"
        functions = "工序记录"
        name = "当前项按钮"
        try:
        # 显示等待检测元素
            button=  self.wait.until(EC.presence_of_element_located((By.XPATH,"//android.widget.Button[@text='当 前 项']")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button




    def get_force(self):
        # "输 入 强 制"
        functions = "工序记录"
        name = "当前项强制按钮"
        try:
            # 显示等待检测元素
            button=  self.wait.until(EC.presence_of_element_located((By.XPATH,"//android.widget.Button[@text='输 入 强 制']")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_input_box(self):
        # "工序记录输入框"android.widget.EditText
        functions = "工序记录"
        name = "工序记录输入框"
        try:
            # 显示等待检测元素
            button=  self.wait.until(EC.presence_of_all_elements_located((By.XPATH,"//android.widget.EditText")))[-1]
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_et_user_name(self):
        functions = "单签"
        name = "签名名字输入框"
        try:
            button = self.wait.until(EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/et_user_name")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_et_user_password(self):
        functions = "单签"
        name = "签名密码输入框"
        try:
            button = self.wait.until(EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/et_user_password")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button


    def get_et_sign_reason(self):
        functions = "单签"
        name = "签名原因输入框"
        try:
            button = self.wait.until(EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/et_sign_reason")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_tv_sign_confirm(self):
        functions = "单签"
        name = "签名确定按钮"
        try:
            button = self.wait.until(EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/tv_sign_confirm")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button



    def get_tv_sign_cancel(self):
        functions = "单签"
        name = "签名取消按钮"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/tv_sign_cancel")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button


    #工序记录步的 功能按钮  name就是名字，注意空格
    def get_fun_button(self,name):
        #  "设备选择"
        functions = "工序记录"
        try:
            # 显示等待检测元素[@text='设备选择']
            button=  self.wait.until(EC.presence_of_element_located((By.XPATH,"//android.widget.Button[@text=\'{}\']".format(name))))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}按钮".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}按钮定位成功".format(name))
        return button

    #库存创建-批次号
    def get_et_ine_batch_no(self):
        functions = "库存创建控件"
        name = "批次号输入框"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/et_ine_batch_no")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    #选择物料-物料编码
    def get_tv_ine_mat_code(self):
        functions = "库存创建控件"
        name = "物料编码输入框"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/tv_ine_mat_code")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_et_mat_select_get_code(self):
        functions = "选择物料"
        name = "物料编码输入框"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/et_mat_select_get_code")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_ll_materiel_select_search(self):
        functions = "选择物料"
        name = "物料编码搜索按钮"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/ll_materiel_select_search")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button
    #选择物料 物料编码
    def get_mat_code_mat_code(self,code):
        functions="选择物料"
        name="物料编码"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[@resource-id='com.wisdom.mingdu.operation:id/tv_whole_show'][@text=\'{}\']".format(code))))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_tv_mat_select_ok(self):
        functions="选择物料"
        name="物料选择确认按钮"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/tv_mat_select_ok")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_et_ine_mat_count(self):
        functions="库存创建控件"
        name="数量输入框"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/et_ine_mat_count")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_tv_ine_quality_status(self):
        functions="库存创建控件"
        name="质量状态下拉框"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/tv_ine_quality_status")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    #下拉框  库存创建控件-质量状态 切换工作中心-工作中心和工作单元字段
    def get_tv_item_value(self,status):
        functions="选择物料"
        name=status
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[@resource-id='com.wisdom.mingdu.operation:id/tv_item_value'][@text=\'{}\']".format(status))))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_tv_ine_save_position(self):
        functions = "获取存储位置"
        name = "存储位置"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/tv_ine_save_position")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_et_sp_position_code(self):
        functions = "存储位置"
        name = "存储位置编码"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/et_sp_position_code")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_ll_sp_select_search(self):
        functions = "存储位置"
        name = "存储位置查找按钮"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/ll_sp_select_search")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_select_position(self,code):
        functions="存储位置"
        name=code
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[@resource-id='com.wisdom.mingdu.operation:id/tv_whole_show'][@text=\'{}\']".format(code))))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button
    def get_tv_save_position_ok(self):
        functions = "存储位置"
        name = "存储位置确定按钮"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/tv_save_position_ok")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_et_ine_con_bind(self):
        functions="库存创建控件"
        name="容器输入框"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/et_ine_con_bind")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button


    def get_tv_ine_save_confirm(self):
        functions="库存创建控件"
        name="库存创建确认按钮"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/tv_ine_save_confirm")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    #获取错误提示信息
    def get_toast_message(self,message):
        functions = "获取toast消息"
        name = "toast消息"

        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(@text, \'{}\')]".format(message))))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}:{}".format(name,message))
            return False
        ilog(functions).WriteLogtoFile("{}:{}-定位成功".format(name,message))
        return True
    # 数值，文本控件错误提示信息
    def get_toast_message_info(self,message):
        functions = "获取toast消息"
        name = "toast消息"

        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(@text, \'{}\')]".format(message))))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}:{}".format(name,message))
            return None
        ilog(functions).WriteLogtoFile("{}:{}-定位成功".format(name,message))
        return button.text


    def get_iv_order_to_operation(self):
        functions = "打开菜单"
        name = "打开菜单按钮"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/iv_order_to_operation")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button
    #     菜单功能
    def get_tv_operation_name(self,title):
        functions = "菜单栏按钮"
        name =   title+"菜单按钮"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@resource-id='com.wisdom.mingdu.operation:id/tv_operation_name'][@text=\'{}\']".format(title))))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_tv_work_center_select(self):
        functions = "设置工作中心"
        name = "工作中心列表"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/tv_work_center_select")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button


    def get_tv_work_center_unit_select(self):
        functions = "设置工作中心"
        name = "工作单元列表"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/tv_work_center_unit_select")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button

    def get_tv_switch_work_center_ok(self):
        functions = "设置工作中心"
        name = "切换确定按钮"
        try:
            button = self.wait.until(
                EC.presence_of_element_located((By.ID, "com.wisdom.mingdu.operation:id/tv_switch_work_center_ok")))
        except Exception:
            elog(functions).WriteLogtoFile("没有找到{}".format(name))
            return None
        ilog(functions).WriteLogtoFile("{}定位成功".format(name))
        return button


if __name__ =="__main__":
    a=all_element()
    a.get_login_name().send_keys("admin")
    a.get_login_password().send_keys("1111")
    #a.screenshots("登录")
    a.get_login_button().click()
    # pp=a.get_toast_message("用户名密码错误")
    # print(pp)
    a.get_iv_order_to_operation().click()
    a.get_tv_operation_name("展开").click()
    a.get_tv_operation_name("设置").click()
