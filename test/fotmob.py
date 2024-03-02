import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
from PIL import Image
from urllib.request import urlopen

class scraperFotmob:
    def __init__(self, match_id):
        self.match_id = match_id
        self.url = f'https://www.fotmob.com/es/match/{match_id}/'
        self.json_fotmob = self.get_json()

    def get_json(self):
        response = requests.get(self.url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        json_fotmob = json.loads(soup.find('script', attrs={'id':'__NEXT_DATA__'}).contents[0])
        return json_fotmob
    
    def save_json(self, ruta_archivo, json_fotmob):
        with open(ruta_archivo, "w", encoding='utf-8') as archivo:
            json.dump(json_fotmob, archivo)

    def open_json(self, ruta_archivo):
        with open(ruta_archivo, "r", encoding='utf-8') as archivo:
            datos_json = json.load(archivo)   
        return datos_json   

    def colors_teams(self, json_data):
        team_colors = json_data['props']['pageProps']['general']['teamColors']
        teams = ['home', 'away']
        colors = []
        fonts = []
        for x in teams:
            color = team_colors['lightMode'][x]
            font = team_colors['fontLightMode'][x]
            colors.append(color)
            fonts.append(font)
        return colors, fonts

    def info_match(self, json_data):
        league = json_data['props']['pageProps']['general']['leagueName']
        round_name = json_data['props']['pageProps']['general']['leagueRoundName']
        country = json_data['props']['pageProps']['general']['countryCode']
        name_home = json_data['props']['pageProps']['general']['homeTeam']
        name_away = json_data['props']['pageProps']['general']['awayTeam']
        
        stadium = json_data['props']['pageProps']['content']['matchFacts']['infoBox']
        referee = stadium['Referee']['text']
        name_stadium = stadium['Stadium']['name']
        city_stadium = stadium['Stadium']['city']
        
        match_day = json_data['props']['pageProps']['general']['matchTimeUTCDate']
        match_day = datetime.fromisoformat(match_day.replace('Z', '+00:00')).strftime('%Y-%m-%d')
        return league, round_name, country, name_home, name_away, match_day, referee, name_stadium, city_stadium

    def score_image(self, json_data):
        info_home = json_data['props']['pageProps']['header']['teams'][0]
        info_away = json_data['props']['pageProps']['header']['teams'][1]
        list_info = ['score', 'imageUrl']
        home_info = []
        away_info = []
        for x in list_info:
            list_home = info_home[x]
            list_away = info_away[x]
            home_info.append(list_home)
            away_info.append(list_away)
        return home_info, away_info

    def get_info_player_match(self, json_data):
        player_of_the_match = json_data['props']['pageProps']['content']['matchFacts']['playerOfTheMatch']
        id_player_match = player_of_the_match['id']
        name_player_match = player_of_the_match['name']['fullName']
        team_player_match = player_of_the_match['teamName']
        rol_player_match = player_of_the_match['role']
        player_home_away = player_of_the_match['isHomeTeam']
        rating_player_match = player_of_the_match['rating']['num']
        return id_player_match, name_player_match, team_player_match, rol_player_match, player_home_away, rating_player_match

    def get_image_player_match(self, id):
        url_image = f'https://images.fotmob.com/image_resources/playerimages/{id}.png'
        image_player_match = Image.open(urlopen(url_image))
        return image_player_match
    
    def get_top_stats_player_match(self, json_data):
        player_of_the_match = json_data['props']['pageProps']['content']['matchFacts']['playerOfTheMatch']
        stats_player_match = player_of_the_match['stats']

        list_top_stats = ['FotMob rating', 'Minutes played', 'Goals', 'Assists', 'Total shots', 'Accurate passes', 'Chances created', 'Expected goals (xG)']
        top_stats_player_match = stats_player_match[0]['stats']
        list_stats_player_match = []

        for x in list_top_stats:
            list_stats_player_match.append(top_stats_player_match[x]['value'])
        return list_stats_player_match

    def get_attack_stats_player_match(self, json_data):
        player_of_the_match = json_data['props']['pageProps']['content']['matchFacts']['playerOfTheMatch']
        stats_player_match = player_of_the_match['stats']

        list_attack_stats = ['Touches', 'Touches in opposition box', 'Passes into final third']
        attack_player_match = stats_player_match[1]['stats']
        list_attack_player_match = []

        for x in list_attack_stats:
            list_attack_player_match.append(attack_player_match[x]['value'])
        return list_attack_player_match

    def get_defense_player_match(self, json_data):
        player_of_the_match = json_data['props']['pageProps']['content']['matchFacts']['playerOfTheMatch']
        stats_player_match = player_of_the_match['stats']
        
        list_defense_stats = ['Tackles won', 'Defensive actions', 'Recoveries']
        defense_player_match = stats_player_match[2]['stats']
        list_defense_player_match = []

        for x in list_defense_stats:
            list_defense_player_match.append(defense_player_match[x]['value'])
        return list_defense_player_match

    def get_duel_player_match(self, json_data):
        player_of_the_match = json_data['props']['pageProps']['content']['matchFacts']['playerOfTheMatch']
        stats_player_match = player_of_the_match['stats']

        list_duel_stats = ['Duels won', 'Aerial duels won', 'Was fouled', 'Fouls committed']
        duels_player_match = stats_player_match[3]['stats']
        list_duel_player_match = []

        for x in list_duel_stats:
            list_duel_player_match.append(duels_player_match[x]['value'])
        return list_duel_player_match

    def get_minute_goals(self, json_data):
        events = json_data['props']['pageProps']['content']['matchFacts']['events']['events']
        goals = [d for d in events if d['type'] == 'Goal']
        goal_times = [d['timeStr'] for d in goals]

        goal_minutes = []

        for valor in goal_times:
            if isinstance(valor, str):
                resultado = eval(valor)
                goal_minutes.append(resultado)
            else:
                goal_minutes.append(valor)
        return goal_minutes

    def get_match_momentum(self, json_data, goal_minutes):
        match_momentum = json_data['props']['pageProps']['content']['matchFacts']['momentum']['main']['data']
        match_momentum = pd.DataFrame(match_momentum)

        match_momentum_local = match_momentum[match_momentum['value'] > 0]
        match_momentum_visit = match_momentum[match_momentum['value'] < 0]

        df_goles_match = match_momentum[match_momentum['minute'].isin(goal_minutes)]['minute'].to_list()
        return match_momentum_local, match_momentum_visit, df_goles_match

    def get_stadistics_match(self, json_data):
        all_stats = json_data['props']['pageProps']['content']['stats']['Periods']['All']['stats']

        ball_possession, xg_match, shot_match, target_match, big_chances_match, big_chances_missed_match, passes_match, fouls_match, corner_match = all_stats[0]['stats'][:9]
        shots_blocked, shots_poste, shots_inside, shots_outside = all_stats[1]['stats'][4:8]
        long_ball, touches_in_box, offsides = all_stats[3]['stats'][5], all_stats[3]['stats'][8], all_stats[3]['stats'][9]
        tackles, bloqueos, saves = all_stats[4]['stats'][1], all_stats[4]['stats'][3], all_stats[4]['stats'][5]
        duelos, aereos, dribbles = all_stats[5]['stats'][2], all_stats[5]['stats'][3], all_stats[5]['stats'][4]
        yellow_card, red_card = all_stats[6]['stats'][1], all_stats[6]['stats'][2]
        return ball_possession, xg_match, shot_match, target_match, big_chances_match, big_chances_missed_match, passes_match, fouls_match, corner_match, shots_blocked, shots_poste, shots_inside, shots_outside, long_ball, touches_in_box, offsides, tackles, bloqueos, saves, duelos, aereos, dribbles, yellow_card, red_card

    def get_players_home(self, json_data):
        ids, posicion, name, camiseta, imagen, rating, isHome, stats, minutes = [], [], [], [], [], [], [], [], []
        data_local = json_data['props']['pageProps']['content']['lineup']['lineup'][0]['players']

        for equipo in data_local:
            for jugador in equipo:
                ids.append(jugador['id'])
                posicion.append(jugador['positionStringShort'])
                name.append(jugador['name']['fullName'])
                camiseta.append(jugador['shirt'])
                imagen.append(jugador['imageUrl'])
                rating.append(jugador['rating']['num'])
                isHome.append(jugador['isHomeTeam'])
                stats.append(jugador['stats'])
                minutes.append(jugador['minutesPlayed'] if jugador['minutesPlayed'] else 0)
                
            df_jug_destacado_local = pd.DataFrame({
                'id': ids, 
                'posicion': posicion,
                'nombre': name,
                'camiseta': camiseta,
                'imagen': imagen,
                'rating': rating,
                'isHome': isHome,
                'stats': stats,
                'minutes': minutes
            })
        return df_jug_destacado_local

    def get_players_visit(self, json_data):
        posicion_visit, name_visit, camiseta_visit, imagen_visit, rating_visit, isHome_visit, stats_visit, minutes_visit = [], [], [], [], [], [], [], []
        data_visit = json_data['props']['pageProps']['content']['lineup']['lineup'][1]['players']

        for equipo in data_visit:
            for jugador in equipo:
                posicion_visit.append(jugador['positionStringShort'])
                name_visit.append(jugador['name']['fullName'])
                camiseta_visit.append(jugador['shirt'])
                imagen_visit.append(jugador['imageUrl'])
                rating_visit.append(jugador['rating']['num'])
                isHome_visit.append(jugador['isHomeTeam'])
                stats_visit.append(jugador['stats'])
                minutes_visit.append(jugador['minutesPlayed'])
                
        df_jug_destacado_visit = pd.DataFrame({
            'posicion': posicion_visit,
            'nombre': name_visit,
            'camiseta': camiseta_visit,
            'imagen': imagen_visit,
            'rating': rating_visit,
            'isHome': isHome_visit,
            'stats': stats_visit,
            'minutes': minutes_visit
        })
        return df_jug_destacado_visit

    def get_data_players_destacados(self, players_home, players_away):
        # jugadores destacados
        player_destacado_home = players_home[['nombre', 'imagen', 'rating', 'camiseta']].sort_values(by='rating', ascending=False).iloc[0]
        player_destacado_away = players_away[['nombre', 'imagen', 'rating', 'camiseta']].sort_values(by='rating', ascending=False).iloc[0]

        # fotos de los jugadores destacados
        image_player_home = Image.open(urlopen(player_destacado_home[1]))
        image_player_away = Image.open(urlopen(player_destacado_away[1]))

        # dataframe de los jugadores destacados
        df_player_home = players_home[players_home['nombre'] == player_destacado_home[0]]
        df_player_away = players_away[players_away['nombre'] == player_destacado_away[0]]

        return image_player_home, image_player_away, df_player_home, df_player_away, player_destacado_home, player_destacado_away

    def get_data_player_home(self, df_player_home):
        list_estadistica1 = ['Minutes played', 'Goals', 'Assists', 'Total shots', 'Accurate passes', 'Chances created', 'Expected assists (xA)', 'FotMob rating']
        list_estadistica2 = ['Ground duels won', 'Fouls committed', 'Aerial duels won']
        list_estadistica3 = ['Touches', 'Successful dribbles', 'Accurate long balls', 'Passes into final third']

        extracted_home = {}
        player_destado_home = df_player_home['stats'].reset_index(drop=True)

        listas_estadisticas = [list_estadistica1, list_estadistica2, list_estadistica3]
        player_stats_home = [player_destado_home[0][0]['stats'], player_destado_home[0][3]['stats'], player_destado_home[0][1]['stats']]

        recuperaciones_player_home = player_destado_home[0][2]['stats'].get('Recoveries', {}).get('value', 0)

        for stats, jugador in zip(listas_estadisticas, player_stats_home):
            for stat in stats:
                extracted_home[stat] = jugador.get(stat, {}).get('value', 0)
        return extracted_home, recuperaciones_player_home    

    def get_data_player_away(self, df_player_away):
        list_estadistica1 = ['Minutes played', 'Goals', 'Assists', 'Total shots', 'Accurate passes', 'Chances created', 'Expected assists (xA)', 'FotMob rating']
        list_estadistica2 = ['Ground duels won', 'Fouls committed', 'Aerial duels won']
        list_estadistica3 = ['Touches', 'Successful dribbles', 'Accurate long balls', 'Passes into final third']

        extracted_away = {}
        player_destado_away = df_player_away['stats'].reset_index(drop=True)

        listas_estadisticas = [list_estadistica1, list_estadistica2, list_estadistica3]
        player_stats_away = [player_destado_away[0][0]['stats'], player_destado_away[0][3]['stats'], player_destado_away[0][1]['stats']]

        recuperaciones_player_away = player_destado_away[0][2]['stats'].get('Recoveries', {}).get('value', 0)

        for stats, jugador in zip(listas_estadisticas, player_stats_away):
            for stat in stats:
                extracted_away[stat] = jugador.get(stat, {}).get('value', 0)
        return extracted_away, recuperaciones_player_away

    def get_data_player_arquero(self, df_player_arquero):
        list_arquero=['Saves', 'Goals conceded', 'Accurate long balls', 'Punches', 'Recoveries', 'Touches', 'Minutes played', 'Goals', 'Assists', 'Total shots', 'Accurate passes', 'Chances created', 'Expected assists (xA)', 'FotMob rating']

        extracted_arquero = {}
        player_destado_arquero = df_player_arquero['stats'].reset_index(drop=True)

        listas_estadisticas = [list_arquero]
        player_stats_arquero = [player_destado_arquero[0][0]['stats']]

        for stats, jugador in zip(listas_estadisticas, player_stats_arquero):
            for stat in stats:
                extracted_arquero[stat] = jugador.get(stat, {}).get('value', 0)
        return extracted_arquero
    
