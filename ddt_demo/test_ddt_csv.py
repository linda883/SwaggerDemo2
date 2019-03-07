import unittest
import csv
import requests
from ddt import ddt, data, unpack, feed_data
import json

def get_data(file_name):
    # 创建一个列表,保存读过来的数据
    rows = []
    # 打开一个csv文件，文件名通过参数传进来
    data_file = open(file_name, 'r')
    # 建立一个csv的读的工具，将文件读进来
    reader = csv.reader(data_file)
    # 跳过第一行的头，头有格式信息，这个头可以是参数名
    next(reader, None)
    # 将reader中的东西读到row中，循环多次
    for row in reader:
        # 将每个row的东西追加到此前定义
        rows.append(row)
    # rows列表中
    return rows


@ddt
class TestSwaggerDdtCsv(unittest.TestCase):
    @unpack
    @data(*get_data('test_data_one.csv'))
    def test_post_pet_csv(self, value1):
        print(value1)


if __name__ == '__main__':
    unittest.main()


