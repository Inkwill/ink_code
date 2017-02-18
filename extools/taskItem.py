import xlwings as xw
import pandas as pd
from extools.ExcleData import ExcleData
from extools.tools import *

# creat id-Name dict
name = ("E:\Client_5\Res\ConfigTables\Public\Config\CommonItem.txt",
        "E:\Client_5\Res\ConfigTables\Public\Config\EquipBase.txt",
        "E:\Client_5\Res\ConfigTables\Public\Config\GemInfo.txt")

id_Name = ExcleData.CombinetoDataFrame(name,['Name']).Name
name_Id = pd.Series(id_Name.drop_duplicates().index, index = id_Name.drop_duplicates().values, name='Name')

# creat str dict
strDict = ExcleData('E:\Client_5\Res\ConfigTables\Client\StrDictionary111.txt').__dataFrame__().vaule

def SelectConvert(data):
	app = xw.apps.active
	select = app.selection.options(numbers=int).value
	print(data[map(str,select)])

# Mission_Config
file = 'E:\Client_5\Res\ConfigTables\Public\Config\Mission_Config.txt'
col = ['Name','Type','EndSceneID','RewardItemID1','RewardItemNum1','IsItem1Bind','RewardItemID2','RewardItemNum2','IsItem2Bind','RewardItemID3','RewardItemNum3']
mdata1 = {'RewardItemID1':id_Name,'RewardItemID2':id_Name,'RewardItemID3':id_Name}
mdata2= {'RewardItemID1':name_Id,'RewardItemID2':name_Id,'RewardItemID3':name_Id}

# E:\Client_5\Res\ConfigTables\Public\Config\ChargeGifts.txt
# file = 'E:\Client_5\Res\ConfigTables\Public\Config\ChargeGifts.txt'
# col = ['Name','Type','EndSceneID','RewardItemID1','RewardItemNum1','RewardItemID2','RewardItemNum2','RewardItemID3','RewardItemNum3']
# mdata1 = {'Item1':id_Name,'Item2':id_Name,'Item3':id_Name,'Item4':id_Name,'Item5':id_Name}
# mdata2 = {'Item1':name_Id,'Item2':name_Id,'Item3':name_Id,'Item4':name_Id,'Item5':name_Id}

# E:\Client_5\Res\ConfigTables\Public\Config\TimeLimitAchievement.txt
# file = 'E:\Client_5\Res\ConfigTables\Public\Config\TimeLimitAchievement.txt'
# col = ['Item1','Item1Count','Desc']
# mdata1 = {'Item1':id_Name}
# mdata2 = {'Item1':name_Id}

#data = ExcleData(file)
#data.LoadtoExcle(col,mapData = mdata1)
#data.LoadfromExcle()

SelectConvert(strDict)





