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
random.seed(0)

doc = """
Queueing Game for Determ arrival and Determ service
"""


class Constants(BaseConstants):
    name_in_url = 'queueing_game'
    players_per_group = 2  #defalut:5
    num_rounds = 2  #default 30

    instructions_template = 'queueing_game/instructions.html'

    T = 20 #max of time
    service_time = 4 #service time


class Subsession(BaseSubsession):
    def creating_session(self):
        #self.group_randomly()
        matching_matrix = [[[1,3],[2,4]],[[1,4],[2,3]]]
        self.set_group_matrix(matching_matrix[self.round_number-1])
        #2人*2グループ*2ラウンドがうまくいくか
        #自前のランダム化関数でうまくいくか
        """
    def vars_for_admin_report(self):
        #arrival time distribution?
        #mean payoff?
        """


class Group(BaseGroup):
    social_payoff = models.IntegerField()
    overwork = models.IntegerField()
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
                workload += Constants.service_time  #service time
            
        self.overwork = workload
        self.social_payoff = sum([player.waiting_time for player in self.get_players()])
        


class Player(BasePlayer):
    arrival_time = models.IntegerField(min=0,max=Constants.T, doc="""The time player arrived""")
    waiting_time = models.IntegerField()
