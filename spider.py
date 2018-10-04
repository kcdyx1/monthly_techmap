##
# @Author: KangChen
# @Date: 2018-09-29 23:21:12
# @LastEditors: KangChen
# @LastEditTime: 2018-09-29 23:21:12
# @FindMe: https://github.com/kcdyx1
##


import requests
from pyquery import PyQuery as pq
import datetime
import json
import re
from urls import aug_urls


def get_wxwenzhang(url):
    # 获取微信公众号文章
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        return r.text
    except:
        print(url + ' 获取失败!')


def get_neirong(pageSource):
    # 先用正则表达式去掉“style=...”
    doc = re.sub('style="[^\"]*?"', '', pageSource)
    # 生成PyQuery对象
    doc = pq(doc)
    # 找到文章的主体
    body = doc('#js_content')
    if body == '':
        print("$^$错误！！！")
    else:
        body = body.text().split('\n')
    return body


def clean_data(dirty_data):
    useless = ['关注全球技术地图', '获取科技前沿动态', '-END-',
               '由国际技术经济研究所整编', '由国际技术经济研究所整编', '转载请注明']
    clean = []
    for i in useless:
        if i in dirty_data:
            dirty_data.remove(i)
            continue
        else:
            continue

    for i in range(dirty_data.count('')):
        dirty_data.remove('')
    for i in dirty_data:
        clean.append(i.strip())

    return clean


def data_fenlei(cleandata):
    fields = ["科技战略", "信息", "生物", "能源", "航空", "航天", "海洋", "新材料", "先进制造"]
    today_fields = []
    fields_index = []
    for i in fields:
        if i in cleandata:
            today_fields.append(i)
            continue
        else:
            continue
    for i in today_fields:
        fields_index.append(cleandata.index(i))
    fields_index.append(len(cleandata))
    # 因为每天不一定按固定顺序排版，所以需要排序一下
    fields_index.sort()
    # print(fields_index)
    # print(today_fields)
    for i in fields_index:
        if i == 0:
            j = i
            continue
        else:
            yield cleandata[j:i]
            j = i


def main():
    # 程序主入口
    for u in aug_urls:
        # 注意选择相应的URL列表
        ps = get_wxwenzhang(u)
        nr = get_neirong(ps)
        ganjingdata = clean_data(nr)
        jieguo = data_fenlei(ganjingdata)
        for j in jieguo:
            for x in range(1, len(j) - 1, 2):
                print(j[0] + "|" + j[x] + "|" + j[x + 1])


# \u636e.{0, }[, ']?\u6d88\u606f
# \d\u6708\d{1, 2}\u65e5
# "\u636e[^,']{0,}\u6d88\u606f"

if __name__ == '__main__':
    main()
