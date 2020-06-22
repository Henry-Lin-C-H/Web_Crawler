# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 09:37:06 2020

@author: 6989
"""

with open("test.txt", mode = "w", encoding = "utf-8") as file:
    file.write("有中文\n換行")
with open("test.txt", mode = "r", encoding = "utf-8") as file:
    data = file.read()
print(data)


# =============================================================================
# import urllib.request as request
# import json
# src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
# with request.urlopen(src) as response:
#     data = json.load(response)
# 
# clist = data["result"]["results"]
# with open("data.txt","w", encoding="utf-8") as file:
#     for company in clist:
#         file.write(company["公司名稱"]+"\n")
#         print(company["公司名稱"])
# =============================================================================


import class_test as cl


# =============================================================================
# print(cl.test.x)
# cl.test.say("Yo")
#  
# 實體物件、屬性 
# p1 = cl.Point(3,5)
# p2 = cl.Point(5,2)
# print(p1.x)
# print(p2.x)
# 
# name1 = cl.FullName("C.W.","Peng")
# print(name1.first, name1.last)
# name2 = cl.FullName("T.Y.","Lin")
# print(name2.first, name2.last)
# =============================================================================

# =============================================================================
# p1 = cl.Point(3,4)
# p1.show()
# print(p1.distance(0,0))
# =============================================================================

# =============================================================================
# 實體方法
# f1 = cl.File("File01.txt")
# f1.open()
# data = f1.read()
# print(data)
# 
# f2 = cl.File("File02.txt")
# f2.open()
# data = f2.read()
# print(data)
# =============================================================================
