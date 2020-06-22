# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 09:40:13 2020

@author: 6989
"""

class test:
    x = 3
    def say(msg = "Hello"):
        print(msg)
        
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def distance(self, targetx, targety):
        return (((self.x - targetx)**2 + (self.y - targety)**2)**0.5)
    
        
class FullName:
    def __init__(self,first,last):
        self.first= first
        self.last= last
        
# File 實體物件的設計: 包裝檔案讀取的程式
class File:
    def __init__(self,name):
        self.name = name
        self.file = None #尚未開啟檔案: 初期是None
    def open(self):
        self.file = open(self.name, mode = "r", encoding="utf-8")
    def read(self):
        return self.file.read()
    