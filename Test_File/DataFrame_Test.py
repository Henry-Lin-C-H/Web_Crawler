# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 08:42:38 2020

@author: 6989
"""

import pandas as pd
data = pd.DataFrame({
        "Name":["Amy", "John", "Bob"],
        "Salary":[30000, 50000, 40000]
        })

print(data["Name"][0])
print(data.iloc[0]["Name"])

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
print(allTime)