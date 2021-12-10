# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城
import random

def create_poke():
    nums = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
    card_types = ["红桃", "黑桃", "方片", "梅花"]
    full_poke_cards = []
    for i in card_types:
        for n in nums:
            full_poke_cards.append([i,n])

    return full_poke_cards

def issue_cars(*args):
    """
    发牌
    :param args: 玩家姓名列表
    :return:
    """
    # 1. 洗牌
    # 2. 发牌
    card_list = create_poke()
    random.shuffle(card_list)
    print(card_list)
    players = {}.fromkeys(args,[])
    for p in players:
        random_cards = random.sample(card_list,3)
        print(random_cards)
        players[p] = random_cards # 给用户发牌
        # 已发了的牌要删掉
        for i in random_cards:
            card_list.remove(i)

    return players




player_cars = issue_cars("Alex","Jack")
print(player_cars)