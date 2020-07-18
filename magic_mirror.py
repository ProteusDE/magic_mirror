#!/usr/bin/env python3

import tkinter as tk
from tkinter.ttk import *
import datetime
import json
import requests
from PIL import ImageTk, Image
import urllib.request
import io
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import *

import pprint

# ----------- FUNCTIONS ------------ #


def exit():
    quit()


def update_time():
    now = datetime.datetime.now()
    localtime = now.strftime("%a, %d %b %Y %H:%M:%S")
    timestamp.configure(text=localtime)
    if spotify_current_playback():
        spotify_status.configure(text="Playing")
        play_btn.configure(text="PAUSE")
    else:
        spotify_status.configure(text="Paused")
        play_btn.configure(text="PLAY")
    window.after(GUI_UPDATE_FREQUENCY, update_time)


def update_weather():
    weather_request = requests.get(f'{WEATHER_URL}?lat={LAT}&lon={LON}&appid={WEATHER_API_KEY}')
    current_timestamp = int(weather_request.json()['current']['dt'])
    current_temperature_kelvin = weather_request.json()['current']['temp']
    current_temperature_celcius = str(int(current_temperature_kelvin) - 273)
    current_weather_description = weather_request.json()['current']['weather'][0]['main']
    current_weather_icon = weather_request.json()['current']['weather'][0]['icon']
    current_weather_url = WEATHER_ICON_URL + f"{current_weather_icon}@2x.png"

    weather_icon_canvas.itemconfig(weather_temperature,
                                   text=current_temperature_celcius + " deg")

    dwu_raw = urllib.request.urlopen(current_weather_url).read()
    current_weather = Image.open(io.BytesIO(dwu_raw))
    cw_image = ImageTk.PhotoImage(current_weather)
    weather_icon_canvas.itemconfig(weather_icon, image=cw_image)
    weather_icon_canvas.image = cw_image

    weather_icon_canvas.itemconfig(weather_text,
                                   text=current_weather_description)

    window.after(WEATHER_FREQUENCY, update_weather)


def tesla_update():
    get_tesla_info()
    window.after(TESLA_CHECK_FREQUENCY, tesla_update)


def get_tesla_info():
    charge_url = TESLA_BASE_URL + 'data_request/charge_state/'
    ch_response = requests.get(charge_url, headers=TESLA_HEADERS)

    if ch_response.status_code == 200:
        pwr = json.loads(ch_response.content.decode('utf-8'))
        km = str(int((pwr["response"]["ideal_battery_range"]) * 1.609))
        percent = str(pwr["response"]["battery_level"])
        last_update = pwr["response"]["timestamp"]
        bat_range.configure(text="Range: " + km + " km (" + percent + "%)")
        progress['value'] = int(percent)
    else:
        print(ch_response.status_code)
        print("Failed to get a response...")
        return None

    climate_url = TESLA_BASE_URL + 'data_request/climate_state/'
    cl_response = requests.get(climate_url, headers=TESLA_HEADERS)

    if cl_response.status_code == 200:
        climate = json.loads(cl_response.content.decode('utf-8'))
        temp_in = climate['response']['inside_temp']
        temp_out = climate['response']['outside_temp']

        temp_inside.configure(text="Temperature inside: " + str(temp_in) + " C")
        temp_outside.configure(text="Temperature outside: " + str(temp_out) + " C")
    else:
        print(cl_response.status_code)
        print("Failed to get a response...")
        return None


def spotify_current_playback():
    global PLAYING_ID

    resp = sp.current_user_playing_track()
    if resp is None:
        print("None is playing")
    else:
        status = resp["is_playing"]
        if status:
            song_id = resp["item"]["id"]
            if song_id != PLAYING_ID:
                print("New song")
                PLAYING_ID = song_id
                change_album_cover(resp)
            return status
        else:
            return False


def change_album_cover(json_response):
    image_url = json_response["item"]["album"]["images"][1]["url"]
    title = json_response["item"]["name"]
    artist = json_response["item"]["album"]["artists"][0]["name"]
    album = json_response["item"]["album"]["name"]

    song = f'{title} | {artist} | {album}'

    spotify_song_title.configure(text=song)

    raw_data = urllib.request.urlopen(image_url).read()
    im = Image.open(io.BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)
    spotify_album_cover.configure(image=image)
    spotify_album_cover.image = image


