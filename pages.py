from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    #ラウンド1のみ表示する
    def is_displayed(self):
	    return self.round_number==1
    pass

class ReadIntroductionWait(WaitPage):
    wait_for_all_groups=True
    body_text = "Waiting for other participants."

class DecideArrivalTime(Page):
    """Player: Choose what time arrive to service"""
    
    form_model = 'player'
    form_fields = ['arrival_time']


class ResultsWaitPage(WaitPage):
    #wait_for_all_groups = True
    #これをつけるとcalc_waitingtimeがsubsession内にないというエラーが出る
    #要検証
    after_all_players_arrive = 'calc_waitingtime'
    #これだけだとグループ全員が入力を終わったら表示してしまう。
    body_text = "Waiting for other participants to input."


class Results(Page):
    #表示したい情報の関数を定義しておいて、HTMLで呼び出す
    """
    def vars_for_template(self):
        return dict(WaitingTime=self.player.waiting_time)
    """


page_sequence = [Introduction,ReadIntroductionWait, DecideArrivalTime, ResultsWaitPage, Results]
