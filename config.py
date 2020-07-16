import os

# --- THE FOLLOWING SIX CONSTANTS NEEDS TO BE ADDED
# --- TO ENVIRONMENTAL VARIABLES BEFORE LAUNCHING THE PROGRAM

# export SPOTIPY_CLIENT_ID='{Add ID here}' etc.
CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = os.environ.get('SPOTIPY_REDIRECT_URI')

VIM = os.environ.get('TESLA_VIM')
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
TESLA_TOKEN = os.environ.get('TESLA_TOKEN')

LAT = '59.917'			# Change this to your latitude
LON = '10.728'			# Change this to your longditude


# ------------- ALTER THESE CONSTANTS IF YOU'D PLEASE ------------------#

TITLE = "MagicMirror"
SCREEN_RESOLUTION = '800x480'

GUI_UPDATE_FREQUENCY = 1000		# Update GUI every 200 ms
TESLA_CHECK_FREQUENCY = 900000  # Update Tesla info every 15 min
WEATHER_FREQUENCY = 1800000		# Update GUI every half hour

# ----- WEATHER API --------#

WEATHER_URL = 'https://api.openweathermap.org/data/2.5/onecall'
WEATHER_ICON_URL = "http://openweathermap.org/img/wn/"


# ----- TESLA API --------#

TESLA_IMG = '/home/pi/github/magic_mirror/images/tesla.jpg'
TESLA_HEADERS = {f'Content-Type': 'application/ \
                 json', 'Authorization': 'Bearer {TESLA_TOKEN}'}
TESLA_BASE_URL = f'https://owner-api.teslamotors.com/api/1/vehicles/{VIM}/'


# ----- SPOTIFY API --------#

SPOTIFY_BASE_URL = 'https://api.spotify.com/v1/me/'
PLAYING_ID = ''


# --------------- COLOR THEME ----------------#

BACKGROUND_COLOR = '#102A43'
BGCOLOR = '#102A43'
BUTTON_BG_COLOR = '#334E68'
TEXT_COLOR = '#FF991F'
BUTTON_TEXT_COLOR = '#F0F4F8'
