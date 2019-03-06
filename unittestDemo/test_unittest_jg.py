import unittest


class TestSwagger(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("在整个类之前执行的。\n")

    @classmethod
    def tearDownClass(cls):
        print("在整个类之后执行的")

    def setUp(self):
        print("这是每个方法前执行的，一般做数据准备")

    def tearDown(self):
        print("这是每个测试方法后执行的，一般做数据清理")

    def test_Swagger(self):
        print("测试1")
        self.assertEqual(1, 1)

    def test_Swagger_2(self):
        print("测试2")
        self.assertEqual(1, 6)


if __name__ == '__main__':
    unittest.main()