def spotify_play():
    is_playing = spotify_current_playback()
    print(is_playing)

    if is_playing is False:
        sp.start_playback()
        print("Playing")
    else:
        sp.pause_playback()
        print("Paused")


def spotify_next():
    sp.next_track()


def spotify_previous():
    sp.previous_track()


def spotify_incr_vol():
    global spotify_volume
    sp.volume(spotify_volume + 10)
    spotify_volume = spotify_volume + 10


def spotify_decr_vol():
    global spotify_volume
    sp.volume(spotify_volume - 10)
    spotify_volume = spotify_volume - 10


def open_tesla_window(event):
    print("Åpnet nytt vindu (tror jeg)")
    tesla_window = tk.Toplevel(window)

    tesla_label = tk.Label(tesla_window, text="TESLA", font=("Helvetica", 45),
                           fg=TEXT_COLOR, bg=BGCOLOR)
    tesla_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N)


# ----------- PROGRAM START ------------ #


print("Starting MagicMirror...")

window = tk.Tk()
window.title(TITLE)
window.geometry(SCREEN_RESOLUTION)
window.configure(background=BACKGROUND_COLOR)
# The method overridedirect might have to be disabled during auth of Spotify
window.overrideredirect(True)  # Make program run full screen mode


window.columnconfigure(0, pad=3, weight=1)
window.columnconfigure(1, pad=3, weight=1)
window.columnconfigure(2, pad=3, weight=2)
window.columnconfigure(3, pad=3, weight=2)
window.columnconfigure(4, pad=3, weight=2)

window.rowconfigure(0, pad=3, weight=1)
window.rowconfigure(1, pad=3, weight=1)
window.rowconfigure(2, pad=3, weight=1)
window.rowconfigure(3, pad=3, weight=1)
window.rowconfigure(4, pad=3, weight=1)
window.rowconfigure(5, pad=3, weight=1)
window.rowconfigure(6, pad=3, weight=1)
window.rowconfigure(7, pad=3, weight=1)
window.rowconfigure(8, pad=3, weight=1)


# ----------- TESLA INFO ------------ #


tesla_label = tk.Label(window, text="TESLA", font=("Helvetica", 15),
                       fg=TEXT_COLOR, bg=BGCOLOR)
tesla_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N)

tesla_canv = tk.Canvas(window, width=300, height=120,
                       bg=BGCOLOR, highlightthickness=0)
tesla_canv.grid(row=3, column=0, sticky=tk.N)
tesla_canv.bind("<Button-1>", open_tesla_window)

t_btn = tk.Button(window, text="TESLA", command=open_tesla_window)
t_btn.grid(row=8, column=0, sticky=tk.E)

tesla_logo = ImageTk.PhotoImage(Image.open(TESLA_IMG))
tesla_img = tesla_canv.create_image(160, 60, image=tesla_logo)

progress = Progressbar(window, orient=tk.HORIZONTAL, length=200,
                       mode='determinate')
progress['value'] = 0
progress.grid(row=3, column=0, sticky=tk.S)

bat_range = tk.Label(window, text="Range: ", fg=TEXT_COLOR, bg=BGCOLOR)
bat_range.grid(row=4, column=0, sticky=tk.N)

temp_inside = tk.Label(window, text="Temperature inside: ",
                       fg=TEXT_COLOR, bg=BGCOLOR)
temp_inside.grid(row=4, column=0, sticky=tk.S)

temp_outside = tk.Label(window, text="Temperature outside: ",
                        fg=TEXT_COLOR, bg=BGCOLOR)
temp_outside.grid(row=5, column=0, sticky=tk.N)


# ----------- TIME ----------- #


localtime = datetime.datetime.now()
timestamp = tk.Label(window, text=localtime, font=("Helvetica", 25),
                     fg=TEXT_COLOR, bg=BGCOLOR)
timestamp.grid(row=0, column=0, sticky=tk.N, columnspan=5)


# -----------  WEATHER INFO ----------- #


weather_label = tk.Label(window, text="WEATHER", font=("Helvetica", 15),
                         fg=TEXT_COLOR, bg=BGCOLOR)
