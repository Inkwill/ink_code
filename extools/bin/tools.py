from extools.tools import *
import xlwings as xw
from extools.ExcleData import ExcleData

name = ("E:\Client_5\Res\ConfigTables\Public\Config\CommonItem.txt",
        "E:\Client_5\Res\ConfigTables\Public\Config\EquipBase.txt",
        "E:\Client_5\Res\ConfigTables\Public\Config\GemInfo.txt")

data = ExcleData.toDataFrame(name,['Name'])
xw.books.active.sheets.active.clear_contents()
xw.Range('A1').value = data
