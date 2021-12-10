import random

class pokerGame:
    def __init__(self, n=0):
        """"初始化方法"""
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
        pokerData = []
        for user in users:
            userPoker = []
            userPoker.append(user)
            for each in users[user]:
                userPoker.append(each.split('-'))
            pokerData.append(userPoker)
        # for user in users:
        #     for each in users[user]:
        #         userPoker = each.split('-')
        #         userPoker.append(user)
        #         pokerData.append(userPoker)

        return theMax






if __name__ == "__main__":
    import pandas as pd
    zjh = pokerGame()
    poker = zjh.getApoker()
    print(poker)
    user = zjh.dispensePoker()
    print(user,zjh.n)
    theMax = zjh.theMax()
    print(theMax)