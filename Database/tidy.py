##----------
# @Author: KangChen
# @Date: 2018-10-08 16:47:29
# @LastEditors: KangChen
# @LastEditTime: 2018-10-08 16:47:29
# @Description: 
# @FindMe: https://github.com/kcdyx1
##----------


import re

with open('./documents_20181008.txt') as f:
    lines = f.readlines()
# print(lines[:10])

for line in lines:
    pr = re.compile("[\u8d44\u6599\u6d88\u606f]{0,2}[\u6765\u6e90：]{0,3}[a-zA-z]+://[^\s]*[\|]")
    line = re.sub(pr, '|', line)
print(line[5555:5558])
