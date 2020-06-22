# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:15:03 2020

@author: 6989
"""

import pandas as pd
# 讀取資料
data = pd.read_csv("googleplaystore.csv") # 把 CSV 格式的檔案讀取成一個 DataFrame
# 觀察資料
print("資料數量:", data.shape) 
print("資料欄位:", data.columns)
print("============================")

# 分析資料 : 評分的各種統計數據
# =============================================================================
# condition = data["Rating"] > 5 # 資料清理，把評分大於 5 分的資料清理掉
# err = data[condition]
# print(err)
# 
# condition = data["Rating"] <= 5
# data = data[condition]
# 
# print("評分平均數:", data["Rating"].mean())
# print("中位數:", data["Rating"].median())
# print("取得前一千個應用程式的平均:", data["Rating"].nlargest(1000).mean())
# =============================================================================

# 分析資料 : 安裝數量的各種統計數據
#print(data["Installs"])
# =============================================================================
# print(data["Installs"][10472]) # 這一筆的資料不乾淨，維 free ，要處理掉
# 
# data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))
# print("下載平均數:", data["Installs"].mean())
# condition = data["Installs"] > 100000
# print("安裝數量大於100000的應用程式:", data[condition].shape[0])
# =============================================================================

# 基於資料的應用 : 關鍵字搜尋應用程式名稱
keyword = input("請輸入關鍵字:")
condition = data["App"].str.contains(keyword, case = False) # case 忽略大小寫
print(data[condition]["App"])

print("包含關鍵字的應用程式數量:", data[condition].shape[0])