weather_label.grid(row=1, column=1, padx=5, pady=5)

weather_icon_canvas = tk.Canvas(window, width=130, height=300, bg=BGCOLOR,
                                highlightthickness=0)
weather_icon_canvas.grid(row=3, column=1, sticky=tk.N, rowspan=3)

cw_image = ImageTk.PhotoImage(Image.open(WEATHER_ICON))

weather_icon = weather_icon_canvas.create_image(50, 30, image=cw_image)
weather_text = weather_icon_canvas.create_text(50, 90, text="-",
                                               font=("Helvetica", 15),
                                               fill=TEXT_COLOR)
weather_temperature = weather_icon_canvas.create_text(50, 115, text="-",
                                                      font=("Helvetica", 15),
                                                      fill=TEXT_COLOR)
update_weather()


# ----------- SPOTIFY  ----------- #


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE,
                                               username='oveistad'))


spotify_incr_vol_btn = tk.Button(window, text="+", height=2, width=2,
                                 command=spotify_incr_vol, bg=BUTTON_BG_COLOR,
                                 fg=BUTTON_TEXT_COLOR, relief=tk.RAISED)
spotify_incr_vol_btn.grid(row=8, column=1, sticky=tk.N)

spotify_decr_vol_btn = tk.Button(window, text="-", height=2, width=2,
                                 command=spotify_decr_vol, bg=BUTTON_BG_COLOR,
                                 fg=BUTTON_TEXT_COLOR, relief=tk.RAISED)
spotify_decr_vol_btn.grid(row=8, column=1, sticky=tk.S)


spotify_label = tk.Label(window, text="SPOTIFY", font=("Helvetica", 15),
                         fg=TEXT_COLOR, bg=BGCOLOR)
spotify_label.grid(row=1, column=2, padx=5, pady=5, sticky=tk.N, columnspan=3)

spotify_status = tk.Label(window, text="Playing status:", fg=TEXT_COLOR,
                          bg=BGCOLOR)
spotify_status.grid(row=2, column=2, sticky=tk.N, columnspan=3)

image = ImageTk.PhotoImage(Image.open(SPOTIFY_IMG))
spotify_album_cover = Label(window, image=image)
spotify_album_cover.grid(row=3, column=2, columnspan=3, rowspan=4)


spotify_song_title = tk.Label(window, text="-", font=("Helvetica", 11),
                              fg=TEXT_COLOR, bg=BGCOLOR)
spotify_song_title.grid(row=7, column=2, sticky=tk.N, columnspan=3)

previous_btn = tk.Button(window, text="PREVIOUS", height=5, width=8,
                         command=spotify_previous, bg=BUTTON_BG_COLOR,
                         fg=BUTTON_TEXT_COLOR, relief=tk.RAISED)
previous_btn.grid(row=8, column=2, sticky=tk.SW, padx=5, pady=5)


is_playing = spotify_current_playback()
if is_playing is False:
    play_btn_text = "-"
else:
    play_btn_text = "PAUSE"


play_btn = tk.Button(window, text=play_btn_text, height=5, width=8,
                     command=spotify_play, bg=BUTTON_BG_COLOR,
                     fg=BUTTON_TEXT_COLOR, relief=tk.RAISED)
play_btn.grid(row=8, column=3, sticky=tk.S, padx=5, pady=5)

next_btn = tk.Button(window, text="NEXT", height=5, width=8,
                     command=spotify_next, bg=BUTTON_BG_COLOR,
                     fg=BUTTON_TEXT_COLOR, relief=tk.RAISED)
next_btn.grid(row=8, column=4, sticky=tk.SE, padx=5, pady=5)


# ----------- EXIT BUTTON  ----------- #


exit_btn = tk.Button(window, text="EXIT", height=5, width=15, command=exit,
                     bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR,
                     relief=tk.RAISED)
exit_btn.grid(row=8, column=0, padx=5, pady=5, columnspan=2, sticky=tk.SW)


get_tesla_info()
window.after(GUI_UPDATE_FREQUENCY, update_time)
window.after(TESLA_CHECK_FREQUENCY, tesla_update)
window.after(WEATHER_FREQUENCY, update_weather)
window.mainloop()
