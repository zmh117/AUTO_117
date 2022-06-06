import  unittest,HTMLReport
class aaa(object):
    def __init__(self ):
        self.a="a"
    def ssss(self):
        b=self.a+"1111"
        print("aaa_ssss")
        return b


class case_1(unittest.TestCase):
    p=aaa()
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)


    @classmethod
    def setUpClass(cls):
        print("this setupclass() method only called once.\n")
        print(cls.p,id(cls.p),"\n")
    @classmethod
    def tearDownClass(cls):
        print ("this teardownclass() method only called once too.\n")
    def setUp(self):
        print ("do something before test : prepare environment.\n")
    def tearDown(self):
        print ("do something after test : clean up.\n")

    def test_ss(self):
        A=self.p.ssss()
        self.assertEqual("a1111", A)
        print("-test_ss--",self.p,id(self.p))


    def test_tt(self):
        self.p.ssss()
        print("tt")



if __name__=="__main__":
    # aaa.ssss()
    # unittest.main()
    #
    # 测试套件
    suite = unittest.TestSuite()
    # 测试用例加载器
    loader = unittest.TestLoader()
    # 把测试用例加载到测试套件中
    suite.addTests(loader.loadTestsFromTestCase(case_1))

    # 测试用例执行器
    runner = HTMLReport.TestRunner(report_file_name='test',  # 报告文件名，如果未赋值，将采用“test+时间戳”
                                   output_path='report',  # 保存文件夹名，默认“report”
                                   title='测试报告',  # 报告标题，默认“测试报告”
                                   description='无测试描述',  # 报告描述，默认“测试描述”
                                   thread_count=1,  # 并发线程数量（无序执行测试），默认数量 1
                                   thread_start_wait=3,  # 各线程启动延迟，默认 0 s
                                   sequential_execution=True,  # 是否按照套件添加(addTests)顺序执行，
                                   # 会等待一个addTests执行完成，再执行下一个，默认 False
                                   # 如果用例中存在 tearDownClass ，建议设置为True，
                                   # 否则 tearDownClass 将会在所有用例线程执行完后才会执行。
                                   # lang='en'
                                   lang='cn'  # 支持中文与英文，默认中文
                                   )
    # 执行测试用例套件
    runner.run(suite)
