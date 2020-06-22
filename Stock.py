# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 15:46:44 2020

@author: 6989
"""

import datetime
year = datetime.datetime.today().year
month = datetime.datetime.today().month
day = datetime.datetime.today().day
hour = datetime.datetime.today().hour
minute = datetime.datetime.today().minute
date = f'{year}_{month}_{day}'

stockNo = []
stockName = []
import csv
with open("選股標的.csv", newline='') as csvfile:
    designedStock = csv.DictReader(csvfile)
    for row in designedStock:
        stockNo.append(row["編號"])
        stockName.append(row["名稱"])
#        print(row["編號"], row["名稱"])

import urllib.request as req
import bs4
import openpyxl as xl
import pandas as pd
for no in range(len(stockNo)):
    #抓取股票資料 (HTML)    
#    url = f'https://tw.stock.yahoo.com/q/ts?s={stockNo[no]}'
    url = f'https://tw.stock.yahoo.com/q/ts?s={stockNo[no]}&t=50'
    
    # 建立一個 Request 物件，附加 Request Headers 的資訊
    request = req.Request(url, headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
            })
    
    with req.urlopen(request) as response:
        data = response.read()
    #    data = response.read().decode("utf-8")
    #print(data)
    
    # 解析原始碼，取得每篇文章的標題
    # 要先安裝 BeautifulSoup4   打開Python或 VisualStudioCode 寫入 pip install beautifulsoup4
    
    root = bs4.BeautifulSoup(data, "html.parser")
    #print(root.title.string)
    
    # =============================================================================
    # tds = root.find_all("td", class_="high")
    # #tds = root.find_all("td")
    # for td in tds:
    #     print(td.string)
    # =============================================================================
    
    trs = root.find_all("tr", align="center", bgcolor="#ffffff", height="25")
    
    time = []
    quantity = []          
    for td in trs:
        time.append(td.find_all("td")[0].string)
        quantity.append(td.find_all("td")[6].string)
    
    
    data = pd.DataFrame({
            "Time":time,
            "Quantity":quantity
            }) #股票爬蟲抓下來的時間與量
#    print(data)
           
    inputHour = ["09", "10", "11", "12", "13"]
    inputMinu = ["00", "05", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"]
    allTime = [] #全部的時間
    for i in inputHour:
        for j in inputMinu:
            if i == "13" and j == "35":
                break
            elif i == "09" and j == "00":
                continue                
            else:
                allTime.append(str(i)+":"+str(j))
    #print(time)
    
    check = []
    inputTime = [] # 輸入時間
    for i in data["Time"]:
        if i in allTime:
            check.append(True)
            inputTime.append(i + ":00")
        else:
            check.append(False)
    
    del inputTime[-1]
    
    data["Calculate"] = check #確認需要計算的區間
#    print(data)
    
    calQuan = 0 # 計算量
    firstBool = True # 第一個量判斷用
    inputQuan = [] # 輸入的量
    for i in data.index:
        if check[i] == False and firstBool == True:
            continue
        elif check[i] == True:
            if firstBool == True:
                calQuan += int(quantity[i])
                firstBool = False
            else:
                inputQuan.append(calQuan)            
                calQuan = 0
                calQuan += int(quantity[i])
        elif data["Time"][i] == "09:01":
            calQuan += int(quantity[i])
            inputTime.append("09:05:00")
            inputQuan.append(calQuan)
            calQuan = 0
        else:
            calQuan += int(quantity[i])
         
    inputTime.reverse()
    inputQuan.reverse()
#    print(inputTime, inputQuan)
            
    
    
    
    #from openpyxl import load_workbook
    try:
        wb = xl.load_workbook(f'預估成交量-阿信_{date}.xlsx')
    except:
        wb = xl.load_workbook("預估成交量-阿信.xlsx")
    try:
        ws = wb[stockNo[no]]
    except:        
        ws = wb.copy_worksheet(wb["計算表"])
        ws.cell(row = 1, column = 11).value = stockNo[no]
        ws.cell(row = 1, column = 13).value = stockName[no]
        ws.title = str(stockNo[no])
    
    
    
    inputCount = 0
    for i in range(1,60):
        if str(ws.cell(row = i, column = 1).value) in inputTime:
            ws.cell(row = i, column = 3).value = inputQuan[inputCount]
            inputCount += 1
    wb.save(f'預估成交量-阿信_{date}.xlsx')
    
    
import tkinter as tk
import os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

pathDesktop = f'{desktop}\\預估量_{date}.xlsx'
try:
    wb.save(pathDesktop)
    print(f'{date}-{hour}:{minute}_更新完成')
except:
    window = tk.Tk()
    window.title("Stock")
    window.geometry("300x100+250+250")
    label = tk.Label(window, text = "Excel檔案開著，桌面檔案無法更新")
    label.pack()
    window.mainloop()
    


# =============================================================================
# b8 = ws.cell(row=8, column=2)
# #b1 = ws["B1"]
# print(b8.value)
# =============================================================================




# =============================================================================
# titles = root.find_all("div", class_ = "title") # 尋找 class = "title" 的 div 標籤
# for title in titles:
#     if title.a != None: # 如果標題包含 a 標籤 (沒有被刪除) print出來
#         print(title.a.string)
# =============================================================================
