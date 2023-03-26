import xlwings as xw
import pandas as pd
from extools.ExcleData import ExcleData
from extools.tools import *
import itertools
import random
import numpy as np

#PATH CONFIG
PATH_MAIN = "D:\Work\main_TLBBM_U5\Res\ConfigTables\\"
PATH_TY = "D:\Work\Res_TY17\ConfigTables\\"
PATH_WW = "D:\Work\Res_WW17\ConfigTables\\"

file_commonitem = "\Public\Config\CommonItem.txt"
file_strdictinary=  "Client\StrDictionary.txt"
file_approach=  "Client\Approach.txt"
file_titledata =  "Public\Config\TitleData.txt"
file_activitylobby =  "Public\Config\ActivityLobby.txt"

class TxtLib(object):
	"""the useful text file lib """
	def __init__(self, path):
		self.path = path
		self.name = ["Public\Config\CommonItem.txt","Public\Config\EquipBase.txt","Public\Config\GemInfo.txt"]

	def commonItemInfo(self):
		return pd.read_table(r"E:\Python\Projects\extools\data\ItemInfo.txt",encoding = 'utf-8',index_col='id')

	def itemName2Id(self):
		return pd.Series(self.itemId2Name().index, index = self.itemId2Name().values, name='Name')

	def itemId2Name(self,type=int):
		data = ExcleData.CombinetoDataFrame([self.path + x for x in self.name],['Name']).Name
		data.index = data.index.astype(type)
		return data

	def strlib(self):
		return pd.read_table(self.path + 'Client\StrDictionary.txt',encoding = 'gbk',index_col=0,names=['id','des','str'])
	
def Select_Content(data,column=None,keyStr= False):
	select = xw.apps.active.selection
	for cell in select:
		key = cell.options(numbers=int).value
		if keyStr:
			key = str(key)
		if column:
			try:
				cell.value = data.loc[key][column]
			except:
				print("{0} can't find!".format(key))
		else:
			try:
				cell.value = data.loc[key]
			except:
				print("{0} can't find!".format(key))

def Select_Id(data,column):
	select = xw.apps.active.selection
	for cell in select:
		value = cell.value
		try:
			cell.value = data[data[column]==value].index[0]
		except:
			print("{0} can't find!".format(value))

class TableFile():
	"""a file can operate with index"""
	def __init__(self, path,encoding='gbk'):
		self.path = path
		self.encoding = encoding
		self.indexs = []
		with open(path, 'r',encoding=encoding) as f:
			self.clist = f.readlines()
			#remove the empty line
			for line in self.clist:
				if '\t' in line:
					self.indexs.append(line[:line.index('\t')])
				else:
					self.indexs.append('0')
			#self.indexs = [(lambda x: x[:x.index('\t')] if '\t' in x else "") (x) for x in self.clist]

	def __next__(self):
		'''support iterable'''
		if(self.iteror < len(self.indexs)):
			key = self.indexs[self.iteror]
			item = (key,self.clist[self.iteror].strip(key).strip('\t'))
			self.iteror += 1
		else:
			raise StopIteration
		return item

	def __iter__(self):
		'''support iterable'''
		self.iteror = 0
		return self

	def __getitem__(self, keys):
		'''support indexing'''
		if isinstance(keys,slice):
			return list(itertools.islice(self,keys.start,keys.stop,keys.step))
		if isinstance(keys,int):
			keys = [keys]
		result = []
		for key in keys:
			try:
				item = self.clist[self.indexs.index(key.__str__())].strip('\n')
				item = item[item.index('\t')+1:]
				result.append(item)
			except:
				print("Not Found: key[%s] in '%s'" %(key, self.path))
				raise KeyError
		return result

	def __setitem__(self, key, value):
		'''support set item by index'''
		try:
			self.clist[self.indexs.index(key.__str__())] = str(key) + '\t' + str(value) + '\n'
			#self.save()
		except:
			print("Not Found: key[%s] in '%s'" %(key, self.path))
			raise KeyError

	def __delitem__(self,key):
		'''support delete item by index'''
		del_index = str(key)
		try:
			self.clist.remove(self.clist[self.indexs.index(del_index)])
			self.indexs.remove(del_index)
			#self.save()
		except:
			print("Not Found: key[%s] in '%s'" %(key, self.path))
			raise KeyError

	def __getpos__(self,key):
		'''get the pos of  key in clist  '''
		lastindex = -1
		for id in self.indexs:
			if id[0]=='#' or id == 'INT' or id == 'int' or id == '' or id == 'Uint16':
				continue
			try:
				key = int(key)
				if lastindex < key < int(id):
					return self.indexs.index(str(lastindex)) + 1
				else:
					lastindex = int(id)
			except:
				print("Get Pos Error: key[{0} or {1}] is not a integer!".format(key,id))
				raise KeyError
		return len(self.indexs)

	def insert(self,key,value,autosave = True,overwrite = False):
		'''insert item by index'''
		if str(key) in self.indexs:
			if overwrite:
				self.__delitem__(key)
			else:
				print("Insert Error :the key[{0}] is already exist!".format(key))
				raise KeyError
		pos = self.__getpos__(key)
		self.indexs.insert(pos, str(key))
		self.clist.insert(pos,str(key) + '\t' + str(value) + '\n')
		if autosave:
			self.save()

	def add(self,keys,values,autosave = True,overwrite = False):
		'''insert itemlist by indexlist'''
		for key in keys:
			value = values[keys.index(key)]
			#print("key={0},value={1}".format(key,value))
			self.insert(key,value, autosave = autosave,overwrite = overwrite)

	def save(self):
		with open(self.path,'w',encoding=self.encoding) as f:
			print("Saving~~~~~~~~~~~~")
			f.writelines(self.clist)
	
	def sifting(self,keys):
		sift_keys = []
		for key in keys:
			str(key) in self.indexs and sift_keys.append(key)
		return sift_keys

