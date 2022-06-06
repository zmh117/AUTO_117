import   UseCase.TEST_CASE_001
import HtmlTestRunner,unittest
import time

if __name__=="__main__":
    report_time = time.strftime('%Y%m%d%H%M%S')
    suite = unittest.TestSuite()
    # 把测试用例加载到测试套件中
    suite.addTest(unittest.TestLoader().loadTestsFromModule(UseCase.TEST_CASE_001))

    # 执行测试用例套件
    file="D:\\Appium\\PY\\UseCase\\report\\"
    runner=HtmlTestRunner.HTMLTestRunner(output=file,verbosity=2 , report_name="test",descriptions="测试报告",report_title="测试报告人-庄慕焕")
    runner.run(suite)

