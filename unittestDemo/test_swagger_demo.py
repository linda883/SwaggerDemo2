import unittest
import requests
import json
from HTMLTestRunner import HTMLTestRunner
# pip3 install requests 如果本地没有这个库，第三方库，你需要从别的地方导过来。


class TestSwaggerDemo(unittest.TestCase):
    def setUp(self):
        self.url2 = 'https://petstore.swagger.io/v2/pet'
        self.data = {
                      "id": 88,
                      "category": {
                        "id": 0,
                        "name": "string"
                      },
                      "name": "diudiu",
                      "photoUrls": [
                        "string"
                      ],
                      "tags": [
                        {
                          "id": 0,
                          "name": "string"
                        }
                      ],
                      "status": "available"
                    }

    def test_swagger_get_pet_by_id(self):
        # 发请求，通过id获得一个宠物
        result = requests.get('https://petstore.swagger.io/v2/pet/8')
        # print(result.json())
        res_data = result.json()
        # print(json.dumps(res_data, indent=2))
        # print(res['id'])
        # 1协议层断言，响应状态码是否是200，200代表成功，前面参数一般预期结果，后面是实际结果
        self.assertEqual(200, result.status_code)
        # 2业务数据层
        self.assertEqual(8, res_data['id'])
        # print(res_data['tags'][0]['name'])
        self.assertEqual('tag2', res_data['tags'][0]['name'])
        # 断言响应在2秒之内2>=实际
        self.assertGreaterEqual(2, result.elapsed.total_seconds())

    def test_swagger_post_add_pet(self):
        # data 通过参数json=将数据转成json格式发送
        result = requests.post(url=self.url2, json=self.data)
        res_data = result.json()
        self.assertEqual(200, result.status_code)
        print(res_data)
        self.assertEqual(88, res_data['id'])
        self.assertGreaterEqual(2, result.elapsed.total_seconds())


if __name__ == '__main__':
    # unittest.main()
    # 建立一个套件
    suite = unittest.TestSuite()
    file_path = 'html_report.html'
    # 写报告

    with open(file_path, 'wb') as f:
        # 测试用例加到套件中
        suite.addTest(unittest.makeSuite(TestSwaggerDemo))
        # suite.addTest(TestSwaggerDemo('test_swagger_post_add_pet'))
        # stream 流--文件
        runner = HTMLTestRunner(stream=f, verbosity=1,
                                title='swagger pet 测试报告', description='get/post测试用例')
        runner.run(suite)
    f.close()

