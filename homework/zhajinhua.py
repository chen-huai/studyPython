import random

class zhajinhua():
    def getYiFuPai(self):
        global yiFuPai
        num = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        hua = ['梅花', '方片', '红桃', '黑桃']
        pai = []
        for i in num:
            for each in hua:
                pai.append(each+'-'+str(i))
        random.shuffle(pai)
        yiFuPai = pai
        return yiFuPai

    def faPai(self):
        user = {
            '玩家1':[],
            '玩家2':[],
            '玩家3':[],
            '玩家4':[],
            '玩家5':[]
        }
        n = 0
        for i in range(3):
            for each in user:
                user[each].append(yiFuPai[n])
                n+=1
        print(user)




if __name__ == "__main__":
    zhajinhua.getYiFuPai
    print(yiFuPai)
    zhajinhua.faPai