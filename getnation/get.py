'''
 * @Author: KangChen
 * @Date: 2018-10-16 14:05:22
 * @LastEditors: KangChen
 * @LastEditTime: 2018-10-16 14:06:58
 * @FindMe: https://github.com/kcdyx1
'''

import jieba
from functools import reduce
# from need_list import nation_list, us_kw, uk_kw, cn_kw, jp_kw, ru_kw, kr_kw, ge_kw


# 世界国家列表，约252个
nation_list = ['阿富汗',
               '奥兰群岛',
               '阿尔巴尼亚',
               '阿尔及利亚',
               '美属萨摩亚',
               '安道尔',
               '安哥拉',
               '安圭拉',
               '安提瓜和巴布达', '阿根廷', '亚美尼亚', '阿鲁巴', '澳大利亚', '奥地利', '阿塞拜疆', '孟加拉', '巴林', '巴哈马', '巴巴多斯', '白俄罗斯', '比利时', '伯利兹', '贝宁', '百慕大', '不丹', '玻利维亚', '波斯尼亚和黑塞哥维那', '博茨瓦纳', '布维岛', '巴西', '文莱', '保加利亚', '布基纳法索', '布隆迪', '柬埔寨', '喀麦隆', '加拿大', '佛得角', '中非', '乍得', '智利', '圣诞岛', '科科斯（基林）群岛', '哥伦比亚', '科摩罗', '刚果（金）', '刚果', '库克群岛', '哥斯达黎加', '科特迪瓦', '中国', '克罗地亚', '古巴', '捷克', '塞浦路斯', '丹麦', '吉布提', '多米尼加', '东帝汶', '厄瓜多尔', '埃及', '赤道几内亚', '厄立特里亚', '爱沙尼亚', '埃塞俄比亚', '法罗群岛', '斐济', '芬兰', '法国', '法国大都会', '法属圭亚那', '法属波利尼西亚', '加蓬', '冈比亚', '格鲁吉亚', '德国', '加纳', '直布罗陀', '希腊', '格林纳达', '瓜德罗普岛', '关岛', '危地马拉', '根西岛', '几内亚比绍', '几内亚', '圭亚那', '海地', '洪都拉斯', '匈牙利', '冰岛', '印度', '印度尼西亚', '印尼', '伊朗', '伊拉克', '爱尔兰', '马恩岛', '以色列', '意大利', '牙买加', '日本', '泽西岛', '约旦', '哈萨克斯坦', '肯尼亚', '基里巴斯', '韩国', '朝鲜', '科威特', '吉尔吉斯斯坦', '老挝', '拉脱维亚', '黎巴嫩', '莱索托',
               '利比里亚', '利比亚', '列支敦士登', '立陶宛', '卢森堡', '马其顿', '马拉维', '马来西亚', '马达加斯加', '马尔代夫', '马里', '马耳他', '马绍尔群岛', '马提尼克岛', '毛里塔尼亚', '毛里求斯', '马约特', '墨西哥', '密克罗尼西亚', '摩尔多瓦', '摩纳哥', '蒙古', '黑山', '蒙特塞拉特', '摩洛哥', '莫桑比克', '缅甸', '纳米比亚', '瑙鲁', '尼泊尔', '荷兰', '新喀里多尼亚', '新西兰', '尼加拉瓜', '尼日尔', '尼日利亚', '纽埃', '诺福克岛', '挪威', '阿曼', '巴基斯坦', '帕劳', '巴勒斯坦', '巴拿马', '巴布亚新几内亚', '秘鲁', '菲律宾', '皮特凯恩群岛', '波兰', '葡萄牙', '波多黎各', '卡塔尔', '留尼汪岛', '罗马尼亚', '卢旺达', '俄罗斯', '圣赫勒拿', '圣基茨和尼维斯', '圣卢西亚', '圣文森特和格林纳丁斯', '萨尔瓦多', '萨摩亚', '圣马力诺', '圣多美和普林西比', '沙特阿拉伯', '塞内加尔', '塞舌尔', '塞拉利昂', '新加坡', '塞尔维亚', '斯洛伐克', '斯洛文尼亚', '所罗门群岛', '索马里', '南非', '西班牙', '斯里兰卡', '苏丹', '苏里南', '斯威士兰', '瑞典', '瑞士', '叙利亚', '塔吉克斯坦', '坦桑尼亚', '泰国', '特立尼达和多巴哥', '多哥', '托克劳', '汤加', '突尼斯', '土耳其', '土库曼斯坦', '图瓦卢', '乌干达', '乌克兰', '阿拉伯联合酋长国', '英国', '美国', '乌拉圭', '乌兹别克斯坦', '瓦努阿图', '梵蒂冈', '委内瑞拉', '越南', '瓦利斯群岛和富图纳群岛', '西撒哈拉', '也门', '南斯拉夫', '赞比亚', '津巴布韦', '欧洲', '欧盟', '联合国']


# 美国
us_kw = ['特朗普', '白宫', '谷歌', '脸书', '推特', '微软', 'Facebook', 'SpaceX', 'Nvidia', 'nvidia', 'IARPA', 'DARPA', 'NASA', 'DHS', '兰德', '麦肯锡', '赛门铁克', '康涅狄格州', 'CSIS', '亚马逊', '加利福尼亚州',
         '兰德公司', '布鲁金斯', '布鲁金斯学会', '纽约', '华盛顿', '莱斯', '哈佛', '哈佛大学', '麻省理工', '麻省理工学院', '高通', '英特尔', '贝尔', '贝尔公司', '苹果', 'IBM', '特斯拉', '美海军', '加州', '诺格', '波音', '明尼苏达', '美军', '宾夕法尼亚', '宾夕法尼亚', '通用']


# 俄罗斯
ru_kw = ['普京', '俄联邦']

# 英国
uk_kw = ['BP', 'BAE', '罗罗', '罗尔斯', '罗伊斯', '曼彻斯特大学']

# 德国
ge_kw = ['西门子', '大众', '德累斯顿', '巴斯夫']

# 中国
cn_kw = ['中科院', '北大', '清华', '南开', '北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西',
         '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆', '台湾', '香港', '澳门']

# 日本
jp_kw = ['丰田', '本田', '东京']

# 韩国
kr_kw = ['三星', '蔚山', '文在寅']

#国际
in_kw = ['世界', '世界卫生组织', '达沃斯']

us_pattern = r'\u7f8e\u56fd'  # 美国
cn_pattern = r'\u4e2d\u56fd'  # 中国
eu_pattern = r'\u6b27[\u76df|\u6d32]?'  # 欧盟
uk_pattern = r'\u82f1\u56fd'  # 英国
fr_pattern = r'\u6cd5\u56fd'  # 法国
ge_pattern = r'\u5fb7\u56fd'  # 德国
ca_pattern = r'\u52a0\u62ff\u5927'  # 加拿大
au_pattern = r'\u6fb3\u5927\u5229\u4e9a'  # 澳大利亚
jp_pattern = r'\u65e5\u672c'  # 日本
kr_pattern = r'\u97e9\u56fd'  # 韩国
ru_pattern = r'\u4fc4\u7f57\u65af'  # 俄罗斯
id_pattern = r'\u5370\u5ea6'  # 印度
is_pattern = r'\u4ee5\u8272\u5217'  # 以色列
in_pattern = r'\u56fd\u9645|\u8054\u5408\u56fd'  # 国际


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
