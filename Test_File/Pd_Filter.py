# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:54:43 2020

@author: 6989
"""

import pandas as pd

# 篩選練習 Series
# ====================================================================
# data = pd.Series([30,15,20])
# condition = data > 18
# print(condition)
# filteredData = data[condition]
# print(filteredData)
# =============================================================================

# =============================================================================
# data = pd.Series(["您好", "Python", "Pandas"])
# condition = data.str.contains("P")
# print(condition)
# filteredData = data[condition]
# print(filteredData)
# =============================================================================


# 篩選練習 DataFrame
data = pd.DataFrame({
        "Name":["Amy", "Bob", "Charles"],
        "Salary":[30000, 50000, 40000]
        })
print(data)
# =============================================================================
# condition = data["Salary"] >= 40000
# filteredData = data[condition]
# print(filteredData)
# =============================================================================

condition = data["Name"]=="Amy"
print(condition)
filteredData = data[condition]
print(filteredData)