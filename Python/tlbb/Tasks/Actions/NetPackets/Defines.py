# -*- coding: utf-8 -*-
PACKET_NAME = \
    """
        //Lua使用
        PACKET_CG_LUA_COMMON = 9998,        //请求lua使用
        PACKET_GC_LUA_COMMON = 9999,        //推送lua使用

        //仓库
        PACKET_CG_BankAcquireList = 277,                //向服务器获取仓库数据
        PACKET_GC_BankAcquireList = 1385,               //银行（仓库）中的物品发送给客户端
        PACKET_CG_AskExpandBank = 1736,                 //请求扩展仓库
        PACKET_GC_RetExpandBank = 1737,                 //推送扩展仓库
        PACKET_CG_BankSwapItem = 16,                    //请求仓库中交换物品、仓库与背包交换物品；
        PACKET_GC_BankSwapItem = 610,                   //推送仓库中交换物品、仓库与背包交换物品；
        PACKET_CG_BankAddItem = 1600,                   //请求仓库中加物品
        PACKET_GC_BankAddItem = 1224,                   //推送仓库中加物品
        PACKET_CG_BankRemoveItem = 524,                 //请求仓库中移除物品
        PACKET_GC_BankRemoveItem = 480,                 //推送仓库中移除物品
        PACKET_GC_BankItemInfo = 879,                   //推送仓库中物品信息


        //正式login登录
        PACKET_CL_Connect = 355,                        //客户端连接login服务器进行登录(检测排队情况)
        PACKET_LC_RetConnect = 311,                     //login服务器返回结果（返回login的Ip地址和端口号）
        PACKET_CL_AskLogin = 299,                       //客户端登录（检测版本号，20秒重复登录）
        PACKET_LC_RetLogin = 223,                       //login服务器返回结果
        PACKET_CL_AskCharList = 711,                    //客户端请求该账号的角色列表
        PACKET_LC_RetCharList = 319,                    //login服务器返回该账号的角色列表结果
        PACKET_CL_AskCreateChar = 522,                     //客户端请求创建角色
        PACKET_LC_RetCreateChar = 440,                  //login服务器返回创建角色结果
        PACKET_CL_AskCharLogin = 426,                   //客户端请求使用该角色进入游戏    
        PACKET_LC_RetCharLogin = 38,                    //login服务器返回角色进入游戏结果
        PACKET_CL_AskQuitQuene = 1067,                  //客户端请求退出排队
        PACKET_CL_AskDeleteChar = 240,                  //客户端请求删除角色
        PACKET_LC_RetDeleteChar = 707,                  //login服务器返回删除角色结果  
        PACKET_LC_Status = 554,                         //login服务器返回客户端排队情况 
        PACKET_LC_ReConnectData= 1871,                  //从登陆界面断线重连
        //连接
        PACKET_CG_CGConnect = 1166,//请求连接
        PACKET_GC_GCConnect = 643,//推送连接
        //心跳
        PACKET_CG_HeartBeat = 1416, //请求心跳
        PACKET_GC_HeartBeat = 738,//推送心跳
        PACKET_CG_NTP = 883,//请求NTP时间同步
        PACKET_GC_NTP = 359,//推送NTP时间同步
        PACKET_GC_NETCHECK=945,//向客户端发送下行网络检测

        //操作返回
        PACKET_GC_OPERATE_RESULT = 309,//推送操作返回
        //场景处理
        PACKET_CG_ENTERSCENE = 722,//客户端试图进入某个场景时发送给服务器的请求信息
        PACKET_GC_ENTERSCENE = 649,//服务器发给客户端进入场景的确认信息
        PACKET_CGAskChangeScene = 205,//客户端请求改变场景
        PACKET_GC_NOTIFYCHANGESCENE = 680,//服务器通知客户端可以改变场景
        PACKET_GC_RETCHANGESCENE = 553,//服务器回应客户端的场景变换请求

        //怪物刷新
        PACKET_GC_NEWMONSTER = 946,//有新的怪物进入自己的视野范围
        PACKET_GC_NEWMONSTER_MOVE = 714,//创建移动的怪
        PACKET_GC_NEWMONSTER_DEATH = 932,//创建死亡的怪
        PACKET_GC_NEWMONSTER_SKILLCHANNEL=809,//创建引导技能中的怪物

        //其他玩家刷新
        PACKET_GC_NEWPLAYER = 732,//有新的玩家进入自己的视野范围
        PACKET_GC_NEWPLAYER_MOVE = 1247,//创建移动的玩家
        PACKET_GC_NEWPLAYER_DEATH = 214,//创建死亡的玩家
        PACKET_GC_NEWPLAYER_SKILLCHANNEL = 557,//创建技能引导中的角色
        //属性
        PACKET_CG_CHARASKBASEATTRIB = 365,//请求基础属性
        PACKET_GC_CHARBASEATTRIB = 642,//回复基础属性

        PACKET_CG_CHARASKDETAILATTRIB = 414,//请求详细属性
        PACKET_GC_CHARDETAILATTRIB = 538,//回复详细属性
        
        //个人设置
        PACKET_CG_MODIFYSETTING = 245,//个性化设置信息
        PACKET_CG_ASKSETTING = 886,//请求设置信息
        PACKET_GC_RETSETTING = 1179,//返回设置信息

        //社交
        PACKET_CG_RELATION = 333,//请求好友相关消息
        PACKET_GC_RELATION = 1254,//推送好友相关消息
        PACKET_CG_FINGER = 672,//请求查找玩家
        PACKET_GC_FINGER = 697,//推送查找玩家


        //道具
        PACKET_CG_ASKITEMINFO = 263,//请求道具信息
        PACKET_GC_ITEMINFO = 1062,//推送道具信息

        //邮件
        PACKET_CG_ASKMAIL = 715,            //请求邮件，主要是第一次登录需要，以后再做
        PACKET_GC_RET_MAIL_NEW = 1270,    // 邮件详细信息  

        //移动
        PACKET_CG_CHARMOVE = 694,//请求角色移动
        PACKET_GC_CHARMOVE = 845,//推送角色移动
        PACKET_GC_CHARMOVERESULT = 1434,//推送角色移动结果
        PACKET_GC_OBJ_TELEPORT = 1293,//推送角色传送
        PACKET_GC_ARRIVE = 799,//推送角色到达
        PACKET_CG_CHARJUMPFLY=1748,//请求轻功飞行
        PACKET_GC_CHARJUMPFLY=1749,//返回轻功飞行

        //移除单位
        PACKET_GC_DELOBJECT = 681,//删除OBJ
        PACKET_GC_DELALLOBJ = 964,//切场景时候，一个整包代替之前的多个PACKET_GC_DELOBJECT包
        PACKET_GC_CHAR_DOACTION=572,//让某角色做一个指定动作
        //技能
        PACKET_CG_CHARUSESKILL = 870,//通知server使用技能
        PACKET_GC_CHARSKILL_SEND = 651,//技能发招
        PACKET_GC_CHARSKILL_DEPLETE_REFIX = 909,//使用技能消耗修正
        PACKET_GC_DETAIL_HEALS_AND_DAMAGES = 1352,//hp,mp,rage,strikePoint的变化，供客户端显示伤害和治疗用
        PACKET_GC_CHARSKILL_GATHER = 323,//技能聚气
        PACKET_GC_NEWSPECIAL = 331,//特殊对象 陷阱
        PACKET_GC_CHARSKILL_LEAD = 912,//技能引导
        PACKET_GC_CHAR_BUFF = 151,//持续性效果
        PACKET_GC_CHAR_BUFFUPDATE = 152,//效果修改
        PACKET_GC_CHAR_DETAIL_BUFF = 367,//持续性效果的详细数据 数据量大 只发给自己
        PACKET_GC_CHAR_DIRECT_IMPACT = 1148,//效果一次性效果
        PACKET_GC_CHARMODIFYACTION = 907,//干扰动作的执行
        PACKET_GC_CHARSKILL_MISSED = 1024,//技能没有命中
        PACKET_GC_TARGET_LIST_AND_HIT_FLAGS = 107,//目标列表和击中与否(已经废弃),用于客户端演示子弹和击中与否
        PACKET_GC_CHAR_CHARGE = 1563,//冲锋 拉人
        PACKET_GC_CHAR_STOPACTION=316,//停止动作

        PAKCET_CG_CHAR_STOP_LOGIC=334,//客户端请求停止当前逻辑
        PACKET_CG_CHAR_ASK_IMPACTLIST=547,//取得角色的impactList
        PACKET_GC_CHAR_IMPACT_LIST_UPDATE = 1344,//更新效果列表 (简要信息  广播用)
        PACKET_GC_DETAIL_IMPACT_LIST_UPDATE = 1197,//更新效果列表(详细信息 指给玩家自己发)

        PACKET_CG_ASKDETAILSKILLLIST = 695, //请求更新当前主角技能列表
        PACKET_GC_DETAILSKILLLIST = 329,//推送当前主角技能列表
        PACKET_GC_STUDYXINFA = 69,//推送学习结果
        PACKET_CG_ASKSTUDYXINFA = 131,//请求学习
        PACKET_GC_ADDSKILL = 568,//推送增加技能
        PACKET_CG_ASKADDSKILLLIST = 530, //请求更新当前主角变身技能列表
        PACKET_GC_ADDSKILLLIST = 739,//变身技能列表
        PACKET_CG_ASKCAMPAIGNCOUNT = 928,   // 活动大厅: 请求角色活动次数
        PACKET_GC_COOLDOWN_UPDATE = 929,//技能时间冷却
        PACKET_GC_RETCAMPAIGNCOUNT = 939,       // 活动大厅: 返回角色活动次数

        PACKET_GC_SPECIAL_OBJ_ACTIVE=1518,//陷阱激活
        //任务
        PACKET_GC_CHARDEFAULTEVENT = 1187,//推送Npc交互的协议
        PACKET_CG_ASKMISSIONLIST = 1058, //请求任务列表
        PACKET_GC_MISSIONADD = 1361, //添加一个任务
        PACKET_GC_MISSIONREMOVE = 594, //删除一个任务
        PACKET_GC_MISSIONMODIFY = 595, //修改一个任务
        PACKET_GC_MISSIONLIST = 593, //返回任务列表
        PACKET_CG_MISSIONSUBMIT = 1625, //递交任务
        PACKET_CG_MISSIONREWARD = 1701, //完成任务获得奖励显示
        PACKET_CG_MISSIONHAVEDONEFLAG = 734, //任务完成
        PACKET_CG_MISSION_ENTERSINGLEFUBEN = 1691, //请求进入单人副本
        PACKET_CG_NPCTRANSFER =1781, //通过传送NPC进行传送

        //ui提示 命令
        PACKET_GC_UICOMMAND = 1200, //发送客户端的某个用户接口命令
        PACKET_GC_SCRIPTCOMMAND = 1003,//推送脚本到客户端的指令
        PACKET_CG_EVENTREQUEST = 918,//查询一个脚本事件
        PACKET_CG_EXECUTESCRIPT = 418,//请求执行服务器某个脚本

        //物品拾取
        PACKET_GC_NEWITEMBOX = 679,//推送掉落报创建
        PACKET_CG_OPENITEMBOX = 913,//请求掉落报打开
        PACKET_CG_PICKITEMBOX = 159,//请求掉落报拾取
        PACKET_GC_PICKRESULT = 678,//推送掉落拾取结果

        //每月签到

        PACKET_CG_ASKMONTHLYSIGNLIST = 1674,//请求每月签到列表
        PACKET_GC_MONTHLYSIGNLIST = 1675,//推送每月签到列表
        PACKET_CG_SIGNORRESIGN = 1676,//请求单词签到
        PACKET_GC_SIGNORRESIGNRESULT = 1677,//推送单次签到
        //死亡
        PACLET_GC_DIE = 51,//推送死亡
        PACKET_GC_PLAYER_DIE = 1543, //主角死亡
        PACKET_GC_PLAYER_RELIVE = 27, //主角复活
        PACKET_CG_PLAYER_DIE_RESULT = 1370, //主角死亡的操作结果


        //特殊对象死亡或解体
        PACKET_GC_SPECIAL_OBJ_FADE_OUT = 1450,//推送特殊对象死亡或解体

        PACKET_GC_BOXITEMLIST = 1015,//推送物品列表

        //背包装备
        PACKET_CG_ASKMYBAGLIST = 415,//请求背包列表
        GCBagList = 631,//推送背包列表

        PACKET_GC_NOTIFYEQUIP = 366,//推送添加新装备
        PACKET_GC_BAGSIZECHANGE = 1182,//推送背包大小变化
        PACKET_CG_ASKMYBAGSIZECHANGE = 258,//请求背包大小变化
        PACKET_GC_DETAILEQUIPLIST = 1252,//推送自身装备信息列表
        PACKET_CG_ASKDETAILEQUIPLIST = 186,//请求自身装备信息列表
        PACKET_CG_USEEQUIP = 285,//请求使用装备
        PACKET_GC_USEEQUIPRESULT = 1419,//推送使用装备
        PACKET_CG_UNEQUIP = 1280,//请求卸下装备
        PACKET_GC_UNEQUIPRESULT = 785,//推送卸下装备
        PACKET_CG_PACKAGE_SWAPITEM = 520,//请求交换背包里的两个物品
        PACKET_GC_PACKAGE_SWAPITEM = 617,//推送交换背包里的两个物品
        PACKET_CG_PACKUP_PACKET = 391,//请求整理背包
        PACKET_GC_PACKUP_PACKET = 434,//推送整理背包

        //大混乱副本
        PACKET_CG_ASK_DAHUNLUAN = 1669,//请求大混乱副本进入
        PACKET_GC_DAHUNLUAN_SCORE = 1670,//推送大混乱副本分数
        PACKET_GC_DAHUNLUAN_ENTER = 1671,//推送大混乱副本进入


        //经验和升级
        PACKET_GC_LEVELUPRESULT = 143,    //服务器通知升级
        PACKET_GC_LEVELUP = 981,     //服务器广播升级    

        //pet 珍兽
        PACKET_GC_MANIPULATEPETRET = 880,  //请求操作珍兽的返回结果。
        PACKET_GC_DETAILATTRIB_PET = 947,  //珍兽详细属性
        PACKET_CG_SET_PETATTRIB = 843,  //通知服务器修改珍兽属性
        PACKET_CG_MANIPULATEPETRET = 674,  //请求操作珍兽
        PACKET_GC_NEWPET_MOVE = 540,  //创建移动的珍兽
        PACKET_GC_NEWPET = 1384,  //视野内 出现一只珍兽
        PACKET_GC_NEWPET_SKILLCHANNEL=163,//添加一只正在引导技能中的珍兽
        PACKET_CG_PETPROCREATEREGISTERUI = 195,  //珍兽繁殖面板的提交信息
        PACKET_CG_USEITEM = 460,  //使用物品
        PACKET_GC_USEITEMRESULT = 925,  //使用物品返回
        PACKET_GC_PETPOSSBUFINFO = 575, //附体珍兽的属性加成返回
        PACKET_GC_REMOVEPET = 135, //珍兽移除
        PACKET_GC_PETCAPTUREPROTECT = 1698, //珍兽宿主改变
        

        
        PACKET_CC_TEAM_INVITE = 384, //请求组队组队邀请   
        PACKET_CG_TEAM_APPLY = 992,//请求组队申请
        PACKET_CG_TEAM_LEAVE = 1030,//请求组队离开
        PACKET_CG_TEAM_KICK = 666,//请求组队踢出
        PACKET_CG_ASK_TEAM_INFO = 1034,//请求组队信息
        PACKET_CG_ASK_TEAM_MEMBER_INFO = 978,//请求组队成员信息
        PACKET_CG_TEAM_APPOINT = 12,//请求任命新队长
        PACKET_CG_TEAM_DISSMISS = 1124,//请求解散队伍
        PACKET_CG_TEAM_LEADER_RET_INVITE = 211,//请求队长回应
        PACKET_CG_TEAM_RET_APPLY = 782,//请求组队申请
        PACKET_CG_TEAM_RET_INVITE = 148,//请求组队邀请
        //PACKET_CG_ASK_TEAMFOLLOW = 1442,//请求组队跟随(移植lua中)
        //PACKET_CG_RETURN_TEAMFOLLOW = 160,//请求组队跟随返回(移植lua中)
        //PACKET_CG_STOP_TEAMFOLLOW = 625,//请求停止组队跟随(移植lua中)
        
        PACKET_CGW_TEAM_UPDATE_NUM = 1697,//队伍请求列表
       
        PACKET_GC_TEAM_ERROR = 1500,    //推送组队错误
        PACKET_GC_TEAM_LIST = 582,  //推送组队列表
        PACKET_GC_TEAM_LEADER_ASK_INVITE = 188,//推送队长邀请
        PACKET_GC_TEAM_ASK_INVITE = 129,//推送组队邀请
        PACKET_GC_TEAM_ASK_APPLY = 717,//推送组队申请
        PACKET_GC_TEAM_RESULT = 1000,//推送组队结果
        PACKET_GC_TEAM_MEMBER_INFO = 899,//推送组队成员信息
        //PACKET_GC_ASK_TEAMFOLLOW = 793,//推送组队跟随(移植lua中)
        PACKET_GC_RETURN_TEAMFOLLOW = 336,//推送返回组队跟随
        PACKET_GC_TEAMFOLLOW_ERROR = 28,//推送跟随错误
        //聊天
        PACKET_CG_COMMAND = 1004, //GM指令
        PACKET_CG_GMCHAT = 772, //GM聊天发送
        PACKET_GC_GMCHAT = 242, //GM聊天返回
        PACKET_CG_CHAT = 469,   //说话
        PACKET_GC_CHAT = 986,   //服务器返回
        PACKET_CG_CHATVOICE = 1721,//创建语音请求
        PACKET_GC_CHATVOICE = 1722,//创建语音返回
        PACKET_CG_CHATVOICETOSTR = 1730,//语音转文字
        PACKET_GC_CHATVOICETOSTR = 1731,//推送语音转文字
        PACKET_CG_CITYLOCATION = 1734,//城市定位

        //=====================神器==============
        PACKET_CG_ASK_UPGRADE_MYSTICALWEAPON = 1672,    //神器升阶
        PACKET_GC_MYSTICALWEAPON_UPGRADE_RESULT = 1673, //神器升级结果

        //PACKET_CG_ASK_LEVELUP_MYSTICALWEAPON = 2040,    //神器升级
        //PACKET_GC_MYSTICALWEAPON_LEVELUP_RESULT = 2030, //神器升级结果

        PACKET_CG_MYSTICALWEAPON_SKILL_ACTIVED = 1678,  //神器技能激活
        PACKET_GC_MYSTICALWEAPON_SKILL_ACTIVED_RESULT = 1679,  //神器技能激活结果
        //神器淬炼
        PACKET_CG_ASK_SHENQI_CUILIAN_INFO = 1685, //请求神器淬炼数据
        PACKET_GC_SHENQI_CUILIAN_RESULT = 1686, //神器淬炼结果

        PACKET_CG_MISSION_MOVIE_END = 1680, //单人副本结束

        PACKET_CG_CHANGESCENEBYMAP = 1681, //通过地图切换场景

        PACKET_CG_MISSION_GUIDE_END = 1682, //引导任务结束
        PACKET_CG_MISSION_POS_CHANGE = 1683, //玩家位置传送 (基于剧情)

        PACKET_CG_MISSION_ENTER_MOVIE = 1684, //玩家进入/退出剧情


        PACKET_CG_SHIMEN_ASKHELP = 1687,//师门任务请求好友帮助
        PACKET_CG_SHIMEN_HELP_LIST = 1688,//师门任务请求帮助所有好友
        PACKET_GC_SHIMEN_ASK_HELP = 1689,//师门任务：服务器推送好友请求
        PACKET_CG_MISSIONBANDON = 2, //放弃任务
        PACKET_GC_ASK_SERVER_TIME = 1116,//同步服务器时间
        PACKET_CG_ASK_SERVER_TIME = 102,//同步服务器时间
        PACKET_CG_ASK_ACCEPT_MISSION=911,//请求接受任务d
        PACKET_CG_MISSION_DELIVERY = 1690,//任务交付东西

        //帮会
        PACKET_CG_GUILD = 746, //请求帮会信息 
        PACKET_GC_GUILD = 496, //返回帮会信息
        PACKET_CG_GUILD_JOIN =373,//申请加入工会
        PACKET_CG_GUILD_ASKMEMBERINFO=204, //查看工会成员
        PACKET_CG_GUILD_APPLY = 1437, //建立工会
        PACKET_GC_GUILD_APPLY = 1053,//建立工会
        PACKET_GC_GUILD_LIST = 410,//返回帮会列表
        PACKET_GC_GUILD_AUTHORITY=926,//帮会权限
        PACKET_GC_GUILD_ERROR = 1203,//返回帮会错误
        PACKET_GC_GUILD_RETURN = 1274,//返回帮会操作结果（enmu）
        
        //城市
        PACKET_CG_CITYASKATTR = 228, //请求城市信息 
        PACKET_GC_CITYATTR = 802, //返回城市信息



        //坐骑
        PACKET_CG_RIDEBAGMOVEITEM = 251,//骑乘背包间移动
        PACKET_CG_ASKRIDEBAGINFO = 1020,//请求骑乘背包信息
        PACKET_GC_RIDEBAGINFO = 481,//骑乘背包信息返回
        PACKET_CG_ASKSETCURPOINT = 1065,//设置当前的骑乘激活点
        PACKET_GC_SETCURPOINT = 756,//返回设置当前的骑乘激活点结果
        PACKET_GC_RIDE_OVERTIMELISTINFO = 1692,//请求到期骑乘道具列表
        PACKET_GC_RIDEBAGMOVEITEMRESULT = 513,//骑乘背包间移动返回结果
        // 老三环副本
        PACKET_CG_ASK_LAOSANHUAN = 1693,    // 请求老三环副本
        PACKET_GC_TEAMMATESCONDITION = 1694,    // 进副本时, 检测队友条件
        // 副本大厅
        PACKET_CG_ASKCOPYSCENECOUNT = 1695,     // 副本大厅: 请求所有副本次数
        PACKET_GC_RETCOPYSCENECOUNT = 1696,     // 副本大厅: 返回所有副本次数
        PACKET_CG_FINDNPC = 1699,       // 寻找NPC
        PACKET_GC_RETFINDNPC = 1700,        // 返回寻找NPC

        //脚本控制转向
        PACKET_GC_CHANGEDIRECTION = 191, //服务器脚本修改朝向

        ///装备强化相关
       
        //请求装备位强化
        PACKET_CG_EQUIPSLOTENHANCE = 1702,//请求装备位强化
        //服务器返回装备位信息
        PACKET_GC_EQUIPSLOTINFO = 1703,//服务器返回装备位信息
        //初始化时请求装备位强化信息
        PACKET_CG_ASKEQUIPSLOTINFO = 1704,//初始化时请求装备位强化信息

        //装备熔炼相关
        PACKET_CG_REQ_FURNACE = 1715,//请求熔炼装备
        PACKET_CG_REQ_FURNACE_REWARD =1716,//请求领取熔炼宝箱
        PACKET_GC_RESP_FURNACE_RESULT =  1717,//请求熔炼后返回结果
        PACKET_GC_RESP_FURNACE_REWARD = 1719,//请求熔炼领取宝箱返回结果
        //时装
        PACKET_GC_LIMITFASHIONTIMEOUT = 1709,// 限时时装到期信息
        PACKET_CG_CHANGEFASHION = 1710,// 换装
        PACKET_GC_FASHIONINFO = 1711,// 换装结果反馈or染色结果反馈
        PACKET_GC_FASHIONINFOS = 1712,// 玩家拥有的时装信息及解锁染色信息
        PACKET_CG_FASHIONCOLOR = 1713,// 时装染色
        PACKET_CG_ASKFASHIONINFO = 1718,// 请求时装和染色信息        PACKET_MAX = ushort.MaxValue,
        PACKET_GC_GETFASHION = 1723, //获得新的时装， 或者延长已有时装的使用时间

        // 镶嵌
        PACKET_GC_GEM_CONTAINER = 1550,// 推送镶嵌
        PACKET_CG_ASK_GEM_CONTAINER = 1154,// 请求镶嵌

        PACKET_CG_USE_GEM = 729,        // 镶嵌/卸下/提升
        PACKET_GC_GEM_OPERATE_RESULT = 1724,    // 宝石操作结果

        PACKET_CG_ASKPETTUJIANINFO = 1725,    // 珍兽图鉴请求
        PACKET_GC_RETASKPETTUJIANINFO = 1726,    // 珍兽图鉴返回
        PACKET_CG_USESHOUHUN = 1727,    // 使用兽魂

        PACKET_CG_COMPOSE_GEM = 1414,   // 宝石合成

        PACKET_CG_ASK_QUIT = 633,

        PACKET_CG_HEROCARD_INFO = 1738,//请求服务器玩家卡牌相关信息
        PACKET_GC_HEROCARD_INFO = 1739,//服务器返回玩家卡牌信息
        PACKET_CG_ACTIVE_HERO = 1740,//请求服务器激活玩家卡牌
        PACKET_GC_MATERIAL_LIST = 1741,//服务器返回材料列表
        PACKET_CG_HERO_LEVELUP = 1742,//请求卡牌升级

        PACKET_CG_ASK_PRIVATEINFO = 235,//请求玩家资料
        PACKET_GC_PRIVATEINFO = 290,//玩家资料返回
        PACKET_CG_APPLY_PRIVATEINFO = 701,//玩家修改资料

        PACKET_CG_CGW_PACKET = 832, //客户端直接发给服务器world的包
        PACKET_GC_WGC_PACKET = 641, //由world直接发往客户端的包(帮会宣战相关)

        PACKET_CG_DISPEL_BUFF = 602, //buff解除

        PACKET_CGW_REQ_LASTRELATIONINFO = 1816, //最近联系人列表
        PACKET_WGC_RET_LASTRELATIONINFO = 1818, //最近联系人列表返回

        PACKET_CG_ASKDETAILXIULIAN = 927,//请求帮会修炼
        PACKET_GC_ASKDETAILXIULIAN = 487,//返回帮会修炼

        PACKET_GC_KICK              = 1875,//踢人返回
        PACKET_CG_TSS_DATA          = 1880,//发送TSS数据
        PACKET_GC_TSS_DATA          = 1881,//接收TSS数据

        PACKET_GC_UPDATE_ACHIEVEMENT = 853,//成就信息更新；
        PACKET_CG_ACHIEVEMENT = 190,//领取成就

        PACKET_CG_ASKBREAKOUTLEVEL = 1954,//请求突破等级
        PACKET_GC_RETBREAKOUTLEVEL = 1962,//请求突破等级返回

        PACKET_CG_FIRSCENE_FINISH = 2040, // 标记序章结束
        PACKET_CG_FIRSCENE_CHANGESCENE = 2042, // 切出序章场景

        PACKET_MAX = 999999,//协议号长度
        
        
        ===================LUA================
        PACKET_GC_MISSIONLIST = 593, //返回任务列表
PacketIDData[593] = {priority = 1}, //不写这一行等同于priority=0

 PACKET_GC_MISSIONREMOVE = 594, //删除一个任务
PacketIDData[594] = {priority = 1}, //不写这一行等同于priority=0

 PACKET_GC_MISSIONADD = 1361, //添加一个任务
PacketIDData[1361] = {priority = 1}, //不写这一行等同于priority=0

 PACKET_GC_MISSIONMODIFY = 595, //修改一个任务
PacketIDData[595] = {priority = 1}, //不写这一行等同于priority=0

 PACKET_CG_ASKMISSIONLIST = 1058, //请求任务列表
 PACKET_CG_MISSIONSUBMIT = 1625, //递交任务
 PACKET_CG_ASK_ACCEPT_MISSION = 911, //请求接受任务
 PACKET_CG_MISSIONHAVEDONEFLAG = 734, //任务完成
 PACKET_CG_PICSHAREDONE = 1963, //图片分享任务
 PACKET_CG_PAOHUAN_HELP = 1977, //跑环任务帮助操作
 PACKET_GC_PAOHUAN_HELP = 1978, //跑环任务帮助操作
PacketIDData[1978] = {priority = 1}, //不写这一行等同于priority=0

//云游商人（抽卡）
 PACKET_CG_ASKDRAWCARDINITDATA = 1743,//抽卡初始数据
 PACKET_GC_RETDRAWCARDINITDATA = 1744,
PacketIDData[1744] = {priority = 1}, //不写这一行等同于priority=0

 PACKET_CG_ASKDRAWCARD = 1745,//请求抽卡
 PACKET_GC_RETDRAWCARD = 1746,
PacketIDData[1746] = {priority = 1}, //不写这一行等同于priority=0

 PACKET_CG_ASK_BLACK_MARKET = 1768, // 客户端请求黑市商人有关消息 
 PACKET_GC_BLACK_MARKET_LIST =1769, // 黑市商店物品信息 
PacketIDData[1769] = {priority = 1}, //不写这一行等同于priority=0
 PACKET_CG_BLACKMARKET_BUY = 1770, // 请求黑市商店购买物品  
 PACKET_GC_BLACKMARKET_REFRESH = 1771, // 黑市商店通知客户端刷新列表  
PacketIDData[1771] = {priority = 1}, //不写这一行等同于priority=0

 PACKET_CL_ASKNOTICE = 1753,           // 客户端登陆请求公告   
 PACKET_LC_RETNOTICE = 1752,           // login服务器返回的公告 
PacketIDData[1752] = {priority = 1}, //不写这一行等同于priority=0

// 结拜相关协议 
 PACKET_CG_SWORN_BROTHER_INFO = 1848, //请求结拜信息 
 PACKET_GC_SWORN_BROTHER_INFO = 1850, //结拜信息 
PacketIDData[1850] = {priority = 1}, //不写这一行等同于priority=0
 PACKET_GC_SWORN_UPDATE_VOTER_DATA = 1873, //服务器更新投票人的信息  CGBrother
PacketIDData[1873] = {priority = 1}, //不写这一行等同于priority=0
 PACKET_CG_BROTHER_MATTERS = 1856, //请求或者更改结拜事宜 
 PACKET_GC_BROTHER_MATTERS = 1857, //收到结拜事宜 
PacketIDData[1857] = {priority = 1}, //不写这一行等同于priority=0
 PACKET_CG_CALL_BROTHER = 1860, //请求召集成员  
 PACKET_GC_CALL_BROTHER = 1863, //回复召集成员  
PacketIDData[1863] = {priority = 1}, //不写这一行等同于priority=0
 PACKET_CG_SWORN_CHANGE_MINGHAO = 1972, //修改江湖名号   
 PACKET_CG_MODIFY_JIANGHUZIHAO = 1974, //修改江湖字号   

// 邮件 
 PACKET_CG_ASK_MAIL_LIST = 960, //请求邮件列表 
 PACKET_GC_RET_MAIL_LIST = 961, //邮件回复协议  
PacketIDData[961] = {priority = 1}, //不写这一行等同于priority=0
 PACKET_CG_ASK_MAIL_NEW = 962, //请求邮件详细信息信息 
 PACKET_GC_NOTIFY_MAIL_NEW = 968, //服务器通知有新邮件了
PacketIDData[968] = {priority = 1}, //不写这一行等同于priority=0   
 PACKET_CG_GET_MAIL_APPEND = 1363, //领取邮件附件  
 PACKET_GC_RET_MAIL_NEW_OPT = 1632, //领取邮件附件返回协议 
PacketIDData[1632] = {priority = 1}, //不写这一行等同于priority=0     
 PACKET_CG_ONEKEY_GET_MAIL_APPEND = 1944, //一键领取邮件附件  CGWNewDelOrBack
 PACKET_CG_MAIL_DEL_OR_BACK = 966,  // 删除邮件

//仓库
 CGBankAcquireList = 277,

 CGAskExpandBank = 1736,
 GCRetExpandBank = 1737,
PacketIDData[1737] = {priority = 1}, //不写这一行等同于priority=0     
 CGBankSwapItem = 16,
 GCBankSwapItem = 610,
PacketIDData[610] = {priority = 1}, //不写这一行等同于priority=0     
 CGBankAddItem = 1600,
 GCBankAddItem = 1224,
PacketIDData[1224] = {priority = 1}, //不写这一行等同于priority=0     
 CGBankRemoveItem = 524,
 GCBankRemoveItem = 480,
PacketIDData[480] = {priority = 1}, //不写这一行等同于priority=0     



//每日礼包
 CGDailyPackInfo = 2053,
 GCDailyPackInfo = 2054,
PacketIDData[ GCDailyPackInfo] = {priority = 1}


//红包
 GCRedPacketList = 1780,
 GCAddRedPacket = 1777,
PacketIDData[1777] = {priority = 1}, //不写这一行等同于priority=0     
 GCDelRedPacket = 1778,
PacketIDData[1778] = {priority = 1}, //不写这一行等同于priority=0     
 GCUpdateRedPacket = 1779,
PacketIDData[1779] = {priority = 1}, //不写这一行等同于priority=0     

 GCReceiveRedPacket = 1947,
PacketIDData[1947] = {priority = 1}, //不写这一行等同于priority=0     



//随身商店/npc商店
 CGRequestCarryStore = 1754,
 GCResponseCarryStore = 261,
PacketIDData[261] = {priority = 1}, //不写这一行等同于priority=0     
 CGShopBuy = 177,
 GCShopBuy = 94,
PacketIDData[94] = {priority = 1}, //不写这一行等同于priority=0     
 CGShopSell = 794,
 GCShopSell = 1433,
PacketIDData[1433] = {priority = 1}, //不写这一行等同于priority=0     
 CGAskItemInfo = 263,

//技能
 GCCharSkillConditionCheckInvalid = 908,

//采集
 GCCollectionInfo = 1969,
 CGRequestCollectionSkillLevelUp = 1970,

//服务器等级
 CGServerLevelInfo = 1821,
 GCServerLevelInfo = 1822,

//元宝商城
 CGYBShopBuy = 1790,
 GCYBShopBuy = 1791,
PacketIDData[1791] = {priority = 1}, //不写这一行等同于priority=0     
 CGAskYBXGList = 1792,
 GCAskYBXGList = 1793,
PacketIDData[1793] = {priority = 1}, //不写这一行等同于priority=0     

//通用商店

 CGCommonShopBuy = 1823,
 GCCommonShopBuy = 1824,
PacketIDData[1824] = {priority = 1}, //不写这一行等同于priority=0     

//分线

 GCRequestChangeLine = 1902,
PacketIDData[1902] = {priority = 1}, //不写这一行等同于priority=0     
 GCLineData = 1903,
PacketIDData[1903] = {priority = 1}, //不写这一行等同于priority=0     
 CGLineData = 1864,
 GCSceneMapping = 1948,


//排队
 CGOutLine = 1917,


//称号
 CGTitleList = 446,
 GCTitleList = 1234,
PacketIDData[1234] = {priority = 1}, //不写这一行等同于priority=0     
 GCTitleUpdate = 1891,
PacketIDData[1891] = {priority = 1}, //不写这一行等同于priority=0     
 CGTitleOperate = 1406,
 GCTitleOperate = 1892, //TODO：删掉
PacketIDData[1892] = {priority = 1}, //不写这一行等同于priority=0     
 CGGMCommand = 1004, //gm命令

//宋辽
 CGSongLiaoDetailInfo = 1826,
 GCSongLiaoDetailInfo = 1827,
 GCSongLiaoBaseInfo = 1825,

//限时
 CGRequestTimeLimitAchievement = 1867,
 GCRequestTimeLimitAchievement = 1868,
PacketIDData[1868] = {priority = 1}, //不写这一行等同于priority=0     
 CGRequestTimeLimitAchievementReward = 1869,

//月卡
 CGRequestYueKaInfo = 1883,
 GCRequestYueKaInfo = 1884,
PacketIDData[1884] = {priority = 1}, //不写这一行等同于priority=0     
 CGRequestYueKaReward = 1885,
 GCRequestYueKaReward = 1886,
PacketIDData[1886] = {priority = 1}, //不写这一行等同于priority=0     

//排行榜
 CGRequireRankList = 1854,
 GCRequireRankList = 1855,
PacketIDData[1855] = {priority = 1}, //不写这一行等同于priority=0     

 CGRequestShaXingRankInfo = 2061, //杀星排行榜
 GCRequestShaXingRankInfo = 2062, //杀星排行榜

//WebQuestion 
 PACKET_CG_CGAskQuestion = 1774, 
 PACKET_GC_GCAskQuestion = 1775,
PacketIDData[1775] = {priority = 1}, //不写这一行等同于priority=0     


//英雄试练
 PACKET_GC_HEROTRIALSSWEEPS = 1647,
PacketIDData[1647] = {priority = 1}, //不写这一行等同于priority=0     

//科举考试
 PACKET_GC_ASKEXAMBASEDATA = 1755,//科举考试基础数据
 PACKET_CG_EXAMANSWERQUESTION = 1756,//科举答题请求
 PACKET_GC_EXAMANSWERQUSERIONRESULT = 1757,//答题结果返回
 PACKET_CG_ASKEXAMTOPDATA = 1762, //请求科举排行列表
 PACKET_GC_EXAMTOPDATA = 1758,//科举排行
 PACKET_GC_EXAMISWRIGHTBROADCASE = 1759,//科举答题结果广播
 PACKET_CG_ASKTAKEREWARD = 1760,//请求领取科举奖励
 PACKET_GC_RETTAKEREWARD = 1761,//请求领奖返回
 PACKET_GC_EXAMUICLOSENOTICE = 1776,//关闭科举界面
 PACKET_CG_EXAMBASEINFO = 1931,// 请求科举会试资格，帮会求助和帮答信息
 PACKET_GC_EXAMBASEINFO = 1932,// 返回科举会试资格，帮会求助和帮答信息
 PACKET_CG_ASKHELPFORMGUILD = 1933,// 请求帮会求助
 PACKET_GC_ASKHELPFORMGUILD = 1934,// 返回帮会求助
 PACKET_CG_SENDEXAMHELPTOGUILD = 1935,// 请求帮会帮答
 PACKET_GC_SENDEXAMHELPTOGUILD = 1936,// 返回帮会帮答
 PACKET_CGW_CHECKQUESTIONANSERED = 1938, // 检测题目是否被帮答
 PACKET_WGC_CHECKQUESTIONANSERED = 1939,// 返回检测题目是否被帮答
 PACKET_WGC_SOMEONEANSERED = 1942,//有人帮答了
 PACKET_WGC_ACCESSHUISHI = 1943,//获得会试资格
 PACKET_WGC_EXAMSTYSTEMNOTICE = 1949,// 会试结束后广播排行榜

//悲酥清风UI
 PACKET_CG_DISPEL_BUFF = 602,//悲酥清风UI
//道具合成
 PACKET_CG_ASKCOMPOSE = 1782,//请求道具合成
 Packet_GC_RETCOMPOSE = 1783,//道具合成返回
PacketIDData[1783] = {priority = 1}, //不写这一行等同于priority=0    
//新手引导
 PACKET_CG_GUIDEFLOW = 1767,//新手引导上传操作数据     

//生活技能
 PACKET_CG_UPDATELIVINGSKILL = 1705, //请求更新生活技能信息
 PACKET_CG_USELIVINGSKILL = 1707, //使用生活技能
 PACKET_GC_UPDATELIVINGSKILL = 1706, //返回生活技能信息
PacketIDData[1706] = {priority = 1}, //不写这一行等同于priority=0    
 PACKET_GC_USELIVINGSKILL = 1708, //返回使用生活技能结果
PacketIDData[1708] = {priority = 1}, //不写这一行等同于priority=0    
// 宝石镶嵌
 PACKET_GC_GEM_CONTAINER = 1550, //返回宝石镶嵌信息
PacketIDData[1550] = {priority = 1},
 PACKET_CG_ASK_GEM_CONTAINER = 1154, //请求宝石镶嵌信息
PacketIDData[1154] = {priority = 1},
 PACKET_CG_USE_GEM = 729,        // 镶嵌/卸下/提升
PacketIDData[729] = {priority = 1},
 PACKET_GC_GEM_OPERATE_RESULT = 1724,    // 宝石操作结果
PacketIDData[1724] = {priority = 1}, //不写这一行等同于priority=0    

//幫會福利-工資
 PACKET_CG_ASK_BANGPAIGONGZI = 1819, //請求幫會工資
 PACKET_GC_SEND_BANGPAIGONGZI = 1820, //接收幫會工資
PacketIDData[1820] = {priority = 1}, //不写这一行等同于priority=0    

// 校场
 PACKET_CG_JIAOCHANGCHALLENGE = 1795,  // 校场发起挑战
 PACKET_GC_JIAOCHANGCHALLENGE = 1796,  // 校场发起挑战返回
 PACKET_GC_JIAOCHANGCHALLENGEDATA = 1797,  // 校场发起挑战通知对方数据
 PACKET_CG_JIAOCHANGCHALLENGEHANDLE = 1798,  // 校场挑战接受拒绝
 PACKET_GC_JIAOCHANGCHALLENGEHANDLE = 1799,  // 校场挑战接受拒绝返回
 PACKET_GC_JIAOCHANGCHALLENGENOTICE = 1800,  // 校场状态变更通知，界面

// PK相关
 PACKET_CG_CHANGE_PK_MODE_REQ = 685,  //切换PK模式
 PACKET_CG_ANTAGONIST_REQ = 64, //个人宣战
 PACKET_CG_ASKKILLERLOG = 1803, //杀人日志
 PACKET_GC_RETKILLERLOG = 1804, //返回杀人日志


//卡牌相关
//CG
 PACKET_CG_HERO_LEVELUP = 1742,//请求卡牌升级
 PACKET_CG_HEROCARD_INFO = 1738,//请求服务器玩家卡牌相关信息
 PACKET_CG_ACTIVE_HERO = 1740,//请求服务器激活玩家卡牌

 PACKET_GC_HEROCARD_INFO = 1739,//服务器返回玩家卡牌信息
PacketIDData[1739] = {priority = 1}, //不写这一行等同于priority=0    
 PACKET_GC_MATERIAL_LIST = 1741,//服务器返回材料列表  by weina 2016-12-28 11:35:24 已作废~原因：英雄谱升级材料改为进背包~
PacketIDData[1741] = {priority = 1}, //不写这一行等同于priority=0    
//支付请求余额
 PACKET_CG_ASK_BALANCE = 1887,//请求玩家账户余额
 PACKET_GC_Ret_BALANCE = 1888,//请求玩家账户余额
PacketIDData[1888] = {priority = 1}, //不写这一行等同于priority=0    

 PACKET_CG_Upload_Log = 1994,//请求玩家账户余额

//坐骑
//CG
 PACKET_CG_ASKRIDEBAGINFO = 1020,//请求骑乘背包信息
 PACKET_CG_ASKSETCURPOINT = 1065,//设置当前的骑乘激活点
 PACKET_CG_RIDEBAGMOVEITEM = 251,//骑乘背包间移动

 PACKET_GC_SETCURPOINT = 756,//返回设置当前的骑乘激活点结果
PacketIDData[756] = {priority = 1}, //不写这一行等同于priority=0    
 PACKET_GC_RIDEBAGMOVEITEMRESULT = 513,//骑乘背包间移动返回结果
PacketIDData[513] = {priority = 1}, //不写这一行等同于priority=0    
 PACKET_GC_RIDE_OVERTIMELISTINFO = 1692, //请求到期骑乘道具列表
PacketIDData[1692] = {priority = 1}, //不写这一行等同于priority=0    

//暗器
 PACKET_CG_HIDDENWEAPONOPT = 1430,
 PACKET_GC_HIDDENWEAPONOPT = 33,
PacketIDData[33] = {priority = 1}, //不写这一行等同于priority=0    


//发型和发色
 PACKET_CG_HAIROPERATE = 1801, //发型操作信息
 PACKET_GC_HAIROPERATERETURN = 1802, //发型返回
PacketIDData[1802] = {priority = 1}, //不写这一行等同于priority=0    
 PACKET_GC_HAIRCOLORCHANGE = 1805, //发型发色改变返回
PacketIDData[1805] = {priority = 1}, //不写这一行等同于priority=0    

//守卫战
 PACKET_CG_GUILDCITYDEFENDINFO = 1829,
 PACKET_GC_GUILDCITYDEFENDINFO = 1828,


//行酒令
 PACKET_CG_GUILDACTIVITYDRINK = 1845,
 PACKET_GC_GUILDACTIVITYDRINK = 1844,


//帮会商店
 PACKET_CG_BANGPAISHOPBUY = 1840,
 PACKET_GC_BANGPAISHOPINFO = 1839,
 PACKET_GC_BANGPAISHOPBUYRETURN = 1841,
 PACKET_CG_BANGPAISHOPOPEN  = 1960,  // 客户端打开帮派商店请求    没有参数

//组队平台
 PACKET_CG_ASK_PLATFORM_LIST = 1836, //请求列表项信息
 PACKET_CG_CREATE_PLATFORM = 1834, //队长 点击自动匹配/取消匹配 或 改变 目标
 PACKET_CG_OPER_PLATFORM = 1835, //没有队伍的人
 PACKET_GC_RET_PLATFORM_INFO = 1837, //服务端返回列表项信息（1836）
PacketIDData[1837] = {priority = 1}, //不写这一行等同于priority=0    
 PACKET_GC_RET_PLATFORM_RESULT = 1838, //请求匹配或取消匹配 返回的信息（1834/1835）
 PACKET_CG_ASK_TEAMGOAL = 1858, //请求目标设定信息
 PACKET_GC_RET_TEAMGOAL = 1859, //返回设定的目标信息
 PACKET_CG_ASK_TEAMFOLLOW = 1983, //请求组队跟随
 PACKET_GC_RET_TEAMFOLLOW = 1984, //返回组队跟随
PacketIDData[1984] = {priority = 1}, //不写这一行等同于priority=0  
 PACKET_CG_RET_TEAMFOLLOW_RESULT = 160, //是否同意组队跟随
 PACKET_CG_TEAMLEADER_ASK_TEAMFOLLOW = 1442, //队长自己发起组队跟随
 PACKET_CG_STOP_TEAMFOLLOW = 625,//停止组队跟随
 PACKET_GC_OTHER_ASK_TEAMFOLLOW = 793,// 其他人发起组队跟随，需要自己确定是否加入（推送组队跟随）

//阵营位置更新
 PACKET_GC_WARPOSITIONMODIFY = 1359, //返回阵营中角色的位置

//野外BOSS
 PACKET_CG_YEWAIBOSS_MAPINFO = 1889, //请求野外BOSS地图信息
 PACKET_GC_RET_YEWAIBOSS_MAPINFO = 1890, //返回野外BOSS地图信息

//帮会领地战
 PACKET_CG_GuildTerritory = 2033, //帮会领地战宣战
 PACKET_GC_GuildTerritory = 2034, //帮会领地战宣战返回
 PACKET_CG_AskGuildTerritoryInfo = 2037, //帮会领地战界面请求数据
 PACKET_GC_BackGuildTerritoryInfo = 2038, //返回帮会领地战界面请求数据

//活动大厅列表
 PACKET_CG_ASKCAMPAIGNCOUNT = 928, //获取活动大厅列表数据
 PACKET_GC_RETCAMPAIGNCOUNT = 939, //返回活动大厅列表数据
PacketIDData[939] = {priority = 1}, //不写这一行等同于priority=0    

 PACKET_CG_SETSYSTEMDATA = 1904,  //系统设置
 PACKET_CG_ASKSYSTEMDATA = 1905,  //系统设置请求
 PACKET_GC_SENDSYSTEMDATA = 1906, //系统设置回送
PacketIDData[1906] = {priority = 1}, //不写这一行等同于priority=0    
//资源找回
 PACKET_GC_FINDRES = 1912,  //资源找回回送
PacketIDData[1912] = {priority = 1}, //不写这一行等同于priority=0    
 PACKET_CG_ASKFINDRES = 1913, //资源找回请求
 PACKET_GC_FINDRESLIST = 1914 ,//资源找回请求
PacketIDData[1914] = {priority = 1}, //不写这一行等同于priority=0    
//神器相关
 PACKET_CG_GODWEAPONCAST = 1685, //请求神器淬炼信息
 PACKET_GC_GODWEAPONCASTRESULT = 1686, //返回神器淬炼信息
PacketIDData[1686] = {priority = 1}, //不写这一行等同于priority=0    
 PACKET_CG_GODWEAPONUPGRADE = 1672, //
 PACKET_GC_GODWEAPONUPGRADERESULT = 1673, //
PacketIDData[1673] = {priority = 1}, //不写这一行等同于priority=0    
 PACKET_CG_GODWEAPONOPEN = 2030, //请求神器开启信息
 PACKET_GC_GODWEAPONOPEN =  2031,//返回神器开启信息
PacketIDData[1999] = {priority = 1}, 

//玩家商店
 PACKET_CG_CONSIGNSALEITEM = 1894, //上架物品
 PACKET_CG_CANCELCONSIGNSALEITEM = 1895, //下架物品
 PACKET_CG_ASK_MYCONSIGNSALEITEM = 1896, //获取自己的上架商品列表
 PACKET_CG_ASK_CONSIGNSALEITEMINFO = 1897, // 获取拍卖物品列表
 PACKET_CG_BUY_CONSIGNSALEITEMINFO = 1898, //购买商品
 PACKET_GC_RET_MYCONSIGNSALEITEM = 1899, // 返回自己的上架商品列表
PacketIDData[1899] = {priority = 1}, //不写这一行等同于priority=0    
 PACKET_GC_ASK_CONSIGNSALEITEMINFO = 1900,
 PACKET_GC_RET_CONSIGNSALEITEMINFO = 1901, // 返回拍卖物品列表
PacketIDData[1901] = {priority = 1}, //不写这一行等同于priority=0    
 PACKET_CG_ASKCONSIGNSALEITEMBASEPRICE = 1916, // 查询物品基准价
 PACKET_GC_QUERY_ITEM_BASE_PRICE_MSG = 1919, // 返回物品基准价
PacketIDData[1919] = {priority = 1}, //不写这一行等同于priority=0    
 PACKET_GC_CONSIGNSALE_RECORD_LIST = 1927, //玩家商店交易记录
PacketIDData[1927] = {priority = 1}, //不写这一行等同于priority=0    
 PACKET_CG_ASK_CONSIGNSALE_ITEM_DETATL = 1929, //查询道具详细信息
 PACKET_CG_ASK_CONSIGNSALEPRODUCTTYPESDATA = 2016, // 获取道具列表总数量
 PACKET_GC_RET_CONSIGNSALEPRODUCTTYPESDATA = 2017, //查询道具详细信息
PacketIDData[2017] = {priority = 1}, //不写这一行等同于priority=0    

 PACKET_CG_MASTER = 1950, // 师徒逻辑请求
 PACKET_GC_MASTER = 1951, //师徒逻辑返回
PacketIDData[1951] = {priority = 1}, //不写这一行等同于priority=0    

 PACKET_CG_ASKEXPPOOLDATA = 1955, //请求多倍经验池数值
 PACKET_GC_ASKEXPPOOLDATA = 1956, //返回多倍经验池数值
PacketIDData[1956] = {priority = 1}, //不写这一行等同于priority=0    
// 货币兑换
 PACKET_CG_ASK_EXCHANGEMONEY = 1961, //兑换货币

//反贼
 PACKET_CG_ASK_REBELPOSITION = 1957, //区域地图请求反贼位置
 PACKET_GC_RET_REBELPOSITIONDATA = 1958,  //返回区域地图反贼位置
//帮会天赋
 PACKET_CG_ASK_GUILDRESEARCHlIST = 1966, // 请求帮会天赋列表
 PACKET_GC_ASK_GUILDRESEARCHlIST = 1967, // 返回帮会天赋列表
PacketIDData[1967] = {priority = 1}, //不写这一行等同于priority=0    
 PACKET_CG_ASK_UPGRADEGUILDRESEARCH = 1968, // 升级帮会天赋

//拍卖行
 PACKET_CG_ASKAUCTIONSHOPITEM = 1995, // 请求拍卖记录 或 物品信息
 PACKET_GC_RETAUCTIONSHOPITEM = 1996, // 返回请求的物品信息
PacketIDData[1996] = {priority = 1}, //不写这一行等同于priority=0    
 PACKET_CG_ASKAUCTIONITEM = 1997,//请求竞拍物品
 PACKET_CG_ASKBUYNOWPRICEITEM=1998, // 请求一口价
 PACKET_GC_RETAUCTIONSHOPRECORDLIST=2001,// 返回拍卖行交易记录
PacketIDData[2001] = {priority = 1}, //不写这一行等同于priority=0    
 PACKET_GC_RETAUCTIONSHOPREDPOINT =2004,// 返回拍卖行红点
PacketIDData[2004] = {priority = 1}, //不写这一行等同于priority=0    
 PACKET_GC_CLOSELOADINGUI = 2023,
PacketIDData[2023] = {priority = 1}, //不写这一行等同于priority=0    

//区域地图
 PACKET_CG_TRANSPORT = 1477,//传送秦皇地宫，阎王宫殿

//华山论剑
 PACKET_CG_HUASHAN_SWORD_RANK = 2015, //请求排行榜
 PACKET_GC_HUASHAN_SWORD_RANK = 2021, //返回排行榜

 PACKET_GC_HUASHAN_ICON = 2028, //华山Icon数据

 PACKET_CG_HUASHAN_MAIN = 2025, //请求华山主界面数据
 PACKET_GC_HUASHAN_MAIN = 2024, //返回华山主界面数据

 PACKET_GC_HUASHAN_RESULT = 2027,//华山奖励界面
 PACKET_GC_HUASHAN_COMBAT_REPORT = 2026, //战报

//任务答题
 PACKET_CG_MISSION_QUETIONS = 2049, //请求答题任务题库信息
 PACKET_GC_MISSION_QUETIONS = 2050, //返回答题任务题库
 PACKET_CG_ANSWER_MISSION_QUETIONS = 2051, //请求答题任务题库信息
 PACKET_GC_ANSWER_MISSION_QUETIONS = 2052, //返回答题任务题库
//帮会杀星相关
 PACKET_GC_ASK_SHAXINGFUBENINFO = 2060, //杀星副本信息

//////////////////////////////////////////////////-
//IDIP聊天信息清除
 PACKET_GC_CHATMESSAGECLEAR = 2041,// 清除聊天信息
//IDIP弹出提示信息
 PACKET_GC_IDIPSHOWWARNING = 2048,// 提示IDIP安全信息


 GCMessageBall  = 456, //消息球

        
    """
    
    
    


