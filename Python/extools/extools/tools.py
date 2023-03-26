# -*- coding:utf-8 -*-
import sys
import pandas as pd
import xlwings as xw

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

def DictValueList(dic, keys):
    result = []
    for key in keys:
        if key in dic:
            result.append(dic[key])
    return result

from itertools import permutations

def Weights2Probability(weights, key, order):
    '''Not put back, Unequal probability take a few tiems, Calculation the probability'''  
    names = list(permutations(weights.keys()))
    result = 0
    for w in names:
        index = w.index(key)+1
        if  index == order:
            if index == 1:
                result = CalculationWeightPro(DictValueList(weights,w),index)
                break
            else:
                result += CalculationWeightPro(DictValueList(weights,w),index)
                #print("The permutations of {0} in {1} = {2}".format(key,w,result))  
    return result
        

def CalculationWeightPro(weights, index):
    if index > len(weights):
        return -1
    result = 1
    for i in range(index):
        s = sum(weights)
        result *= weights.pop(0)/s
    return result

def CalculatePro(box, key, n):
    ''' Calculate the probalility of draw the key from box at least n times'''
    result = 0
    for i in range(n):
        result += Weights2Probability(box, key,i+1)
    return result

def RandomBox(box):
    '''Random draw a element from box by weight'''
    import random  
    rand = random.randint(1,sum(box))
    i = 0
    for element in box:
        rand -= element
        if rand <= 0:
            return i
        else:
            i += 1

if __name__ == '__main__':
    from sympy import *

    x = Symbol("x")
    print(diff(E**(sin(x)),x))





