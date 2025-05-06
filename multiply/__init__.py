from otree.api import *
from otree.app_template.models import Constants

doc = """
Your app description
"""


class C(BaseConstants):
    name_in_url = 'multiply'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    factor = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number_entered = models.FloatField()


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['number_entered']



class Results(Page):
    @staticmethod

    def vars_for_template(player: Player):
        result = player.number_entered * C.factor
        return {
            "result": result,
            "factor": C.factor,
        }


page_sequence = [MyPage, Results]
