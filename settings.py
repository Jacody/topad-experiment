import os
from dotenv import load_dotenv

# Lade die Umgebungsvariablen aus der .env-Datei
load_dotenv()


import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "_static"),
]

SESSION_CONFIGS = [
    dict(
        name='topad',
        display_name="TOPAD-Game",
        num_demo_participants=12,
        app_sequence=['stall_page','control','topad']
    ),
]


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
DEBUG = 0                   #Debug mode on

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'coby'
AUTH_LEVEL = 'STUDY'

# Alle sensiblen Daten aus Umgebungsvariablen laden
ADMIN_PASSWORD = os.getenv('OTREE_ADMIN_PASSWORD', '')
if not ADMIN_PASSWORD:
    # Warnung: Keine Passwort-Umgebungsvariable gefunden
    # In der Produktion sollte diese Variable gesetzt werden
    # Für Entwicklungszwecke kann ein Standardwert verwendet werden
    # ADMIN_PASSWORD = 'default-password'  # Nur für Entwicklung
    pass

# Setze die Werte aus den Umgebungsvariablen
SECRET_KEY = os.getenv("SECRET_KEY", "")
if not SECRET_KEY:
    # Warnung: Kein Secret Key in Umgebungsvariablen gefunden
    # In der Produktion sollte diese Variable gesetzt werden
    # SECRET_KEY = "default-secret-key"  # Nur für Entwicklung
    pass

INSTALLED_APPS = ['otree']

DATABASES = {
    'default': None
}
