# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:16:06 2020

@author: 6989
"""

#抓取PTT八卦版標題網頁原始碼 (HTML)
import urllib.request as req
def getData(url):    

    # 建立一個 request 物件，附加 request headers 的資訊
    request = req.Request(url, headers={
            "cookie":"over18=1", # 將已滿 18 歲的 cookie 代入
            "user-agent":"mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/80.0.3987.163 safari/537.36"
            })
    
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    #print(data)
    
    # 解析原始碼，取得每篇文章的標題
    # 要先安裝 beautifulsoup4   打開python或 visualstudiocode 寫入 pip install beautifulsoup4
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    #print(root.title.string)
    
    titles = root.find_all("div", class_ = "title") # 尋找 class = "title" 的 div 標籤
    for title in titles:
        if title.a != None: # 如果標題包含 a 標籤 (沒有被刪除) print出來
            print(title.a.string)
            
    # 抓取上一頁的連結
    nextlink = root.find("a", string = "‹ 上頁") # 找到內文是 ‹ 上頁 的 a 標籤
#    print(nextlink["href"])
    return nextlink["href"]

# 抓取一個頁面的標題
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"

count = 0
while count < 3:
    pageURL = "https://www.ptt.cc"+getData(pageURL)    
    count += 1
