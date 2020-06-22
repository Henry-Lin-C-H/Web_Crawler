# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:25:03 2020

@author: 6989
"""

import pandas as pd

# 資料索引
data = pd.DataFrame({
        "Name":["Amy", "Bob", "Charles"],
        "Salary":[30000, 50000, 40000]
        },
        index = ["a", "b", "c"])
print(data)

# 觀察資料
# =============================================================================
# print("資料數量:", data.size)
# print("資料形狀:", data.shape)
# print("資料索引:", data.index)
# =============================================================================

# 取得列(Row/橫向) 的 Series 資料
# =============================================================================
# print("取得第二列:", data.iloc[1], sep="\n")
# print("====================")
# print("取得第c列:", data.loc["c"], sep="\n")
# =============================================================================

# 取得蘭 (Column/直向) 的 Series 資料
# =============================================================================
# print("取得name欄位", data["Name"], sep = "\n")
# names = data["Name"] # 取得單維度的 Series 資料
# print("把 name 全部變大寫", names.str.upper(), sep = "\n")
# 
# # 計算薪水的平均值
# salaries = data["Salary"]
# print("薪水的平均值", salaries.mean())
# =============================================================================

# 建立新的欄位
data["revenue"] = [50000, 40000, 30000]
data["rank"] = pd.Series([3,6,1], index=["a", "b", "c"])

data["cp"] = data["revenue"] - data["Salary"]


print(data)