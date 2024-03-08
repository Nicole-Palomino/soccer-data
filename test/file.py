import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import requests
import json
from PIL import Image, ImageDraw
from urllib.request import urlopen
from bs4 import BeautifulSoup
from mplsoccer import FontManager
from fotmob import scraperFotmob
from sofascore import scraperSofaScore
from functions import functions_horizontal as fh

warnings.filterwarnings("ignore", category=FutureWarning)


ruta_archivo_europa = "../data/europa_league/EUROPALEAGUE_MARSELLA_VILLARREAL.json"
ruta_archivo_europa_sofascore = "../data/europa_league/EUROPALEAGUE_MARSELLA_VILLARREAL_SOFASCORE.json"

match_id = '4430798'
match_id_sofascore = '12095415'
url_sofascore = 'https://www.sofascore.com/villarreal-olympique-de-marseille/QHsugb#id:12095415'

scraper = scraperFotmob(match_id)
sofascore = scraperSofaScore(match_id_sofascore)

json_fotmob = scraper.get_json()
json_sofascore = sofascore.get_json()

scraper.save_json(ruta_archivo_europa, json_fotmob)
sofascore.save_json(ruta_archivo_europa_sofascore, json_sofascore)

json_data = scraper.open_json(ruta_archivo_europa)
json_data_sofascore = sofascore.open_json(ruta_archivo_europa_sofascore)

match = sofascore.get_players_match_stats(match_id_sofascore, 'Marseille', 'Villarreal')
match_home, match_away = match[0], match[1]

match_home = match_home.fillna(0)
match_away = match_away.fillna(0) 

players = sofascore.get_stats_featured_players(match_home, match_away)
player_home, player_away = players[0], players[1]

player_arquero = sofascore.get_info_featured_arquero(match_away)
print(player_arquero)