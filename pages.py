from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1 
    #ラウンド1のみ表示する
    pass

class StartWait(WaitPage):
    wait_for_all_groups=True
    body_text = "Waiting for other participants."

class DecideArrivalTime(Page):
    """Player: Choose what time arrive to service"""
    def is_displayed(self):
        return self.group.id_in_subsession > 1
    form_model = 'player'
    form_fields = ['arrival_time']

class DecideWaitPage(WaitPage):
    wait_for_all_groups = True
    body_text = "Waiting for other participants to input."

class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        return self.group.id_in_subsession > 1
    after_all_players_arrive = 'calc_waitingtime'
    body_text = "Waiting for other participants to input."

class Results(Page):
    def is_displayed(self):
        return self.group.id_in_subsession > 1
    #表示したい情報の関数を定義しておいて、HTMLで呼び出す?
    """
    def vars_for_template(self):
        return dict(WaitingTime=self.player.waiting_time)
    """


page_sequence = [Introduction,StartWait, 
                 DecideArrivalTime, DecideWaitPage, 
                 ResultsWaitPage, Results]
