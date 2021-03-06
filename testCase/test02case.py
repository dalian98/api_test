import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
import readExcel

url = geturlParams.geturlParams().get_Url()  # 调用我们的geturlParams获取我们拼接的URL
login_xls = readExcel.readExcel().get_xls('userCase.xlsx', 'login1')  # 获取userCase.xlsx中sheet为login1的测试数据


@paramunittest.parametrized(*login_xls)  # 传入参数
class testUsershabi(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):  # 将各参数格式为str
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)

    def description(self):
        self.case_name

    def setUp(self):
        print(self.case_name + "测试开始前准备")

    def test02case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):  # 断言
        url1 = "http://www.xxx.com/login?"  # 用于创建一个完整的url
        new_url = url1 + self.query
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))  # 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        info = RunMain().run_main(self.method, url, data1)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)  # 将响应转换为字典格式

        if self.case_name == 'login':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], 200)
        if self.case_name == 'login_error':  # 同上
            self.assertEqual(ss['code'], -1)
        if self.case_name == 'login_null':  # 同上
            self.assertEqual(ss['code'], 10001)