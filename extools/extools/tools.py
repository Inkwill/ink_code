# -*- coding:utf-8 -*-
import sys
import pandas as pd

def Pos2Arear(pos, radius):
    ''' change pos(x,y) to arear info '''
    print('left=%d' % (pos[0]-radius))
    print('top=%d' % (pos[1]-radius))
    print('right=%d' % (pos[0]+radius))
    print('bottom=%d' % (pos[1]+radius))

#Pos2Arear((60,122),3)

def test_Filter():
    '''Filter test '''
    exData = ExcleData("E:\Client_5\Res\ConfigTables\Public\Config\CommonItem.txt")
    for i in exData:
        print(i["Name"])
    # for x in exData.Filter(lambda a, b: a in b, "天",'Name'):
    #   print(x)

def test_dataFram():
    baseData = ExcleData("E:\Client_5\Res\ConfigTables\Public\Config\CommonItem.txt").__dataFram__()
    data = baseData[baseData['Name'].map(lambda x: '天' in x)]
    return data['Name'].values

def MergeDict(dict1, dict2):
    for k, v in dict2.items():
        if k in dict1.keys():
            dict1[k] = dict1[k] + v
        else:
            dict1[k] = v
    return dict1
        