def AddTableById(file,id,content_add):
	with open(file,"r+", encoding='utf-8') as f:
		content = f.read()
		f.seek(0,0)
		pos = content.find(str(id))
		if pos >=0 :
			content = content[:pos] + content_add  + content[pos:]
		f.write(content)

def MakeTable_Exlselect(path):
	select = xw.apps.active.selection
	print(select.option())

def SyncTable(filename,encoding = 'gbk',**kwargs):
	tb_ori = TableFile(PATH_MAIN + filename,encoding=encoding)
	keys = tb_ori.sifting(kwargs['keys'])
	content_add = tb_ori[keys]
	for path in kwargs['paths']:
		tb = TableFile(path + filename,encoding = tb_ori.encoding)
		tb.add(keys,content_add,overwrite = True)

def AddTable(sheetName,pathlist):
	sheet = xw.Book(r"D:\Work\Tlbb_Doc\4-数值相关\7_资源放出\表格配置\maketable.xlsx").sheets(sheetName)
	filename = sheet.range('B1').value
	keys = sheet.range('A3').expand('down').options(numbers = int).value
	values = sheet.range('B3').expand().options(numbers= int).value
	contents = []
	if isinstance(keys,int):
		keys  = [keys]
		contents.append('\t'.join(str(x) for x in values))
	else:
		for content in values: 
			contents.append('\t'.join(str(x) for x in content))
	for path in pathlist:
		file = path + filename
		tb = TableFile(file)
		tb.add(keys,contents,autosave = False,overwrite = True)
		print(keys)
		tb.save()

def Re_name(path,key = None,replace=None):
	import os
	import shutil
	newpath = path + 'new\\'
	not os.path.exists(newpath) and os.mkdir(newpath)
	list(map(os.remove,[newpath + f for f in os.listdir(newpath)]))

	filelist = [f for f in  os.listdir(path) if os.path.isfile(path+f) and  key and  key  in f]
	
	list(map(shutil.copyfile,[path+f for f in filelist],[newpath + f for f in filelist]))

	if key:
		for file in filelist:
			os.rename(newpath +file, newpath+file.replace(key,replace))


def Re_encoding(path,old_encoding = None,new_encoding=None):
	import os
	import chardet
	import codecs

	newpath = path + 'new\\'
	not os.path.exists(newpath) and os.mkdir(newpath)
	list(map(os.remove,[newpath + f for f in os.listdir(newpath)]))

	filelist = [f for f in  os.listdir(path) if os.path.isfile(path+f) and 'GBK_' in f]
	for file in filelist:
		with codecs.open(path+file, 'rb') as f:
			content = f.read()
			cur_encoding =  chardet.detect(content)['encoding']
			if cur_encoding == old_encoding:
				content = content.decode(old_encoding,'ignore')
				try:
					codecs.open(newpath + file.replace('GBK_',''), 'w', encoding = new_encoding).write(content)
				except :
					print("Re_encoding Error! : {0}".format(path + file))
					raise KeyError
				else:
					print("{0}:  {1} ->  {2}".format(file,cur_encoding,new_encoding))
			else:
				print("old_encoding = {0},cur_encoding = {1}".format(old_encoding,cur_encoding))
	print("Re_encoding compelet!")

class Weapon_Soul(object):
	"""docstring for Weapon_Soul"""
	def __init__(self):
		self.attr = [0 for i in range(4)]
		self.attrMax = [100 for i in range(4)]

	def train(self):
		p1,p2,p3 = 300,100,200
		rand  =  [random.randint(0,101)/100.0 for i in range(4)]
		add = [round(rand[i] ** (((self.attr[i]/self.attrMax[i])*p1 + p2)/p3)*2-1,2) for i in range(4)] 
		if sum(add)>0:
			#print("\tAdd {0}: {1} -> {2}".format(add,self.attr, [round(self.attr[i]+add[i],2) for i in range(4)]))
			self.attr =  [min(round(self.attr[i]+add[i],2),self.attrMax[i]) for i in range(4)]
		#else:
			#print("\tDrop[sum = {0:.2f}]".format(sum(add)))
			
def Test_Ws():
	ws = Weapon_Soul()
	time = 0
	sumlist = [0 for x in range(100)]
	while  sum(ws.attr) < sum(ws.attrMax):
		# print('{0:*^10} | {1} | sum={2:.2f}'.format(time,ws.attr,sum(ws.attr)))
		ws.train()
		if len(sumlist)>time :
			sumlist[time] = sum(ws.attr)
		time += 1

	return time,sumlist

def Run(func,times):
	result = 0
	attlist = np.array([])
	for i in range(times):
		time,sumlist = func()
		result += time
		attlist = np.insert(attlist, 0, sumlist, axis = 0)
	return result/times,attlist.reshape(times,100)

# import matplotlib.pyplot as plt

# num,attrlist = Run(Test_Ws,3)
# print('num = ', num)
# print('list = ',attrlist)
# for d in attrlist:
# 	plt.plot(d)
# plt.show()


# Re_encoding("C:\\Users\\wangsijia\\Desktop\\HK+1\\Client\\",'UTF-16','GBK')
# Re_encoding("C:\\Users\\wangsijia\\Desktop\\HK+1\\Public\\Config\\",'UTF-16','GBK')
#Re_encoding("C:\\Users\\wangsijia\\Desktop\\HK+1\\Public\\Scene\\",'UTF-16','GBK')











