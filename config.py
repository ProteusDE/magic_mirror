import os

# --- THE FOLLOWING SIX CONSTANTS NEEDS TO BE ADDED
# --- TO ENVIRONMENTAL VARIABLES BEFORE LAUNCHING THE PROGRAM

# export SPOTIPY_CLIENT_ID='{Add ID here}' etc.
CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = os.environ.get('SPOTIPY_REDIRECT_URI')

VIM = os.environ.get('VIM')
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
TESLA_TOKEN = os.environ.get('TESLA_TOKEN')
GOOGLE_MAPS_TOKEN = os.environ.get('GOOGLE_API')

LAT = '63.43'			# Change this to your latitude
LON = '10.39'			# Change this to your longditude


# ------------- ALTER THESE CONSTANTS IF YOU'D PLEASE ------------------#

TITLE = "MagicMirror"
SCREEN_RESOLUTION = '800x480'

GUI_UPDATE_FREQUENCY = 1000		# Update GUI every 200 ms
TESLA_CHECK_FREQUENCY = 900000  # Update Tesla info every 15 min
WEATHER_FREQUENCY = 1800000		# Update GUI every half hour

# ----- WEATHER API --------#

WEATHER_URL = 'https://api.openweathermap.org/data/2.5/onecall'
WEATHER_ICON_URL = "http://openweathermap.org/img/wn/"
WEATHER_ICON = "/home/pi/github/magic_mirror/images/weather_icon.png"

# ----- TESLA API --------#

TESLA_IMG = '/home/pi/github/magic_mirror/images/tesla.jpg'
TESLA_HEADERS = {'Content-Type': 'application/json', 'Authorization': f'Bearer {TESLA_TOKEN}'}
TESLA_BASE_URL = f'https://owner-api.teslamotors.com/api/1/vehicles/{VIM}/'
TESLA_CLIMATE_URL = '/api/1/vehicles/{id}/data_request/climate_state'

# ----- SPOTIFY API --------#

SPOTIFY_BASE_URL = 'https://api.spotify.com/v1/me/'
PLAYING_ID = ''
SPOTIFY_IMG = '/home/pi/github/magic_mirror/images/spotify_logo.png'
SCOPE = "user-read-playback-state,\
         user-modify-playback-state,user-library-read"
PC_PLAYBACK_ID = '572e2c1bf0419b6f88c619c61ead7c1291976002'
MOBILE_PLAYBACK_ID = 'eb95c22f8081a328257d4accf8cbabf1e8e73290'
LIVINGROOM_PLAYBACK_ID = 'aedf617860060aeb536287250a2159a20b48c380'

# --------------- COLOR THEME ----------------#

BACKGROUND_COLOR = '#102A43'
BGCOLOR = '#102A43'
BUTTON_BG_COLOR = '#334E68'
TEXT_COLOR = '#FF991F'
BUTTON_TEXT_COLOR = '#F0F4F8'
