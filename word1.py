# konlpy
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype
# https://www.lfd.uci.edu/~gohlke/pythonlibs
# wordcloud‑1.8.1‑cp36‑cp36m‑win_amd64.whl
# (venv) D:\study\pj5>pip install wordcloud-1.8.1-cp36-cp36m-win_amd64.whl
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# data=open('data\\alice.txt').read()
# print(data)
# # wc=WordCloud().generate(data)
# wc=WordCloud(background_color='white',max_words=2000).generate(data)
# plt.imshow(wc)
# plt.axis('off')
# plt.show()
# 마스크 적용-----
# from PIL import Image
# import numpy as np
# img=Image.open('img\\two.png')
# mask=np.array(img)
# print(mask)
# data=open('data\\alice.txt').read()
# wc=WordCloud(mask=mask,background_color='white').generate(data)
# plt.imshow(wc)
# plt.axis('off')
# plt.show()
# stopword--------
from PIL import Image
from wordcloud import STOPWORDS
import numpy as np
print(STOPWORDS)
sw=STOPWORDS
print(len(sw))
sw.add('said')
print(len(sw))
img=Image.open('img/one.png')
mask=np.array(img)
print(mask)
data=open('data\\alice.txt').read().lower()
wc=WordCloud(mask=mask,stopwords=sw).generate(data)
plt.imshow(wc)
plt.axis('off')
plt.show()
