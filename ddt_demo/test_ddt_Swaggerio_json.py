import unittest
from ddt import ddt, file_data, unpack
import requests

@ddt
class TestSwaggerDdtFile(unittest.TestCase):
    def setUp(self):
        self.url = 'https://petstore.swagger.io/v2/pet'

    @file_data('test_data.json')
    def test_ddt_json_post_add_pet(self, **test_data):
        # print(test_data)
        # 这是从json文件中取出来的值
        self.id_exp = test_data.get('id')
        # print(type(test_data))
        result = requests.post(url=self.url, json=test_data)
        self.assertEqual(200, result.status_code)
        # print(result.json())
        # 从响应的json格式中取的id
        self.id_a = result.json()['id']
        self.assertEqual(self.id_exp, self.id_a)


if __name__ == '__main__':
    unittest.main()

