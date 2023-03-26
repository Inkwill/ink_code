import random
import pandas as pd
import xlwings as xw
from pylab import show
import math
import os

def We(d):
	return 1.0/(1.0+10**(d/400))

def LoadFightScore(path):
	FightScore = []
	try:
		with open(path, "r") as f:
			for line in f:
				FightScore.append(float(line.strip('\n')))
	except FileNotFoundError:
		print('LoadExcle Err: %s not found!' % name)
	return FightScore

class Team(object):
	"""docstring for Team"""
	K = 32
	score_win = 10
	score_lose = 1
	num_addscore = 20

	def __init__(self, id):
		super(Team, self).__init__()
		self.id = id
		self.winscore = 0
		self.losescore = 0
		self.addscore = 0
		self.winNum = 0
		self.loseNum = 0
		self.fightscore = 0

	def totlascore(self):
		return self.winscore + self.losescore + self.addscore

	def win(self,opponent):
		#self.addscore += int((self.winNum + self.loseNum)/self.num_addscore)
		#self.addscore += 1 if opponent.totlascore() > self.totlascore() else 0
		#self.winscore += self.score_win
		self.winscore = round((self.winscore + self.K *(1-We(opponent.totlascore() - self.totlascore()))),0)
		self.winNum +=1

	def lose(self,opponent):
		#self.addscore += int((self.winNum + self.loseNum)/self.num_addscore)
		#self.losescore += self.score_lose
		self.losescore = round((self.losescore + self.K *(0-We(opponent.totlascore() - self.totlascore()))),0)
		self.loseNum +=1

	def battle(self, opponent):
		key = self.fightscore - opponent.fightscore
		rate = min(50 + key * 50 , 100)
		if rate > 0 and random.randint(0,100)<= rate:
			self.win(opponent)
			opponent.lose(opponent)
			#print("Team_{0}[{2}] win Team_{1}[{3}]".format(self.id, opponent.id,self.score,opponent.score))
		else:
			self.lose(opponent)
			opponent.win(opponent)
			#print("Team_{0}[{2}] lose Team_{1}[{3}]".format(self.id, opponent.id,self.score,opponent.score))


	def match(self, teams, n=50):
		m_team = []
		for t in teams:
			if t.id != self.id and abs(t.totlascore() - self.totlascore()) <= n and (self.winNum + self.loseNum) == (t.winNum + t.loseNum):
				m_team.append(t)
		if len(m_team) > 0:
			return m_team[random.randint(0,len(m_team)-1)]
		else:
			return self.match(teams,n+1)

def TeamBattle(teams, times):
	for i in range(times):
		for t in teams:
			if t.winNum + t.loseNum + 1 == i + 1:
				t.battle(t.match(teams))


def Test(battleTimes, TeamNum):

	fightscores = LoadFightScore("D:/Work/MyDoc/FightScore.cfg")
	teams = []
	for i in range(TeamNum):
		teams.append(Team(i+1))
		teams[i].fightscore = fightscores[i] if i < len(fightscores) else 2.0

	TeamBattle(teams, battleTimes)
	result = []
	for t in teams:
		result.append(t.totlascore())
	return pd.Series(result)

if __name__ == '__main__':

	data = pd.DataFrame(index=range(200),columns=range(10))
	describe = []
	for i in range(10):
		s = Test(80, 200)
		data[i] = s
		describe.append(200 - len(s.drop_duplicates()))

	dataSheet = xw.books.active.sheets['elo']
	dataSheet.clear_contents()
	dataSheet.range("A2").value=data
	dataSheet.range("B1").value=describe

