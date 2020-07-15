# --- THESE SIX CONSTANTS NEEDS TO BE SET BEFORE LAUNCHING THE PROGRAM ----#

TESLA_TOKEN = ''		# Insert Tesla Token here
TESLA_BASE_URL = ''		# 'https://owner-api.teslamotors.com/api/1/vehicles/{VIM}/'
SPOTIFY_TOKEN = ''		# Insert Spotify Token here
WEATHER_API_KEY = ''    # Insert Weather API Key here


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
TESLA_IMG = '/home/pi/progging/MagicMirror/images/tesla.jpg'
TESLA_HEADERS = {'Content-Type': 'application/ \
                json', 'Authorization': 'Bearer {0}'.format(TESLA_TOKEN)}


# ----- SPOTIFY API --------#
SPOTIFY_BASE_URL = 'https://api.spotify.com/v1/me/'
PLAYING_ID = ''


# --------------- COLOR THEME ----------------#

BACKGROUND_COLOR = '#102A43'
BGCOLOR = '#102A43'
BUTTON_BG_COLOR = '#334E68'
TEXT_COLOR = '#FF991F'
BUTTON_TEXT_COLOR = '#F0F4F8'
