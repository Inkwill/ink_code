# -*- coding:utf-8 -*-
import pandas as pd
import xlwings as xw

def To_Excle(df,sheetName,startRange = 'A1',newbook = True,clear = True,show_index = True):
    if newbook:
        dataSheet = xw.Book().sheets[0]
        dataSheet.name = sheetName
    else:
        try:
            dataSheet = xw.books.active.sheets[sheetName]
        except:
            dataSheet = xw.books.active.sheets.add(sheetName)
    if clear:            
        dataSheet.clear_contents()
    if show_index:
        dataSheet.range(startRange).value = df
    else:
        dataSheet.range(startRange).options(index = False).value = df

def GetDataFrame(self,col = None, mapData = None):
    df = self.__dataFrame__(col)
    for c in df.columns:
        if mapData and c in mapData:
            print(c)
            df[c].update(df[c].map(mapData[c]))
        return df
