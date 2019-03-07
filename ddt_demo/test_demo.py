import unittest
from ddt import ddt, data, unpack
'''
在测试类上使用@ddt装饰符
测试方法上使用@data@unpack装饰符:解压，解包
@data装饰符把参数当作测试数据，参数可以是单个值,二个值、列表、元组、字典。
'''


@ddt
class TestDemo(unittest.TestCase):
    @unittest.skip
    @data('你好', '你', '我')
    def test_ddt_demo(self, value):
        print(value)
        self.assertEqual('你', value)

    @unittest.skip
    @data((1, 2), (2, 3))
    @unpack
    def test_ddt_demo_two(self, value1, value2):
        print(value1, value2)
        self.assertEqual(value1+1, value2)

    @unittest.skip
    @data([1, 2], [2, 3])
    @unpack
    def test_ddt_demo_three(self, value1, value2):
        print(value1, value2)
        self.assertEqual(value1+1, value2)

    @data({'first': 1, 'cond': 2}, {'first': 4, 'cond': 8})
    @unpack
    def test_ddt_demo_four_dict(self, first, cond):
        print(first, cond)
        self.assertTrue(first < cond)


if __name__ == '__main__':
    unittest.main()

