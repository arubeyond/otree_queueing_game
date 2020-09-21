from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random
import numpy as np
random.seed(0)
np.random.seed(seed=0)


def make_matching():
    R = 2  #=Constants.num_rounds
    N = 3  #=num_demo_participants
    G = [2 for r in range(R)]  #=num of players in group
    
    #for r in range(R):
    #    while True:
    #        G[r] = np.random.poisson(5)
    #        if G[r]<=N:break
    
    B = [(n+1) for n in range(N)]
    matrix = [[] for r in range(R)]
    for r in range(R):
        g = G[r]
        matrix[r].append([])
        ids = [(n+1) for n in range(N)]
        for i in range(N%g):
            idx = np.random.randint(len(B))
            ids.remove(B[idx])
            matrix[r][0].append(B.pop(idx))
            if not B:B = [(n+1) for n in range(N)]
        np.random.shuffle(ids)
        for i in range(N//g):
            matrix[r].append(ids[i*g:(i+1)*g])
    #休みを平均化したもの、R,N,Gを内生化
    return matrix

doc = """
Queueing Game for Determ arrival and Determ service
"""
matching_matrix = make_matching()


class Constants(BaseConstants):
    name_in_url = 'queueing_game'
    players_per_group = 3  
    #グループ人数は上のmake_matching関数で変更する。ここは参加被験者数と一致させる
    num_rounds = 2  #default 30

    instructions_template = 'queueing_game/instructions.html'
    service_time_fix = 4 #for display
    T = 20 #max of time


class Subsession(BaseSubsession):
    def creating_session(self):
        #self.group_randomly()
        self.set_group_matrix(matching_matrix[self.round_number-1])
        #自前のランダム化関数でうまくいくか
        """
    def vars_for_admin_report(self):
        #arrival time distribution?
        #mean payoff?
        """


class Group(BaseGroup):
    social_payoff = models.IntegerField()
    overwork = models.IntegerField()
    #こっちでサービス時間の設定を行う
    def calc_waitingtime(self):
        workload = 0
        for t in range(Constants.T+1):
            workload = max(0,workload-1)
            arrival_players = []
            for player in self.get_players():
                if player.arrival_time == t:
                    arrival_players.append(player)
            random.shuffle(arrival_players)
            for player in arrival_players:
                player.waiting_time = workload
                workload += player.service_time
            
        self.overwork = workload
        self.social_payoff = sum([player.waiting_time for player in self.get_players()])
        



class Player(BasePlayer):
    arrival_time = models.IntegerField(min=0,max=Constants.T, doc="""The time player arrived""")
    service_time = models.IntegerField(initial=4)
    waiting_time = models.IntegerField()
