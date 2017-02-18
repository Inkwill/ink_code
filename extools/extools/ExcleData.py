# -*- coding:utf-8 -*-

import os.path
from pandas import Series, DataFrame
import pandas as pd
import xlwings as xw
from extools import tools
import math

class ExcleData(object):

    """数据表: 第一行类型(方法), 第二行标题名 第三行key(字段名) 
       第一列为索引列
       iterable 从数据开始
    """
    def __init__(self, name):
        super(ExcleData, self).__init__()
        self.name = name
        self.data_original =[]
        self.data=[]
        self.typeDic = {'STRING':str, 'INT':int, 'FLOAT':float}
        try:
            with open(name, "r") as f:
                for line in f:
                    self.data_original.append(line.strip('\n').split('\t'))
            #load txt
            self.dataType = self.data_original[0]
            self.dataTitle = self.data_original[1]
            self.dataKey = self.data_original[2]
            self.indexList = []
            for i in self.data_original[1:]:
                if "#" not in i[0]:
                    self.data.append(i)
            for i in self.data:
                self.indexList.append(i[0])
        except FileNotFoundError:
            print('LoadExcle Err: %s not found!' % name)

    def __next__(self):
        #print('Call next: %d/%d' %(self.iteror,len(self.data)))
        if(self.iteror < len(self.data)):
            item = self.data[self.iteror]
            data = self.__toDic__(item, self.dataKey)
            self.iteror += 1
        else:
            raise StopIteration
        return data

    def __iter__(self):
        '''support iterable'''
        self.iteror = 0
        return self

    def __getitem__(self, n):
        '''support indexing'''
        try:
            if n.__str__() in self.indexList:
                item = self.data[self.indexList.index(n.__str__())]
                return self.__toDic__(item, self.dataKey)
        except Exception:
            print("Not Found: %s in %s" %(n, self.name))
            raise IndexError

    def __delitem__(self, n):
        '''support del item'''
        if n.__str__() in self.indexList:
            self.indexList.remove(n.__str__())
        else:
            print("Not Found: %s in %s" %(n, self.name))
            raise IndexError

    def __toDic__(self, data, columns=None, toArray=False):
        dic = {}
        if columns is None:
            columns = self.dataKey

        for x in columns:
            try:
                if toArray and not type(data[self.dataKey.index(x)]) == list:
                    dic[x] = [data[self.dataKey.index(x)]]
                else:
                    dic[x] = data[self.dataKey.index(x)]
            except IndexError:
                print("Index : %s (%s) out of range (%d)"  % (data[0],self.dataKey.index(x),len(data)))
        return dic

    def __dataFrame__(self,col=None):
        data = {}
        for line in self.data:
                data = tools.MergeDict(data, self.__toDic__(line, col, True))
        #return data
        return DataFrame(data, index=self.indexList, columns= col)

    def CombinetoDataFrame(path,col=None):
        # Combine sevral file.txt to a dataframe 
        data = pd.DataFrame()
        for p in path:
            d = ExcleData(p).__dataFrame__(col)
            if data.empty:
                data = d
            else:
                data = data.append(d)
        return data

    def Filter(self, func, value, key):
        ''' Filter content in key by func'''
        result = []
        if key not in self.dataKey:
            raise KeyError

        for line in self.data:
            data = self.__toDic__(line, self.dataKey)
            #print("If %s in %s" % (value ,data[key]))
            if func(value, data[key]):
                result.append({'ID':line[0],'Name':data[key]})

        return result

    def LoadtoExcle(self,col = None, mapData = None):
        try:
            dataSheet = xw.books.active.sheets[os.path.basename(self.name)]
        except:
            dataSheet = xw.books.active.sheets.add(os.path.basename(self.name))

        df = self.__dataFrame__(col)
        for c in df.columns:
            if mapData and c in mapData:
                print(c)
                df[c].update(df[c].map(mapData[c]))
        dataSheet.clear_contents()
        dataSheet.range('A1').value = df

    def LoadfromExcle(self, mapData = None):
        try:
            dataSheet = xw.books.active.sheets[os.path.basename(self.name)]
        except:
            print("Not found the sheet: %s" % os.path.basename(self.name))

        df = dataSheet.range('A1').expand().options(pd.DataFrame).value
        for c in df.columns:
            if mapData and c in mapData:
                df[c].update(df[c].map(mapData[c]))
            if c in self.dataKey:
                t = self.dataType[self.dataKey.index(c)]
                try:
                    df[c] = df[c].astype(self.typeDic[t])
                except:
                    print("Series's type save Err: %s to %s" % (c, self.typeDic[t]))
                    if df[c].isnull().any():
                        df[c] = df[c].dropna().astype(self.typeDic[t]).astype(str).replace('nan', '')
                
        df.index = df.index.map(lambda x:str(int(x)))
        self.Save(df, self.name)

    def Save(self, df, export = None, encode= 'GBK'):
        if export !=  None:
            with open(export,'w',encoding = encode) as f:
                print('Start save data :(columns= %d, lines = %d)' % (len(df.columns), len(df.index)))
                for line in self.data_original:
                    index = line[0]
                    if "#" not in index and index in df.index:
                        for c in df.columns:
                            if c in self.dataKey:
                                oldata = line[self.dataKey.index(c)]
                                newdata = df[c][index]
                                if oldata != str(newdata):
                                    print('[id ={0}][col ={1}]'.format(index, c))
                                    print('{0} -> {1}'.format(oldata, newdata))
                                    line[self.dataKey.index(c)] = newdata if not math.isnan(float(newdata)) else ''
                    line = list(map(str,line))
                    f.write('\t'.join(line) + '\n')
        else:
            print('Start save data :(columns= %d, lines = %d)' % (len(df.columns), len(df.index)))
            for line in self.data_original:
                index = line[0]
                if "#" not in index and index in df.index:
                    for c in df.columns:
                        if c in self.dataKey:
                            oldata = line[self.dataKey.index(c)]
                            newdata = df[c][index]
                            if oldata != str(newdata):
                                print('[id ={0}][col ={1}]'.format(index, c))
                                print('{0} -> {1}'.format(oldata, newdata))
                                line[self.dataKey.index(c)] = newdata if not math.isnan(float(newdata)) else ''
                line = list(map(str,line))
