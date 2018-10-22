from getnation import main as gn
import pandas as pd
# import matplotlib.pyplot as plt
# import imageio
# from wordcloud import WordCloud
# import jieba
# import jieba.analyse

d = pd.read_csv('../1808/8yue_all.csv', sep='|', header=0)
# print(d.describe())

def write_file(jieguo):
    with open('./fenxi.txt', 'a') as f:
        f.write(str(jieguo) + '\n')

for i in d['content_clean']:
    jieguo = gn(i)
    write_file(jieguo)