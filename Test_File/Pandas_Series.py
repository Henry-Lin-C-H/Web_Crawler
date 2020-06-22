# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 10:34:51 2020

@author: 6989
"""

import pandas as pd

# 資料索引
data = pd.Series([5,4,-2,3,7], index=["a", "b", "c", "d", "e"])
#print(data)

# 觀察資料
# =============================================================================
# print("資料型態:", data.dtype)
# print("資料數量:", data.size)
# print("資料索引:", data.index)
# =============================================================================

# 取得資料 : 依據順序、依據索引
# =============================================================================
# print(data[0], data[4])
# print(data["a"], data["e" ])
# =============================================================================

# 數字運算：基本、總體、順序
# =============================================================================
# print("最大值:", data.max())
# print("總和:", data.sum())
# print("標準差:", data.std())
# print("中位數:", data.median())
# print("最大的三個數:\n", data.nlargest(3))
# =============================================================================


# 字串運算 : 基本、串接、搜尋、取代
data = pd.Series(["您好", "Python", "Pandas"])
print(data.str.lower())
print(data.str.upper())
print(data.str.len())
print(data.str.cat(sep="-"))
print(data.str.contains("P"))
print(data.str.replace("您好", "Hello"))
