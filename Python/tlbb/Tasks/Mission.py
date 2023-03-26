#coding=utf-8
import gevent
import time
import random

class Mission():
    def __init__(self, person):
        self.person = person
    
    def run(self, nIndex=0):
        if nIndex == 1:
            self.BaiYeTianShi()
        elif nIndex == 2:
            self.FuDiQiYuan()
        elif nIndex == 3:
            self.XuMiCaoYao()
        elif nIndex == 4:
            self.ShenMiDiTu()
        elif nIndex == 5:
            self.XiuFuDiTu()
        elif nIndex == 6:
            self.NanMuRong()
        elif nIndex == 7:
            self.BeiQiaoFeng()
        elif nIndex == 8:
            self.DianFengZhiZhan()
        elif nIndex == 9:
            self.JiXuQianXing()
        elif nIndex == 10:
            self.KeAiMengCong()
        elif nIndex == 11:
            self.LuZhiXue()
        elif nIndex == 12:
            self.HeiWuGong()
        elif nIndex == 13:
            self.YinYouDuWu()
        elif nIndex == 14:
            self.ChongWuBaoBao()
        elif nIndex == 15:
            self.ShenXianDiaoXiang()
        elif nIndex == 16:
            self.ChengYiKaoYan()
        elif nIndex == 17:
            self.WuGongKaoYan()
        elif nIndex == 18:
            self.AiXinKaoYan()
        elif nIndex == 19:
            self.ShiZhongQin()
        elif nIndex == 20:
            self.ZhiLiKaoYan()
        elif nIndex == 21:
            self.QieCuoWuYi()
        elif nIndex == 22:
            self.JueShiShenGong()
        elif nIndex == 23:
            self.QiuJiuZhiRen()
        elif nIndex == 24:
            self.HeiYiBangFei()
        elif nIndex == 25:
            self.JiuHouTuZhenYan()
        elif nIndex == 26:
            self.XiaoXinXingShi()
        elif nIndex == 27:
            self.GuanXinJiaRen()
        elif nIndex == 28:
            self.HuoQuTuZhi()
        elif nIndex == 29:
            self.DaZhanERen()
        elif nIndex == 100:
            self.Move(26.3, 28.8,10)
            self.Move(43.8, 27.9,10)
            self.Move(50.9, 49.4,10)
            self.Move(51.9, 52.3,5)
            self.Battle(51.9, 52.3, 3, 200)
        else:
            self.BaiYeTianShi()
            self.FuDiQiYuan()
            self.XuMiCaoYao()
            self.ShenMiDiTu()
            self.XiuFuDiTu()
            self.NanMuRong()
            self.BeiQiaoFeng()
            self.DianFengZhiZhan()
            self.JiXuQianXing()
            self.KeAiMengCong()
            self.LuZhiXue()
            self.HeiWuGong()
            self.YinYouDuWu()
            self.ChongWuBaoBao()
            self.ShenXianDiaoXiang()
            self.ChengYiKaoYan()
            self.WuGongKaoYan()
            self.AiXinKaoYan()
            self.ShiZhongQin()
            self.ZhiLiKaoYan()
            self.QieCuoWuYi()
            self.JueShiShenGong()
            self.QiuJiuZhiRen()
            self.HeiYiBangFei()
            self.JiuHouTuZhenYan()
            self.XiaoXinXingShi()
            self.GuanXinJiaRen()
            self.HuoQuTuZhi()
            self.DaZhanERen()
            

    def Move(self,posx, posz, durtime=15):
        self.person.ACG_CHARMOVE(posx,posz)
        time1 = time.time()
        while True:
            gevent.sleep(2)
            self.person.ACGIdle()
            curtime = time.time()
            if curtime-time1 > durtime:
                break
     
    def Battle(self,posx,posz,rd,sMonsterName = u'',durtime=20):
        self.person['state'] = "start"
        time1 = time.time()
        while True:
            self.person.battle(posx,posz,rd,sMonsterName)
            curtime = time.time()
            if curtime-time1 > durtime:
                break
            #self.person.ACGIdle()
            gevent.sleep(0)
        pass
    #任务1--拜谒天师
    def BaiYeTianShi(self):
        self.person.ACGAskMail()
        gevent.sleep(2)
        self.person.ACGIdle()
        self.Move(21,27)
        self.person.ACGCharDefaultEvent(0)
        gevent.sleep(2)
        self.person.ACGIdle()
        self.person.ACGMissionSubmit(0,0,1003001,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
           
    #任务2--福地奇缘
    def FuDiQiYuan(self):
        self.person.ACGCharDefaultEvent(0)
        gevent.sleep(2)
        self.person.ACGIdle()
        self.person.ACGAskAcceptMission(0,0,1003002)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(48,17)
        
        self.person.ACGCharDefaultEvent(1)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(1,0,1003002,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
    
    #任务3--寻觅草药
    def XuMiCaoYao(self):
        self.person['MissionIsFinish'] = 0
        self.person.ACGCharDefaultEvent(1)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGAskAcceptMission(0,0,1003003)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        #self.Move(54.8,48.9,20)
        self.Move(random.uniform(54, 56),random.uniform(49, 51),20)
        
        self.Battle(54.8,48.9,3)
        
        while self.person['MissionIsFinish'] != 1:
            self.Battle(54.8,48.9,3)
            gevent.sleep(0)
        
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(48,17,20)
        
        self.person.ACGCharDefaultEvent(1)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(1,0,1003003,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        
    #任务4--神秘地图
    def ShenMiDiTu(self):
        self.person.ACGCharDefaultEvent(1)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGAskAcceptMission(0,0,1003005)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(51,18,10)
        
        self.person.ACGCharDefaultEvent(2)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(1,0,1003005,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        
    #任务5--修复地图
    def XiuFuDiTu(self):
        self.person.ACGMissionEnterMovie(19,1,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        self.person.ACGMissionMovieEnd(19)
        gevent.sleep(2)
        self.person.ACGIdle()
        self.person.ACGMissionEnterMovie(19,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGCharDefaultEvent(2)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(2,0,1003006,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
    
    #任务6--南慕容
    def NanMuRong(self):
        self.person.ACGCharDefaultEvent(2)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGAskAcceptMission(0,0,1003007)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(53,23,5)
        
        self.Move(75,50,15)
        
        self.Move(76,51,5)
        
        self.person.ACGCharDefaultEvent(4)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(4,0,1003007,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
    
    #任务7--北乔峰
    def BeiQiaoFeng(self):
        self.person.ACGCharDefaultEvent(4)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGAskAcceptMission(0,0,1003008)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(82,47,10)
        
        self.person.ACGCharDefaultEvent(3)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(3,0,1003008,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        
    #任务8--巅峰之战
    def DianFengZhiZhan(self):
        self.person.ACGMissionEnterMovie(55,1,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        self.person.ACGMissionEnterMovie(55,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGCharDefaultEvent(3)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(3,0,1003009,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
     
    #任务9--继续前行
    def JiXuQianXing(self):
        self.person.ACGCharDefaultEvent(3)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGAskAcceptMission(0,0,1003010)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(93.66,30.34,10)
        self.Move(115.35,29.76,10)
        self.Move(121.29,28.90,10)
        self.Move(124,28,10)
        
        self.person.ACGCharDefaultEvent(10000201)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(10000201,0,1003010,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
    
    #任务10--可爱萌宠
    def KeAiMengCong(self):
        self.person.ACGCharDefaultEvent(10000201)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGAskAcceptMission(0,0,1003011)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(125,38,10)
        
        self.person.ACGCharDefaultEvent(20)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(20,0,1003011,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        
    #任务11--鹿之血
    def LuZhiXue(self):
        self.person['MissionIsFinish'] = 0
        self.person.ACGCharDefaultEvent(20)
        gevent.sleep(2)
        self.person.ACGIdle()
           
        self.person.ACGAskAcceptMission(0,0,1003012)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        
        #self.Move(148,29.6)
        
        self.Move(random.uniform(148, 150),random.uniform(29, 31),20)
        
        
        self.Battle(148,29.6,3,u'鹿')
        
        while self.person['MissionIsFinish'] != 1:
            self.Battle(148,29.6,3,u'鹿')
            gevent.sleep(0)
        
        
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(125,38)
        
        self.person.ACGCharDefaultEvent(20)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(20,0,1003012,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        
    #任务12--黑蜈蚣
    def HeiWuGong(self):
        self.person['MissionIsFinish'] = 0
        self.person.ACGCharDefaultEvent(20)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGAskAcceptMission(0,0,1003013)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(142,55,20)
        #收集黑蜈蚣
        self.person.ACGCharDefaultEvent(36)
        gevent.sleep(5)
        self.person.ACGIdle()
        
        while self.person['MissionIsFinish'] != 1:
            self.person.ACGCharDefaultEvent(36)
            gevent.sleep(5)
            self.person.ACGIdle()
        
        self.Move(125,38)
        
        self.person.ACGCharDefaultEvent(20)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(20,0,1003013,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()

    #任务13--引诱毒物,莽牯毒哈王
    def YinYouDuWu(self):
        self.person['MissionIsFinish'] = 0
        self.person.ACGCharDefaultEvent(20)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGAskAcceptMission(0,0,1003014)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(168,40.6)
        
        #点香引诱
        self.person.ACGCharDefaultEvent(37)
        gevent.sleep(5)
        self.person.ACGIdle()
        
        #self.person['monsterdic'] = {}
                
        self.person.ACGAskChangeScene()
        gevent.sleep(5)
        self.person.ACGIdle()
        
        #XXXXXXXXXXXXXX
        nCurrentScene = self.person.m_CurrentSceneID
        
        self.person.ACGENTERSCENE(1)
        gevent.sleep(5)
        self.person.ACGIdle()
                
        self.person.ACGMissionEnterMovie(69,1,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACG_EXECUTESCRIPT(1100019,u'OnMovieEnd',[1,1100019,69,1])
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionEnterMovie(69,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Battle(160,37,3)
        
        i = 1 # 由于大于120秒后副本会自动退出，所以打怪时间不能超过120秒
        while self.person['MissionIsFinish'] != 1:
            i=i+1
            self.Battle(160,37,3)
            gevent.sleep(0)
            if i>5:
                break
        
        #XXXXXXXXXXXXXX
        timeout = time.time()
        while nCurrentScene == self.person.m_CurrentSceneID:
            gevent.sleep(1)
            self.person.ACGIdle()
            if time.time()-timeout>15:
                break
        
        #self.person['monsterdic'] = {}
        self.person.ACGAskChangeScene()
        gevent.sleep(5)
        self.person.ACGIdle()
        
        self.person.ACGENTERSCENE(1)
        gevent.sleep(5)
        self.person.ACGIdle()
        
        self.Move(162,50)
        
        self.person.ACGCharDefaultEvent(10000203)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        #self.person['monsterdic'] = {}
        self.person.ACGMissionSubmit(10000203,0,1003015,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()

    #任务14--宠物宝宝
    def ChongWuBaoBao(self):
        self.person.ACG_EXECUTESCRIPT(1100044,u'PetSelect',[2])
        gevent.sleep(3)
        self.person.ACGIdle()
        
    #任务15--神仙雕像
    def ShenXianDiaoXiang(self):
        self.person.ACGCharDefaultEvent(10000203)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGAskAcceptMission(0,0,1003016)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(163.8,105.1)
        
        self.Move(167.4,127.6,30)
        
        self.Move(167.6,130)
        
        self.person.ACGCharDefaultEvent(38)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(38,0,1003016,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        
    #任务16--诚意考验(需要验证一下)
    def ChengYiKaoYan(self):
        self.person.ACGMissionEnterMovie(46,1,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        self.person.ACGMissionEnterMovie(46,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGCharDefaultEvent(10000205)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(10000205,0,1003017,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        
    #任务17--武功考验
    def WuGongKaoYan(self):
        self.person['MissionIsFinish'] = 0
        self.person.ACGCharDefaultEvent(10000205)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGAskAcceptMission(0,0,1003018)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        #self.Move(149,164.7,20)
        self.Move(random.uniform(148, 150),random.uniform(164, 166),20)
        
        self.Battle(149,164.7,3,u'幻蝶')
        
        while self.person['MissionIsFinish'] != 1:
            self.Battle(149,164.7,3,u'幻蝶')
            gevent.sleep(0)
        
        self.Move(165,133,20)
        
        self.person.ACGCharDefaultEvent(10000205)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(10000205,0,1003018,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        
    #任务18--爱心考验
    def AiXinKaoYan(self):
        self.person['MissionIsFinish'] = 0
        self.person.ACGCharDefaultEvent(10000205)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGAskAcceptMission(0,0,1003019)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(148.3,127.1,7)
        
        self.person.ACGCharDefaultEvent(55)#采花
        gevent.sleep(3)
        self.person.ACGIdle()
    
        while self.person['MissionIsFinish'] != 1:
            self.person.ACGCharDefaultEvent(55)#采花
            gevent.sleep(3)
            self.person.ACGIdle()
        
        self.Move(165,133,20)
        
        self.person.ACGCharDefaultEvent(10000205)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(10000205,0,1003019,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        
    #任务19--石中琴
    def ShiZhongQin(self):
        self.person.ACGCharDefaultEvent(10000205)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGAskAcceptMission(0,0,1003034)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(175.5,113.9)
        
        self.person.ACGCharDefaultEvent(10000207)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(10000207,0,1003034,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
    
    #任务20--智力考验
    def ZhiLiKaoYan(self):
        self.person.ACGMissionEnterMovie(20,1,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionMovieEnd(20)
        gevent.sleep(2)
        self.person.ACGIdle()
        self.person.ACGMissionEnterMovie(20,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(165,132,20)
        
        self.person.ACGCharDefaultEvent(10000205)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(10000205,0,1003020,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
    
    #任务21--切磋武艺
    def QieCuoWuYi(self):
        self.person['MissionIsFinish'] = 0   
        #self.person['monsterdic'] = {}
        self.person.ACGAskChangeScene()
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
                 
        #XXXXXXXXXXXXXX
        nCurrentScene = self.person.m_CurrentSceneID
        
        self.person.ACGENTERSCENE(1)
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Battle(155,128,2)
        
        i = 1 # 由于大于120秒后副本会自动退出，所以打怪时间不能超过120秒
        while self.person['MissionIsFinish'] != 1:
            i=i+1
            self.Battle(155,128,2)
            gevent.sleep(0)
            if i>5:
                break
        
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        
        #self.person['monsterdic'] = {}
        
        #XXXXXXXXXXXXXX
        timeout = time.time()
        while nCurrentScene == self.person.m_CurrentSceneID:
            gevent.sleep(1)
            self.person.ACGIdle()
            if time.time()-timeout>15:
                break
        
        self.person.ACGAskChangeScene()
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGENTERSCENE(1)
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(165,132)
        
        self.person.ACGCharDefaultEvent(10000205)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(10000205,0,1003021,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
    
    #任务22--绝世神功
    def JueShiShenGong(self):
        self.person.ACGCharDefaultEvent(10000205)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGAskAcceptMission(0,0,1003022)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGCharDefaultEvent(10000205)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(10000205,0,1003022,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
    
    #任务23--求救之人
    def QiuJiuZhiRen(self):
        self.person.ACGCharDefaultEvent(10000205)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGAskAcceptMission(0,0,1003023)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(128.9,138.2,18)
        
        self.Move(103.6,134.6,18)
        
        self.Move(101.1,134.2,6)
        
        self.person.ACGCharDefaultEvent(56)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(56,0,1003023,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        
    #任务24--黑衣绑匪
    def HeiYiBangFei(self):
        self.person['MissionIsFinish'] = 0
        self.person.ACGCharDefaultEvent(56)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGAskAcceptMission(0,0,1003024)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(117,126.7)
        
        self.Battle(117,126.7,3,u'黑衣人')
        
        while self.person['MissionIsFinish'] != 1:
            self.Battle(117,126.7,3,u'黑衣人')
            gevent.sleep(0)
        
        self.Move(102,133.5)
        
        self.person.ACGCharDefaultEvent(56)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(56,0,1003024,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
      
    #任务25--酒后吐真言
    def JiuHouTuZhenYan(self):
        self.Move(103.9,114)
        self.person.ACGCharDefaultEvent(10000208)#开始喝酒
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        self.person.ACGCharDefaultEvent(10000208)
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        self.person.ACGCharDefaultEvent(10000208)
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        
        self.Move(101.1,134.2)
        
        self.person.ACGCharDefaultEvent(56)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(56,0,1003026,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
       
    #任务26--小心行事
    def XiaoXinXingShi(self):
        self.person.ACGCharDefaultEvent(56)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGAskAcceptMission(0,0,1003027)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(98.3,120.3,10)
        self.Move(65.8,124.8,10)
        self.Move(51.1,139.9,10)
        self.Move(49,142,10)
        
        self.person.ACGCharDefaultEvent(10000209)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(10000209,0,1003027,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
    
    #任务27--关心佳人
    def GuanXinJiaRen(self):
        self.person.ACGCharDefaultEvent(10000209)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGAskAcceptMission(0,0,1003029)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(50,143,5)
        
        self.person.ACGCharDefaultEvent(10000210)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(10000210,0,1003029,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
    
    #任务28--获取图纸
    def HuoQuTuZhi(self):
        self.person['MissionIsFinish'] = 0
        self.person.ACGCharDefaultEvent(10000210)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGAskAcceptMission(0,0,1003030)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(67,148.7,10)
        
        self.Battle(67,148.7,3,u'一品堂头目')

        while self.person['MissionIsFinish'] != 1:
            self.Battle(67,148.7,3,u'一品堂头目')
            gevent.sleep(0)
        
        self.Move(50,143,10)
        
        self.person.ACGCharDefaultEvent(10000210)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(10000210,0,1003030,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
    
    #任务29--大战恶人
    def DaZhanERen(self):
        #self.person['monsterdic'] = {}
        self.person['MissionIsFinish'] = 0
        self.person.ACGAskChangeScene()
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        
        #XXXXXXXXXXXXXX
        nCurrentScene = self.person.m_CurrentSceneID
        
        self.person.ACGENTERSCENE(1)
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Battle(48,143,3)

        while self.person['MissionIsFinish'] != 1:
            self.Battle(48,143,3)
            gevent.sleep(0)
        
        self.person.ACGMissionEnterMovie(24,1,0)
        gevent.sleep(1)
        self.person.ACGIdle()
        
        self.person.ACGMissionPosChange(24,44.7,140.9)
        gevent.sleep(0)
        self.person.ACGIdle()
        
        self.person.ACG_EXECUTESCRIPT(1100020,u'OnMovieEnd',[1,1100020,24,2])
        gevent.sleep(0)
        self.person.ACGIdle()
        self.person.ACGMissionEnterMovie(24,0,0)
        gevent.sleep(0)
        self.person.ACGIdle()

        #self.person['monsterdic'] = {}
        
        #XXXXXXXXXXXXXX
        timeout = time.time()
        while nCurrentScene == self.person.m_CurrentSceneID:
            gevent.sleep(1)
            self.person.ACGIdle()
            if time.time()-timeout>10:
                break
        
        self.person.ACGAskChangeScene()
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGENTERSCENE(1)
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.Move(50.5,153)
        
        self.person.ACGCharDefaultEvent(10000216)
        gevent.sleep(2)
        self.person.ACGIdle()
        
        self.person.ACGMissionSubmit(10000216,0,1003032,0,0)
        gevent.sleep(2)
        self.person.ACGIdle()
        