# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:57:52 2020

@author: 6989
"""

import datetime

year = datetime.datetime.today().year
month = datetime.datetime.today().month
day = datetime.datetime.today().day
hour = datetime.datetime.today().hour
minute = datetime.datetime.today().minute
print(f'{year}_{month}_{day}')

# =============================================================================
# stockNo = []
# sotckName = []
# import csv
# with open("選股標的.csv", newline='') as csvfile:
#     designedStock = csv.DictReader(csvfile)
#     for row in designedStock:
#         stockNo.append(row["編號"])
#         sotckName.append(row["名稱"])
# print(stockNo)
# print(sotckName)
# =============================================================================

import os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

pathDesktop = f'{desktop}\\text.xlsx'
print(pathDesktop)