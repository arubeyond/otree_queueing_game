from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    #ラウンド1のみ表示する
    def is_displayed(self):
	    return self.round_number==1
    pass


class DecideArrivalTime(Page):
    """Player: Choose what time arrive to service"""

    form_model = 'player'
    form_fields = ['arrival_time']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'calc_waitingtime'

    body_text = "Waiting for other participants to input."


class Results(Page):
    #表示したい情報の関数を定義しておいて、HTMLで呼び出す
    """
    def vars_for_template(self):
        return dict(WaitingTime=self.player.waiting_time)
    """


page_sequence = [Introduction, DecideArrivalTime, ResultsWaitPage, Results]
