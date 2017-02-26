import requests
from bs4 import BeautifulSoup
from collections import Counter
import time

res = requests.get("http://www.appledaily.com.tw/realtimenews/section/new/")
soup = BeautifulSoup(res.text)
count = 1
domain = "http://www.appledaily.com.tw"
s = []

print("==============Breaking News===================")
print("時間   類別            標題                (點閱人數)   ")
for news in soup.select('.rtddt'):
    print("[%d]"%(count), news.select('time')[0].text, news.select('h2')[0].text, news.select('h1')[0].text)
    print(domain + news.select('a')[0]['href'])
    print()
    count += 1
    s.append(news.select('h2')[0].text)
    time.sleep(0.5)
    
word_counts = Counter(s)
top1 = word_counts.most_common(1)
count -= 1

print("共有: %d 新聞"%count)
print("其中", top1[0][0], "類新聞最多，有",top1[0][1], "則" ) 

