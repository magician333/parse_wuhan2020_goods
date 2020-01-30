

import json
import re
import time

temp_dict = dict()
info = """    武汉加油！！！
-物资解析器-
-purplefire 紫火-
---输入格式分隔为;；，、:： 格式为：数字*物品---
---模式切换请设置---"""


def main(kinds, text):
    with open(time.strftime('%H-%M-%S', time.localtime(time.time()))+".json", "w", encoding="utf-8") as output_file:

        for i in items.split(";，、；：:"):
            # 格式 物资 数量 如n95口罩 3000
            if kinds == 1:
                goods, num = i.split(" ")
            # 格式 数量*物资 如3000*n95口罩
            elif kinds == 2:
                print(i.split("*"))
                num, goods = i.split("*")
            # 格式 物资*数量 如n95口罩*3000
            elif kinds == 3:
                goods, num = i.split("*")

            goods = re.sub(u"（.*）", "", goods)
            temp_dict[goods.strip()] = int(num)

        output_file.write(json.dumps([temp_dict], ensure_ascii=False))


if __name__ == '__main__':
    while True:
        try:
            print(info)
            items = input("输入需要解析的数据：")
            # 此处设置模式，默认模式2
            main(2, items)
            print("\n--------解析完成--------\n\n\n")
        except KeyboardInterrupt:
            print("\n--------感谢使用--------\n")
            exit()
