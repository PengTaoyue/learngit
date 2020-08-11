import requests
import unittest
from Commonlib.ReadExc import ReadEx
class Test_Tq(unittest.TestCase):
    def setUp(self):
        print("开始")

    def tearDown(self) :
        print("结束")

    def test01(self):
        readxcel = ReadEx()
        data = readxcel.read_excel()

        for i in data:
            #给接口地址定义变量名称
            url = "http://v.juhe.cn/historyWeather/province"
            para = {"province": i["province"], "key": i["key"]}
            # 发送请求
            r = requests.get(url, params=para)
            print(r.status_code)
            res = r.json()
            self.assertEqual(res["reason"], i["reason"])

if __name__=='__main__':
    unittest.main()