# -*- coding:utf-8 -*-
import xlwings as xw
import pandas as pd

# get  table data from win32 clipboard
def GetWin32Clipboard():
	import win32clipboard as w
	import win32con

	w.OpenClipboard()
	d = w.GetClipboardData(win32con.CF_UNICODETEXT).replace("\r",'')
	w.EmptyClipboard()
	w.SetClipboardData(win32con.CF_UNICODETEXT, d)
	w.CloseClipboard()
	return d

# write a line in file by line number
def writeline(file,line_num,content):
	with open(file,'r+',encoding='utf-8') as f:
		print(f.readline())

writeline('text.txt',1,'1')
#d.to_csv('text.txt',sep='\t',index=False)
#xw.books.active.sheets.active.range('A1').value =  d
