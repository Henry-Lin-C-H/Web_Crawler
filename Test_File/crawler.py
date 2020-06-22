# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:48:23 2020

@author: 6989
"""

#抓取PTT電影版標題網頁原始碼 (HTML)
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"

# 建立一個 Request 物件，附加 Request Headers 的資訊
request = req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
        })

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
#print(data)

# 解析原始碼，取得每篇文章的標題
# 要先安裝 BeautifulSoup4   打開Python或 VisualStudioCode 寫入 pip install beautifulsoup4
import bs4
root = bs4.BeautifulSoup(data, "html.parser")
#print(root.title.string)

titles = root.find_all("div", class_ = "title") # 尋找 class = "title" 的 div 標籤
for title in titles:
    if title.a != None: # 如果標題包含 a 標籤 (沒有被刪除) print出來
        print(title.a.string)
