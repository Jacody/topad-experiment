from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

class Constants(BaseConstants):
    name_in_url = 'livepage'
    players_per_group = 3
    num_rounds = 1
    endowment = c(10)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    def get_decisions(self):
        return {p.id_in_group: p.decision for p in self.get_players()}

class Player(BasePlayer):
    decision = models.BooleanField(
        choices=[
            [True, 'Annehmen'],
            [False, 'Ablehnen']
        ],
        widget=widgets.RadioSelect,
        label='Möchten Sie den Betrag annehmen?'
    )

    def live_decision(self, data):
        self.decision = data['decision']
        decisions = self.group.get_decisions()
        return {0: decisions}  # Send decisions to all players
