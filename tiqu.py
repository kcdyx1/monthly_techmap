##----------
# @Author: KangChen
# @Date: 2018-10-04 11:19:08
# @LastEditors: KangChen
# @LastEditTime: 2018-10-04 11:19:08
# @Description:
# @FindMe: https://github.com/kcdyx1
##----------

import re


def get_first_sen(neirong):
    # print(neirong)
    res = re.search(r"^\u636e[^,']{0,}\u6d88\u606f", neirong, re.U)
    if res == None:
        pass
    else:
        return res.group()


def get_date(fsen):
    res = re.search(r"\d\u6708\d+\u65e5", fsen)
    if res == None:
        res = re.search(
            r"^\u636e[^,']*([\u8fd1][\u65e5]|[\u8fd1][\u671f])\u6d88\u606f", fsen)
        if res == None:
            return 'None'
        else:
            return res.group(1)
    else:
        return res.group()


def get_source(fsen):
    res = re.search(
        r"^\u636e([^,']*)\d\u6708\d+\u65e5\u6d88\u606f", fsen, re.U)
    if res == None:
        res = re.search(
            r"^\u636e([^,']*[\u7f51])|([^,']*[\u62a5]).*\u6d88\u606f", fsen, re.U)
        if res == None:
            return 'None'
        else:
            return res.group(1)
        return res.group(1)
    else:
        res1 = res.group(1)
        res1 = res1.strip(" ").replace("《", "").replace("》", "")
        # 统一OFweek网
        res1 = re.sub(r"[oO]F[wW]eek[^，,]*[\u7f51]?[\u7ad9]?", "OFweek网", res1)
        # 统一Phys.org网
        res1 = re.sub(r"[pP]hys(\.org)?[\u7f51]?[\u7ad9]?", "Phys.org网", res1)
        # 统一生物谷网
        res1 = re.sub(r"\u751f\u7269\u8c37[\u7f51]?[\u7ad9]?", "生物谷网", res1)
        # 统一EurekAlert网
        res1 = re.sub(r"[eE]urek[aA]lert[\u7f51]?[\u7ad9]?",
                      "EurekAlert网", res1)
        # 统一cnBeta网
        res1 = re.sub(r"[cC]n[bB]eta[\u7f51]?[\u7ad9]?", "cnBeta网", res1)
        # 统一ScienceDaily网
        res1 = re.sub(
            r"[sS]cience[\s]?[dD]aily[\u7f51]?[\u7ad9]?", "ScienceDaily网", res1)
        return res1


def main(month):
    shuxian = "|"
    with open('./1808/r_aug.txt', 'r') as fj:
        lines = fj.readlines()
        print("title|content|field|source|date|content_clean")
        for line in lines:
            line = line.replace(',', '，').replace(" ", "").replace(
                '\n', '').replace("'", "").split('|')
            fs = get_first_sen(line[2])
            date = get_date(fs)
            sou = get_source(fs)
            line.append(sou)
            line.append(date)
            a = len(fs) + 1
            thisone = [line[1], line[2], line[0],
                       line[3], line[4], line[2][a:]]
            if len(thisone[4]) >= 3:
                yuefen = re.search(r"(\d)\u6708(\d+)\u65e5", thisone[4])
                if int(yuefen.group(1)) == month:
                    print(shuxian.join(thisone))
            else:
                print(shuxian.join(thisone))


if __name__ == '__main__':
    main(8)

# 测试用代码
# a = "据Phys网8月1日消息，日本财务省于8月31日截止了各省厅2019年度的预算申请，"
# b = get_source(a)
# c = get_date(a)
# print(b, c)
