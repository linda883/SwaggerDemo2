# http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
import unittest
import requests
from ddt import ddt, file_data, unpack
import yaml


@ddt
class TestSwaggerDdt(unittest.TestCase):

    @file_data('test_data.yaml')
    @unpack
    def test_post_pet(self, **kwargs):

        url = kwargs.get("url")
        method = kwargs.get("method")
        header = kwargs.get("hearder")['Content-Type']
        data = kwargs.get("payload")
        ok = kwargs.get("validate")

        print(url, method, data, ok, type(data),header)
        if header == 'application/json':
            res = requests.request(method=method, url=url, json=data, )
        else:
            res = requests.request(method=method, url=url, data=data, )
        self.assertEqual(200, res.status_code)


if __name__ == '__main__':
    unittest.main()



