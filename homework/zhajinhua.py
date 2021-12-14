import random

class pokerGame:
    def __init__(self, n=0):
        self.n = n

    def getApoker(self):
        global thePoker
        num = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        hua = ['梅花', '方片', '红桃', '黑桃']
        poker = []
        for i in num:
            for each in hua:
                poker.append(each+'-'+str(i))
        random.shuffle(poker)
        thePoker = poker
        return thePoker

    def dispensePoker(self):
        # while (52 - zjh.n) // 15 >= 1:
        #     msg = input('你是否继续发牌Y/N')
        #     if msg == 'Y':
                global users
                users = {
                    '玩家1':[],
                    '玩家2':[],
                    '玩家3':[],
                    '玩家4':[],
                    '玩家5':[]
                }
                # n = 0

                for i in range(3):
                    for each in users:
                        users[each].append(thePoker[self.n])
                        self.n += 1
                return users
    def theMax(self):
        # 炸金花中豹子（AAA最大，222最小）最大；其次是同花顺（AKQ最大，A23最小）；再者同花（AKQ最大，234最小）；顺子（AKQ最大，234最小）；对子（AAK最大，223最小）；单张（AKQ最大，234最小）。
        # 豹子6>同花顺5>同花4>顺子3>对子2>单张1
        pokerData = []
        for user in users:
            userPoker = []
            userPoker.append(user)
            userPoker.append(users[user])
            for each in users[user]:
                userPoker.append(each.split('-'))
            pokerData.append(userPoker)

        # for user in users:
        #     for each in users[user]:
        #         userPoker = each.split('-')
        #         userPoker.append(user)
        #         pokerData.append(userPoker)
        for m in range(len(pokerData)):
            num = []
            decor =[]
            for i in range(2,5):
                if pokerData[m][i][1] == 'J':
                    numRes = 11
                elif pokerData[m][i][1] == 'Q':
                    numRes = 12
                elif pokerData[m][i][1] == 'K':
                    numRes = 13
                elif pokerData[m][i][1] == 'A':
                    numRes = 14
                else:
                    numRes = int(pokerData[m][i][1])
                num.append(numRes)
                decor.append(pokerData[m][i][0])
            num.sort()
            decorSet = set(decor)
            if num[0] == 2 and num[1] == 3 and len(decorSet) == 1:
                num[2] == 1
                num.sort()
            numSet = set(num)
            if len(numSet) == 1:
                pokerData[m].append(6)
                pokerData[m].append('豹子')
            elif int(num[0]) + 2 == int(num[1]) + 1 == int(num[2]):
                if len(decorSet) == 1:
                    pokerData[m].append(5)
                    pokerData[m].append('同花顺')
                else:
                    pokerData[m].append(3)
                    pokerData[m].append('拖拉机')
            elif len(decorSet) == 1:
                pokerData[m].append(4)
                pokerData[m].append('同花')
            elif len(numSet) == 2:
                pokerData[m].append(2)
                pokerData[m].append('对子')
            else:
                pokerData[m].append(1)
                pokerData[m].append('单张')
            pokerData[m].append(num)
        userNum = 1
        bigger = pokerData[0]
        for i in range(len(pokerData) - 1):
            if pokerData[userNum][5] == bigger[5]:
                if int(pokerData[userNum][7][0]) + int(pokerData[userNum][7][1]) + int(pokerData[userNum][7][2]) > int(bigger[7][0]) + int(bigger[7][1]) +int(bigger[7][2]):
                    bigger = pokerData[userNum]
                if int(pokerData[userNum][7][2]) > int(bigger[7][2]):
                    bigger = pokerData[userNum]
                elif int(pokerData[userNum][7][2]) == int(bigger[7][2]):
                    if int(pokerData[userNum][7][1]) > int(bigger[7][1]):
                        bigger = pokerData[userNum]
                    elif int(pokerData[userNum][7][1]) == int(bigger[7][1]):
                        if int(pokerData[userNum][7][0]) > int(bigger[7][0]):
                            bigger = pokerData[userNum]
                        elif int(pokerData[userNum][7][1]) == int(bigger[7][1]):
                            if int(pokerData[userNum][7][0]) > int(bigger[7][0]):
                                # 这个是要判断花色
                                bigger = pokerData[userNum]
                        else:
                            bigger = bigger
                    else:
                        bigger = bigger
                else:
                    bigger = bigger
            elif pokerData[userNum][5] > bigger[5]:
                bigger = pokerData[userNum]
            else:
                bigger = bigger
            userNum += 1
        return bigger






if __name__ == "__main__":
    zjh = pokerGame()
    poker = zjh.getApoker()
    # print('扑克牌顺序：%s' % poker)
    flag = 1
    while flag == 1:
        while (52 - zjh.n)//15 >= 1:
            msg1 = input('\n你是否继续发牌Y/N')
            if msg1 == 'Y' or msg1 == 'y':
                user = zjh.dispensePoker()
                print('所有玩家牌面：%s' % user)
                theMax = zjh.theMax()
                print('赢家：%s；\n牌型：%s；\n牌面：%s' % (theMax[0], theMax[6] , theMax[1]))
            else:
                flag = 0
                break
        else:
            msg2 = input('\n你是否重新洗牌Y/N')
            if msg2 == 'Y' or msg2 == 'y':
                poker = zjh.getApoker()
                # print('扑克牌顺序：%s' % poker)
                zjh.n = 0
            else:
                flag = 0
                break

