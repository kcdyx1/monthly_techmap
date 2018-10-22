/*
 * @Author: KangChen
 * @Date: 2018-10-16 14:05:22
 * @LastEditors: KangChen
 * @LastEditTime: 2018-10-16 14:06:58
 * @FindMe: https://github.com/kcdyx1
 */

import jieba
from functools import reduce
from need_list import nation_list, us_kw, uk_kw, cn_kw, jp_kw, ru_kw, kr_kw, ge_kw


def fenci(wenben):
    '''
    采用全模式分词，粒度更细
    :wenben: 待分词的文本
    :returns: 分词列表
    '''
    seg_list = jieba.lcut_for_search(wenben)
    return seg_list


def get_nation_d(fenci_list):
    '''
    直接获取国家名称
    :fenci_list: list
    :nas: list
    '''
    head = fenci_list[:15]
    nas = []
    # print(head)
    for i in head:
        if i in nation_list and i not in nas:
            nas.append(i)
    return nas


def get_nation_ind(fenci_list):
    '''
    在没有直接出现国家名称时，用某些关键词来推断，并分类

    '''
    nas = []
    for i in fenci_list[:3]:
        if i == '美':
            nas.append('美国')
        if i == '中':
            nas.append('中国')
        if i == '英':
            nas.append('英国')
        if i == '法':
            nas.append('法国')
        if i == '俄':
            nas.append('俄罗斯')
        if i == '澳':
            nas.append('澳大利亚')
        if i == '德':
            nas.append('德国')
    if nas:
        return nas
    else:
        for i in fenci_list[:30]:
            if i in us_kw:
                nas.append('美国')
            if i in cn_kw:
                nas.append('中国')
            if i in ru_kw:
                nas.append('俄罗斯')
            if i in uk_kw:
                nas.append('英国')
            if i in jp_kw:
                nas.append('日本')
            if i in kr_kw:
                nas.append('韩国')
            if i in ge_kw:
                nas.append('德国')
        return nas

def manual(kw_list):
    print(kw_list[:30])
    nas = [input("请根据关键词输入国别: \n")]
    if nas:
        return nas


def foo(text):
    '''
    国家提取入口，先做分词，
    然后用关键词直接提取，
    不行就用规则，
    再不行就手动输入！
    '''
    res = fenci(text)
    zhijie = get_nation_d(res)
    if zhijie:
        pullout = zhijie
    else:
        jianjie = get_nation_ind(res)
        if jianjie:
            pullout = jianjie
        else:
            pullout = manual(res)
    
    # 对列表进行去重，用reduce函数，必须用"from functools import reduce"导入
    pullout = reduce(lambda x, y: x if y in x else x + [y], [[], ] + pullout)
    return pullout

# if __name__ == '__main__':
#     aha('中国')
