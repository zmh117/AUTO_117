import Page.pages as page
from Driver.driver import get_sql_server
import time
import unittest
from Driver.driver import get_data



class case_001(unittest.TestCase):
    p = page.page()
    def __init__(self,*args ):
        super().__init__(*args )
    @classmethod
    def setUpClass(cls):

        print("this setupclass() method only called once.\n")
    #     # cls.Flag = 1
    #     # g=get_data(cls.Flag)
    #     # g.get_cpu_info("记录cpu")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("this teardownclass() method only called once too.\n")
    #

    def setUp(self):
        print ("do something before test : prepare environment.\n")
    def tearDown(self):
        print ("do something after test : clean up.\n")
        #self.p.driver.close()
    #@unittest.skip("1s")
    def test_a(self):
        wo_name = "AAA16"
        self.p.login_page("admin", "1111")
        self.p.start_wo(wo_name)

        batch="AAA1612"
        self.p.task("库存创建控件",wo_name)
        self.p.start_next()
        A = self.p.text_control("GEX")
        print(A)
        self.p.inventory_creation(batch, "", "", "", "ZC_001")
        sqls="select  C_BATCH_NUM from XPHARMA_WMS_SUBBATCH_INFO where C_SUBBATCH_NUM=\'{}001\';".format(batch)
        print(sqls)
        re=get_sql_server().sql_check_one(sqls,"C_BATCH_NUM")
        print("re:",re)
        self.assertEqual(batch,re)
        self.assertEqual("GEX",A[1])
        self.p.start_next()
        #self.Flag=0

    def test_b(self):
         #self.p.login_page("admin", "1111")
         self.p.change_work_station("104","104-2")





if __name__=="__main__":

    # case=case_001()
    # case.test_inventory_creation()
    # case.p.driver
    # GET=get_data()
    # case.test_ss()
    # page_name="工单开始"
    # T1=threading.Thread(target=case.test_ss )
    # T2=threading.Thread(target=GET.get_cpu_info, args=(page_name, ))
    # T1.start()
    # T2.start()
    #case.test_1("A9")
    #unittest.main(verbosity=2)
    suite = unittest.TestSuite()
    suite.addTest(case_001("test_a"))
    suite.addTest(case_001("test_b"))
    runner= unittest.TextTestRunner()
    runner.run(suite)
