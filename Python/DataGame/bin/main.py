# -*- coding:utf-8 -*-

from DataGame.gameFunction import *
from DataGame.player import *

def Run(player, days):
		for day in range(days):
			player.startDay(day)

testPlayer = Player('Player001')
Run(testPlayer, 1)

#print(testPlayer.__dict__)

# data = ExcleData("data\GameManager.txt")
# a = map(GameFunction, data.indexList)
# b = map(testPlayer.playGame, list(a))
# for x in b:
# 	pass

#print(testPlayer.lv)
for log in testPlayer.log:
	print(log)
