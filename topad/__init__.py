from otree.api import *
import time
from Completly_randomlists import generate_magic_matrix, print_matrix
from settings import SESSION_CONFIGS
from json import dumps as json_dumps, loads as json_loads
#import time
#import pytz
#from datetime import datetime, timezone, timedelta
#doc = """
#Your app description
#"""


class C(BaseConstants):
    NAME_IN_URL = 'topad'  #set the Appname
    PLAYERS_PER_GROUP = None #No Groups needed
    NUM_ROUNDS = SESSION_CONFIGS[0]['num_demo_participants'] #Set the number of Rounds equal to the amount of players
    STARTINGVALUE = 0.03 #Set the startingvalues
    matrix = generate_magic_matrix(NUM_ROUNDS)  #import the Matrix with the predefined positions
    print_matrix(matrix) #print the matrix once
    #print(SESSION_CONFIGS)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):   #define the properties of Group
    wait_for_ids = models.LongStringField(initial='[]') #For first page
    arrived_ids = models.LongStringField(initial='[]') #For first page
    winner = models.IntegerField(initial=0)
    winner_payoff = models.FloatField()
    actual_players = models.FloatField()

def unarrived_players(group: Group):
    return set(json_loads(group.wait_for_ids)) - set(json_loads(group.arrived_ids)) #For first page

class Player(BasePlayer):   #define the properties Player
    possible_payoff = models.FloatField()
    position = models.IntegerField()
    is_winner = models.BooleanField(initial=False)
    round_start = models.FloatField(initial=0.0)
    decision_time = models.FloatField()
    wait_time = models.FloatField()
    result_time = models.FloatField()

    take = models.BooleanField(
        label=" ",
        choices=[
            [True, "I want to Take it"],
            [False, "Pass and Double it"],
        ]
    )

    answer3 = models.LongStringField(label=" ")

def set_possible_payoffs(group): #Assigns how much each player can win
    player_lists = group.get_players()
    for player in player_lists:
        player.position = C.matrix[player.round_number-1][player.id_in_group - 1]
        player.possible_payoff = C.STARTINGVALUE*(2**(player.position-1))
#PAGES
class TakeOrPass(Page):

    form_model = 'player'
    form_fields = ['take']
    timeout_seconds = 15

    @staticmethod # start timer
    def vars_for_template(player):
        player.round_start = time.time()
        return dict(
            instruction_start=player.round_start
        )

    def get_context_data(self, **kwargs): # set possible payoff
        context = super().get_context_data(**kwargs)
        set_possible_payoffs(self.group)
        return context

    def error_message(self, values):
        if 'take' not in values or values['take'] is None:
            return 'This field is required.'

    @staticmethod # end timer
    def before_next_page(player, timeout_happened):
        player.decision_time = time.time() - player.round_start

def wait_page_live_method(player: Player, data):  #For first page
    group = player.group
    arrived_ids_set = set(json_loads(group.arrived_ids))
    arrived_ids_set.add(player.id_in_subsession)
    group.arrived_ids = json_dumps(list(arrived_ids_set))
    arrived_count = len(arrived_ids_set)

    if not unarrived_players(group):
        return {0: dict(finished=True, arrived_count=arrived_count)}
    return {0: dict(arrived_count=arrived_count)}

class DecisionWaitPage(Page):  #For first page

    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        # first time
        if not json_loads(group.wait_for_ids):
            wait_for_ids = [p.id_in_subsession for p in group.get_players()]
            group.wait_for_ids = json_dumps(wait_for_ids)
        return bool(unarrived_players(group))

    @staticmethod
    def live_method(player: Player, data):
        if data.get('type') == 'wait_page':
            return wait_page_live_method(player, data)

    @staticmethod
    def error_message(player: Player, values):
        group = player.group
        if unarrived_players(group):
            return "Wait page not finished"

    @staticmethod # end timer
    def before_next_page(player, timeout_happened):
        player.wait_time = time.time() - player.round_start - player.decision_time

class ResultsWaitPage(WaitPage): #define the winner when all players arrived
    @staticmethod
    def after_all_players_arrive(group: Group):
        player_lists = group.get_players() #make a list of all players
        for i in range(1, (len(player_lists)+1)): #check all players
            for player in player_lists: #check each position
                if group.winner == 0:
                    if player.position == i and player.take:
                        #The first player who took the money wins
                        player.is_winner = True
                        player.payoff = player.possible_payoff
                        group.winner_payoff = player.possible_payoff
                        group.winner = player.position
        if group.winner == 0:
            for player in player_lists:  # check each position
                if player.position == len(player_lists) and (player.take == False):
                     # if not, the last player will win
                     player.is_winner = True
                     player.payoff = player.possible_payoff
                     group.winner_payoff = player.possible_payoff
                     group.winner = player.position


class Results(Page):
    timeout_seconds = 12
    @staticmethod # end timer
    def before_next_page(player, timeout_happened):
        player. result_time = time.time() - player.round_start - player.decision_time - player.wait_time

    pass

class Feedback(Page):
    def is_displayed(player:Player):
        return (player.round_number == C.NUM_ROUNDS)

    form_model = 'player'
    form_fields = ['answer3']

class CombinedResults(Page):
    @staticmethod
    def is_displayed(player:Player):
        return player.round_number == C.NUM_ROUNDS #last Round
    form_model = 'player'

class ThankYou(Page):
    @staticmethod
    def is_displayed(player:Player):
        return player.round_number == C.NUM_ROUNDS #last Round
    pass

page_sequence = [TakeOrPass, DecisionWaitPage, ResultsWaitPage, Results, Feedback, CombinedResults ]