PACKET_LIST = PACKET_NAME.strip().splitlines()

tempList = []
 
for i in PACKET_LIST:
    if ( ('PACKET' in i) |('CG' in i) | ('GC' in i) ) & ('priority' not in i):
        tempList.append(i)
 
PACKET_LIST = tempList



PACKET_DIC = {}
ID_DIC = {}
_id_index = 0
_id = 0
for p in PACKET_LIST:
    if PACKET_LIST[_id_index].find(',') > 0:
        PACKET_LIST[_id_index] = PACKET_LIST[_id_index][:PACKET_LIST[_id_index].find(',')].strip()
    else:
        PACKET_LIST[_id_index] = PACKET_LIST[_id_index].strip()
    if PACKET_LIST[_id_index].find('=') > 0:
        
        _id = int(PACKET_LIST[_id_index][PACKET_LIST[_id_index].find('=') + 1:].strip())
        PACKET_LIST[_id_index] = PACKET_LIST[_id_index][:PACKET_LIST[_id_index].find('=')].strip()
    ID_DIC[PACKET_LIST[_id_index]] = _id
    PACKET_DIC[_id] = PACKET_LIST[_id_index]
    _id_index += 1
    _id += 1

# for i in PACKET_DIC:
#     print i , PACKET_DIC[i]



def PACKET_DEFINE(idnumber):
    return PACKET_DIC[idnumber]


def ID_DEFINE(packetname):
    return ID_DIC[packetname]


def MAX_ID():
    return ID_DIC['PACKET_MAX']
