# -*- coding:utf-8 -*-

from extools.ExcleData import *

class GameFunction(object):
	"""the function of game, that some player will be changed by playing"""
	def __init__(self, id):
		self.id = id
		try:
			dic = ExcleData("..\data\GameManager.txt")[id]
			self.name = dic['name']
			self.needLv = int(dic['needlv'])
			self.costTime = int(dic['costTime'])
		except Exception:
			print("[GameFunction init]Not found : ..\data\GameManager.txt")

		try:
			self.data = ExcleData("..\data\%s.txt" % self.id)
			self.funcList = self.data.dataKey[1:]
		except Exception:
			print("[GameFunction init]Not found : %s" % "..\data\%s.txt" % self.id)

	def OnPlay(self, player):
		for f in self.funcList:
			try:
				getattr(self, f)(player)
			except AttributeError:
				print("[GameFunction OnPlay]Not found func: %s" % f)


	def AddExp(self, player):
		if self.data:
			addExp = int(self.data[player.lv]['AddExp'])
		else :
			addExp = 0
			print("Not found 'AddExp': %s" % "..\data\%s.txt" % self.id)
		player.AddExp(addExp)

	def AddCopper(self,player):
		if self.data:
			addCopper = int(self.data[player.lv]['AddCopper'])
		else :
			addCopper = 0
			print("Not found 'AddCopper': %s" % "..\data\%s.txt" % self.id)
		player.AddMoney({'copper':addCopper})

	def AddSilver(self,player):
		if self.data:
			addSilver = int(self.data[player.lv]['AddSilver'])
		else :
			addSilver = 0
			print("Not found 'AddSilver': %s" % "..\data\%s.txt" % self.id)
		player.AddMoney({'silver':addSilver})
