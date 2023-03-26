# -*- coding:utf-8 -*-

from extools.ExcleData import *
from DataGame.gameFunction import *

class Player():
		"""Player data sample, has attr: num ,time"""
		def __init__(self, name, time = 120, pay = 0):
			self.maxTime = time
			self.maxPay = pay
			self.name = name
			self.lv = 1
			self.exp = 0
			self.money = {'copper':0, 'silver':0}
			self.log = []
			self.done = []
			self.time = 0
			self.pay = 0

			try:
				self.gameFunctions = ExcleData("..\data\GameManager.txt").indexList
			except Exception:
				print("Not found : data\GameManager.txt")

		def AddExp(self, exp):
			#print("\t[exp]%s get exp : %d" % (self.name, exp))
			self.log.append("\t[Get exp]: %d" % exp)
			self.exp += exp
			self.levelUp()

		def levelUp(self):
			needExp = int(ExcleData("..\data\LevelData.txt")[self.lv]['exp'])
			if self.exp >= needExp:
				newLv = self.lv + 1
				self.exp -= needExp
				self.lv = newLv
				self.log.append("\t\t[lvUp]: %d" % self.lv)
				#print("\t\t[lvUp]%s LevelUp to: %d" % (self.name, self.lv))
				self.levelUp()

		def AddMoney(self, money):
			if 'copper' in money.keys():
				self.log.append("\t[Get money]: copper = %d" % money['copper'])
				self.money['copper'] += money['copper']
			elif 'silver' in money.keys():
				self.log.append("\t[Get money]: silver = %d" % money['silver'])
				self.money['silver'] += money['silver']


		def playGame(self,game):
			'''play a gameFunction '''
			if game:
				self.time += game.costTime
				self.log.append("%s play the %s(%s) [CostTime = %dm]" %(self.name, game.id, game.name, game.costTime))

				# Do Something ...
				game.OnPlay(self)

				# End
				self.log.append("\tEnd of %s--Remaining Time:%dm\n" % (game.id, self.maxTime - self.time))
				self.done.append(game.id)
				return self.time < self.maxTime
			else :
				return False

		def offline(self, day):
			'''time is over'''
			self.log.append("****Day[%d] time is Over!****" % (day + 1))

		def chooseGame(self):
			for game in self.gameFunctions:
				if game not in self.done:
					gf = GameFunction(game)
					if gf.needLv <= self.lv:
						return gf
			return None

		def startDay(self, day):
			self.time = 0
			self.pay = 0
			self.done = []
			self.log.append("\n\n****Start a new day :%d****" % (day +1))

			while self.playGame(self.chooseGame()):
				pass

			self.offline(day)
