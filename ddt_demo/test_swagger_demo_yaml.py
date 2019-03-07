import unittest
from ddt import ddt, file_data, unpack
import requests


@ddt
class TestSwaggerDdtFileYaml(unittest.TestCase):
    @file_data('test_data.yaml')
    def test_ddt_json_post_add_pet(self, **test_data):
        self.url = test_data.get('url')
        self.method = test_data.get('method')
        self.data = test_data.get('payload')
        self.ok = test_data.get('validate')
        result = requests.request(method=self.method, url=self.url, data=self.data)
        self.assertEqual(200,result.status_code)


if __name__ == '__main__':
    unittest.main()

