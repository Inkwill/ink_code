from nose.tools import *
from extools.ExcleData import ExcleData

def test_ExcleData():
	data = ExcleData("tests\CommonItem.txt")
	assert_equal(data.name, "tests\CommonItem.txt")
	assert_equal(data.data_original[0],data.dataType)
	assert_equal(data.data_original[1],data.dataTitle)
	assert_equal(data.data_original[2],data.dataKey)

	i = 0
	for x in data.data_original:
		i = i+1 if '#' in x[0] else i
	assert_equal(len(data.data_original),i + 1 + len(data.data))

	for x in data.data:
		assert_equal(data.__toDic__(x), data[x[0]])

def test_DataFrame():
	from random import choice

	da = ExcleData("tests\CommonItem.txt")
	df = da.__dataFrame__()
	id = choice(da.indexList)
	key = choice(da.dataKey)
	assert_equal(da[id][key], df[key][id])

def test_Save():
	import os
	import filecmp 

	da = ExcleData("tests\CommonItem.txt")
	df = da.__dataFrame__()
	da.Save(df,'Temp.txt')
	assert_equal(filecmp.cmp('Temp.txt',da.name),True)
	os.remove('Temp.txt')
