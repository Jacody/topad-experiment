from otree.api import *
import time
from settings import SESSION_CONFIGS
from json import dumps as json_dumps, loads as json_loads
from topad import C


class C(BaseConstants):
    NAME_IN_URL = 'control'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NUM_PLAYERS = SESSION_CONFIGS[0]['num_demo_participants']
    STARTINGVALUE = C.STARTINGVALUE
    ENDVALUE = STARTINGVALUE*(2**(NUM_PLAYERS-1))

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    wait_for_ids = models.LongStringField(initial='[]')  # For first page
    arrived_ids = models.LongStringField(initial='[]')  # For first page
    pass

def unarrived_players(group: Group):
    return set(json_loads(group.wait_for_ids)) - set(json_loads(group.arrived_ids))  # For first page

class Player(BasePlayer):
    instruction_start = models.FloatField(initial=0.0)
    instruction_time = models.FloatField()
    control1_time = models.FloatField()
    control2_time = models.FloatField()
    control3_time = models.FloatField()
    control4_time = models.FloatField()
    controlWait_time = models.FloatField()
    answer1a = models.IntegerField(
        label=" ",
        choices=[
            [1, 'Player in position 5 and Player in position 7'],
            [2, 'Player in position 5'],
            [3, 'Player in position 7']
        ],
        widget=widgets.RadioSelect
    )
    answer2a = models.IntegerField(
        label=" ",
        choices=[
            [1, 'Player in position 1'],
            [2, 'Player in position 7'],
            [3, 'Player in position 5'],
        ],
        widget=widgets.RadioSelect
    )
    pass
    answer1b = models.IntegerField(
        label=" ",
        choices=[
            [1, 'Player in position 5 and Player in position 7'],
            [2, 'Player in position 5'],
            [3, 'Player in position 7']
        ],
        widget=widgets.RadioSelect
    )
    answer2b = models.IntegerField(
        label=" ",
        choices=[
            [1, 'Player in position 1'],
            [2, 'Player in position 7'],
            [3, 'Player in position 5'],
        ],
        widget=widgets.RadioSelect
    )
    pass

# PAGES

class Instructions2(Page):  # show player the instruction
    timeout_seconds = 120

    @staticmethod
    def vars_for_template(player):
        player.instruction_start = time.time()
        return dict(
            instruction_start=player.instruction_start
        )

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.instruction_time = time.time() - player.instruction_start

class Control1a(Page):
    timeout_seconds = 30

    form_model = 'player'
    form_fields = ['answer1a']

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.control1_time = time.time() - player.instruction_start - player.instruction_time
    pass

class Control2a(Page):
    timeout_seconds = 20
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.control2_time = time.time() - player.instruction_start - player.instruction_time - player.control1_time
    pass
class Control3a(Page):
    timeout_seconds = 30
    form_model = 'player'
    form_fields = ['answer2a']

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.control3_time = time.time() - player.instruction_start - player.instruction_time - player.control1_time- player.control2_time
    pass

class Control4a(Page):
    timeout_seconds = 20
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.control4_time = time.time() - player.instruction_start - player.instruction_time - player.control1_time - player.control2_time - player.control3_time
    pass

class Control1b(Page):
    def is_displayed(player: Player):
        return player.answer1a != 2

    timeout_seconds = 30
    form_model = 'player'
    form_fields = ['answer1b']


class Control2b(Page):
    def is_displayed(player: Player):
        return player.answer1a != 2

    timeout_seconds = 20


class Control3b(Page):
    def is_displayed(player: Player):
        return player.answer2a != 1

    timeout_seconds = 30
    form_model = 'player'
    form_fields = ['answer2b']


class Control4b(Page):
    def is_displayed(player: Player):
        return player.answer2a != 1
    timeout_seconds = 20

def wait_page_live_method(player: Player, data):  # For first page
    group = player.group
    arrived_ids_set = set(json_loads(group.arrived_ids))
    arrived_ids_set.add(player.id_in_subsession)
    group.arrived_ids = json_dumps(list(arrived_ids_set))

    arrived_count = len(arrived_ids_set)

    if not unarrived_players(group):
        return {0: dict(finished=True, arrived_count=arrived_count)}
    return {0: dict(arrived_count=arrived_count)}

class ControlWaitPage(Page):  # For first page

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

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.controlWait_time = time.time() - player.instruction_start - player.instruction_time - player.control1_time - player.control2_time - player.control3_time - player.control4_time
    pass

page_sequence = [Instructions2, Control1a, Control2a, Control3a, Control4a, ControlWaitPage]
