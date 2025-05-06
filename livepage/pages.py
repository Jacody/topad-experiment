from otree.api import Page, WaitPage
from .models import Constants

class DecisionPage(Page):
    form_model = 'player'
    form_fields = ['decision']

    live_method = 'live_decision'

    def before_next_page(self):
        # Hier wird die Auszahlung festgelegt
        pass

class Results(Page):
    pass

page_sequence = [DecisionPage, Results]
