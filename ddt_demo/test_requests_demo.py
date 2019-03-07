import unittest
import requests
# pip install requests


class TestRequestDemo(unittest.TestCase):

    def test_demo_get(self):
        result = requests.get('https://petstore.swagger.io/v2/pet/8')
        print(result.json())
        print(result.cookies)
        print(result.headers.get('Content-Type'))
        print(result.text)
        print(result.elapsed.total_seconds())
        print(result.encoding)
        print(result.status_code)
        print(result.url)


if __name__ == '__main__':
    unittest.main()
