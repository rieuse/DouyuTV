# 抓取弹幕后保存为text文档，然后词云分析,此部分是词云部分
__author__ = '布咯咯_rieuse'
__time__ = '2017.6.2'
__github__ = 'https://github.com/rieuse'


import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy.misc import imread

with open('大司马即将上课前后.txt','r',encoding='utf-8') as f:
    text = f.read()

cut_text = " ".join(jieba.cut(text))
color_mask = imread("2.png")
cloud = WordCloud(
    font_path="FZLTKHK--GBK1-0.ttf",
    background_color='MistyRose',
    mask=color_mask,
    max_words=4000,
    font_step=5, #步调太大，显示的词语就少了
    min_font_size=20,
    max_font_size=180
)
wordcloud = cloud.generate(cut_text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()