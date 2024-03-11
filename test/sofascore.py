import json
import requests
import pandas as pd
from PIL import Image
from urllib.request import urlopen
from bs4 import BeautifulSoup

class scraperSofaScore:
    def __init__(self, match_id_sofascore):
        self.match_id = match_id_sofascore
        self.url_lineups = f'https://api.sofascore.com/api/v1/event/{self.match_id}/lineups'
        self.headers = {
            'authority': 'api.sofascore.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dnt': '1',
            'if-none-match': 'W/"4bebed6144"',
            'origin': 'https://www.sofascore.com',
            'referer': 'https://www.sofascore.com/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        }

    def get_json(self):
        response = requests.get(self.url_lineups, headers=self.headers)
        json_sofascore = response.json()
        return json_sofascore
    
    def save_json(self, ruta_archivo, json_fotmob):
        with open(ruta_archivo, "w", encoding='utf-8') as archivo:
            json.dump(json_fotmob, archivo)

    def open_json(self, ruta_archivo):
        with open(ruta_archivo, "r", encoding='utf-8') as archivo:
            datos_json = json.load(archivo)   
        return datos_json 
    
    def get_headers(self, url):
        r = requests.get(url, headers=self.headers)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        json_fotmob = json.loads(soup.find('script', attrs={'id':'__NEXT_DATA__'}).contents[0])
        return json_fotmob
    
    def get_colors_teams(self, json_fotmob):
        team_colors = json_fotmob['props']['pageProps']['initialProps']['event']
        teams = ['homeTeam', 'awayTeam']
        colors = []
        fonts = []
        for x in teams:
            color = team_colors[x]['teamColors']['primary']
            font = team_colors[x]['teamColors']['text']
            colors.append(color)
            fonts.append(font)
        return colors, fonts

    def get_players_match_stats(self, match_id, home_name, away_name):
        response = requests.get(
            f'https://api.sofascore.com/api/v1/event/{match_id}/lineups', 
            headers=self.headers
        )
        
        names = {'home': home_name, 'away': away_name}
        dataframes = {}
        for team in names.keys():
            data = pd.DataFrame(response.json()[team]['players'])
            columns_list = [
                data['player'].apply(pd.Series), data['shirtNumber'], 
                data['jerseyNumber'], data['substitute'], 
                data['statistics'].apply(pd.Series, dtype=object), 
                data['captain']
            ]
            df = pd.concat(columns_list, axis=1)
            df['team'] = names[team]
            dataframes[team] = df
        
        return dataframes['home'], dataframes['away']
    
    def get_stats_featured_players(self, match_home, match_away):
        player_destacado_home = match_home[['name', 'id', 'rating', 'shirtNumber']].sort_values(by='rating', ascending=False).iloc[0]
        player_destacado_away = match_away[['name', 'id', 'rating', 'shirtNumber']].sort_values(by='rating', ascending=False).iloc[0]
        
        return player_destacado_home, player_destacado_away
    
    def get_image_players(self, player_home_id, player_away_id):
        url_image_home = f'https://api.sofascore.app/api/v1/player/{player_home_id}/image'
        url_image_away = f'https://api.sofascore.app/api/v1/player/{player_away_id}/image'

        image_player_home = Image.open(urlopen(url_image_home))
        image_player_away = Image.open(urlopen(url_image_away))

        return image_player_home, image_player_away

    def get_info_featured_player_away(self, match_away):
        player_featured_away = match_away[['name', 'minutesPlayed', 'goals', 'expectedAssists', 'accuratePass', 'keyPass', 'accurateLongBalls', 'possessionLostCtrl', 'touches', 'aerialWon', 'rating', 'totalTackle', 'duelWon', 'fouls', 'team']]
        
        player_destacado_away = player_featured_away.sort_values(by='rating', ascending=False).iloc[0]

        return player_destacado_away
    
    def get_info_featured_player_home(self, match_home):
        player_featured_home = match_home[['name', 'minutesPlayed', 'goals', 'expectedAssists', 'accuratePass', 'keyPass', 'accurateLongBalls', 'possessionLostCtrl', 'touches', 'aerialWon', 'rating', 'totalTackle', 'duelWon', 'fouls', 'team']]
        player_destacado_home = player_featured_home.sort_values(by='rating', ascending=False).iloc[0]

        return player_destacado_home
    
    def get_info_featured_arquero(self, match_home):
        player_featured_port = match_home[['name', 'minutesPlayed', 'saves', 'expectedAssists', 'accuratePass', 
                           'keyPass', 'accurateLongBalls', 'possessionLostCtrl', 'touches', 
                           'duelLost', 'rating', 'totalTackle', 'duelWon', 'fouls', 'team']]

        player_destacado_port = player_featured_port.sort_values(by='rating', ascending=False).iloc[0]

        return player_destacado_port
    
    def get_player_id(self, jersey, data):
        for player in data:
            if player['player']['jerseyNumber'] == jersey.astype(str):
                return player['player']['id']
        return None
    
    def get_ids_heatmap(self, json_data_sofascore, player_destacado_home, player_destacado_away):
        data_home = json_data_sofascore['home']['players']
        data_away = json_data_sofascore['away']['players']

        player_jersey_local = player_destacado_home[3]
        player_jersey_visit = player_destacado_away[3]

        player_id_local = self.get_player_id(player_jersey_local, data_home)
        player_id_visit = self.get_player_id(player_jersey_visit, data_away)
        return player_id_local, player_id_visit
    
    def get_heatmap(self, match_id_sofascore, player_id):
        url = f'https://api.sofascore.com/api/v1/event/{match_id_sofascore}/player/{player_id}/heatmap'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            heatmap_data = response.json().get('heatmap', [])
            return pd.DataFrame(heatmap_data)
        else:
            return None
        
    def get_heatmap_players(self, match_id_sofascore, player_id_home, player_id_away):
        heatmap_hpme = self.get_heatmap(match_id_sofascore, player_id_home)
        heatmap_away = self.get_heatmap(match_id_sofascore, player_id_away)
        # heatmap_match = self.get_heatmap(match_id_sofascore, player_id_match)
        return heatmap_hpme, heatmap_away
    
    def get_mapa_tiros(self, match_id):
        url = f'https://api.sofascore.com/api/v1/event/{match_id}/shotmap'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            tiros = response.json()['shotmap']
            tiros_partido = pd.DataFrame(tiros)
            return tiros_partido
        else:
            return None
        
    def get_xg_match(self, tiros_partido):
        df_xG = tiros_partido[['isHome', 'shotType', 'xg', 'time', 'addedTime']]
        df_xG['xg'] = df_xG.xg.fillna(0)

        local_xG = df_xG[df_xG['isHome'] == True].sort_values(by='time').reset_index(drop=True)
        visit_xG = df_xG[~df_xG['isHome'] == True].sort_values(by='time').reset_index(drop=True)

        local_xG['xG_cumsum'] = local_xG.xg.cumsum()
        visit_xG['xG_cumsum'] = visit_xG.xg.cumsum()

        goles_local = local_xG[local_xG['shotType'] == 'goal']
        goles_visit = visit_xG[visit_xG['shotType'] == 'goal']    

        return goles_local, goles_visit, local_xG, visit_xG
    
    def get_coord_tiros(self, df_tiros, id_home, id_away):
        goal_tiros = df_tiros[df_tiros['eventType'] == 'Goal']
        nogoal_tiros = df_tiros[df_tiros['eventType'] != 'Goal']

        goal_home = goal_tiros[goal_tiros['teamId'] == id_home]
        goal_away = goal_tiros[goal_tiros['teamId'] == id_away]

        nogoal_home = nogoal_tiros[nogoal_tiros['teamId'] == id_home]
        nogoal_away = nogoal_tiros[nogoal_tiros['teamId'] == id_away]

        # Coordenadas de los goles del equipo local
        coord_x_goal_local = goal_home['x'].tolist()
        coord_y_goal_local = goal_home['y'].tolist()

        # Coordenadas de los goles del equipo visitante
        coord_x_goal_visit = goal_away['x'].tolist()
        coord_y_goal_visit = goal_away['y'].tolist()

        # Coordenadas de los no goles del equipo local
        coord_x_nogoal_local = nogoal_home['x'].tolist()
        coord_y_nogoal_local = nogoal_home['y'].tolist()

        # Coordenadas de los no goles del equipo visitante
        coord_x_nogoal_visit = nogoal_away['x'].tolist()
        coord_y_nogoal_visit = nogoal_away['y'].tolist()

        return coord_x_goal_local, coord_y_goal_local, coord_x_goal_visit, coord_y_goal_visit, coord_x_nogoal_local, coord_y_nogoal_local, coord_x_nogoal_visit, coord_y_nogoal_visit