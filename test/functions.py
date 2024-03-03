from mplsoccer import VerticalPitch, Pitch
from PIL import Image
from urllib.request import urlopen
import warnings
from scipy.ndimage import gaussian_filter

warnings.filterwarnings("ignore", category=FutureWarning)

# funciones para el 15:9
class functions_horizontal:
    def sacar_spines(ax):
        ax.spines[['top', 'right', 'bottom', 'left']].set_visible(False)
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)

    def color_ax(ax):
        ax.set_facecolor('beige')

    def get_image_escudo(ax, image):
        image_escudo = Image.open(urlopen(image))
        ax.imshow(image_escudo)

    def get_image_jug(ax, image):
        ax.imshow(image)  

    def get_information_horizontal(ax, equipos, cuerpo, color_home, color_away, home_name, away_name, score_home, score_away, stadium_city, leagueName, leagueRoundName, day, stadium_name, referee):
        ax.text(.2, .8, f'{home_name}', ha='center', va='center', fontproperties=equipos.prop, size=19, color='white', bbox=dict(facecolor=f'{color_home}', boxstyle='round'))
        ax.text(.5, .8, f'{score_home} - {score_away}', ha='center', va='center', fontproperties=equipos.prop, size=23)
        ax.text(.8, .8, f'{away_name}', ha='center', va='center', fontproperties=equipos.prop, size=19, color='white', bbox=dict(facecolor=f'{color_away}', boxstyle='round'))
        ax.text(.5, .5, f'{stadium_city} {day}', ha='center', va='center', fontproperties=cuerpo.prop, size=15)
        ax.text(.5, .3, f'{leagueName} {leagueRoundName}', ha='center', va='center', fontproperties=cuerpo.prop, size=15)
        ax.text(.5, .1, f'{stadium_name}   Árbitro: {referee}', ha='center', va='center', fontproperties=cuerpo.prop, size=15)
    
    def get_jugador_destacado_local(ax, jugador_destacado_local, extracted_local, recuperaciones_local, nombre, cuerpo):
        ax.text(.22, .9, f'{jugador_destacado_local[0]}', ha='left', va='center', fontproperties=nombre.prop, size=23)
        ax.text(.05, .8, f"Minutos jugados: {extracted_local['Minutes played']}'", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .74, f"Goles: {extracted_local['Goals']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .68, f"Asistencias: {extracted_local['Assists']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .62, f"Tiros: {extracted_local['Total shots']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .56, f"Pases: {extracted_local['Accurate passes']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .5, f"Chances creadas: {extracted_local['Chances created']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .44, f"Asistencias esperadas: {extracted_local['Expected assists (xA)']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .38, f"Recuperaciones: {recuperaciones_local}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .32, f"Toques: {extracted_local['Touches']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .26, f"Regates: {extracted_local['Successful dribbles']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .20, f"Rating: {extracted_local['FotMob rating']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .14, f"Balones largos: {extracted_local['Accurate long balls']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .08, f"Duelos ganados: {extracted_local['Ground duels won']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .02, f"Faltas cometidas: {extracted_local['Fouls committed']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)

    def get_jugador_destacado_visit(ax, jugador_destacado_visit, extracted_visit, recuperaciones_visit, nombre, cuerpo):
        ax.text(.22, .9, f'{jugador_destacado_visit[0]}', ha='left', va='center', fontproperties=nombre.prop, size=23)
        ax.text(.05, .8, f"Minutos jugados: {extracted_visit['Minutes played']}'", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .74, f"Goles: {extracted_visit['Goals']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .68, f"Asistencias: {extracted_visit['Assists']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .62, f"Tiros: {extracted_visit['Total shots']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .56, f"Pases: {extracted_visit['Accurate passes']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .5, f"Chances creadas: {extracted_visit['Chances created']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .44, f"Asistencias esperadas: {extracted_visit['Expected assists (xA)']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .38, f"Recuperaciones: {recuperaciones_visit}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .32, f"Toques: {extracted_visit['Touches']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .26, f"Regates: {extracted_visit['Successful dribbles']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .20, f"Rating: {extracted_visit['FotMob rating']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .14, f"Balones largos: {extracted_visit['Accurate long balls']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .08, f"Duelos ganados: {extracted_visit['Ground duels won']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .02, f"Faltas cometidas: {extracted_visit['Fouls committed']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)

    def get_jugador_destacado_arquero(ax, jugador_destacado_local, extracted_local, nombre, cuerpo):
        ax.text(.21, .92, f'{jugador_destacado_local[0]}', ha='left', va='center', fontproperties=nombre.prop, size=23)
        ax.text(.05, .8, f"Minutos jugados: {extracted_local['Minutes played']}'", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .74, f"Goles: {extracted_local['Goals']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .68, f"Asistencias: {extracted_local['Assists']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .62, f"Tiros: {extracted_local['Total shots']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .56, f"Pases: {extracted_local['Accurate passes']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .5, f"Chances creadas: {extracted_local['Chances created']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .44, f"Asistencias esperadas: {extracted_local['Expected assists (xA)']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .38, f"Recuperaciones: {extracted_local['Recoveries']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .32, f"Toques: {extracted_local['Touches']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .26, f"Atajadas: {extracted_local['Saves']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .20, f"Rating: {extracted_local['FotMob rating']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .14, f"Balones largos: {extracted_local['Accurate long balls']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .08, f"Goles concedidos: {extracted_local['Goals conceded']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)
        ax.text(.05, .02, f"Despejes de balón: {extracted_local['Punches']}", ha='left', va='center', fontproperties=cuerpo.prop, size=16)

    def get_estadisticas_match(ax, cuerpo, widths_possession, posesion, colores, xgs_match, shots_match, corners_match, offsides_match, yellow_cards, red_cards, homeColor, awayColor, total_value):
        ax.text(50., .5, f'Posesión', ha='center', va='center', fontproperties=cuerpo.prop, size=17, color="white")
        ax.barh(0.5, widths_possession[0], height=0.2, left=0, color=colores[0])
        ax.barh(0.5, widths_possession[1], height=0.2, left=widths_possession[0], color=colores[1])
        ax.text(12., .5, f'{posesion[0]}%', ha="left", va="center", fontproperties=cuerpo.prop, fontsize=18, color="white", zorder=2)
        ax.text(92., .5, f'{posesion[1]}%', ha="right", va="center", fontproperties=cuerpo.prop, fontsize=18, color="white", zorder=2)

        if xgs_match[0] > xgs_match[1]:
            ax.text(12., .3, f'{xgs_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=17, color='white', bbox=dict(facecolor=f'{homeColor}', boxstyle='round'))
            ax.text(50., .3, f'Goles experados (xG)', ha='center', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(92., .3, f'{xgs_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=17)
        elif xgs_match[0] == xgs_match[1]:
            ax.text(12., .3, f'{xgs_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(50., .3, f'Goles experados (xG)', ha='center', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(90., .3, f'{xgs_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=17)
        else:
            ax.text(12., .3, f'{xgs_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(50., .3, f'Goles experados (xG)', ha='center', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(92., .3, f'{xgs_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=17, color='white', bbox=dict(facecolor=f'{awayColor}', boxstyle='round'))

        if shots_match[0] > shots_match[1]:
            ax.text(12., .12, f'{shots_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=17, color='white', bbox=dict(facecolor=f'{homeColor}', boxstyle='round'))
            ax.text(50., .12, f'Tiros totales', ha='center', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(92., .12, f'{shots_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=17)
        elif shots_match[0] == shots_match[1]:
            ax.text(12., .12, f'{shots_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(50., .12, f'Tiros totales', ha='center', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(92., .12, f'{shots_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=17)
        else:
            ax.text(12., .12, f'{shots_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(50., .12, f'Tiros totales', ha='center', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(92., .12, f'{shots_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=17, color='white', bbox=dict(facecolor=f'{awayColor}', boxstyle='round'))

        if corners_match[0] > corners_match[1]:
            ax.text(12., -.06, f'{corners_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=17, color='white', bbox=dict(facecolor=f'{homeColor}', boxstyle='round'))
            ax.text(50., -.06, f'Corners', ha='center', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(92., -.06, f'{corners_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=17)
        elif corners_match[0] == corners_match[1]:
            ax.text(12., -.06, f'{corners_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(50., -.06, f'Corners', ha='center', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(92., -.06, f'{corners_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=17)
        else:
            ax.text(12., -.06, f'{corners_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(50., -.06, f'Corners', ha='center', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(92., -.06, f'{corners_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=17, color='white', bbox=dict(facecolor=f'{awayColor}', boxstyle='round'))

        if offsides_match[0] > offsides_match[1]:
            ax.text(12., -.24, f'{offsides_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=17, color='white', bbox=dict(facecolor=f'{homeColor}', boxstyle='round'))
            ax.text(50., -.24, f'Offside', ha='center', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(92., -.24, f'{offsides_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=17)
        elif offsides_match[0] == offsides_match[1]:
            ax.text(12., -.24, f'{offsides_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(50., -.24, f'Offside', ha='center', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(92., -.24, f'{offsides_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=17)
        else:
            ax.text(12., -.24, f'{offsides_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(50., -.24, f'Offside', ha='center', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(92., -.24, f'{offsides_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=17, color='white', bbox=dict(facecolor=f'{awayColor}', boxstyle='round'))

        if yellow_cards[0] > yellow_cards[1]:
            ax.text(12., -.42, f'{yellow_cards[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=17, color='white', bbox=dict(facecolor=f'{homeColor}', boxstyle='round'))
            ax.text(50., -.42, f'Tarjetas amarillas', ha='center', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(92., -.42, f'{yellow_cards[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=17)
        elif yellow_cards[0] == yellow_cards[1]:
            ax.text(12., -.42, f'{yellow_cards[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(50., -.42, f'Tarjetas amarillas', ha='center', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(92., -.42, f'{yellow_cards[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=17)
        else:
            ax.text(12., -.42, f'{yellow_cards[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(50., -.42, f'Tarjetas amarillas', ha='center', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(92., -.42, f'{yellow_cards[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=17, color='white', bbox=dict(facecolor=f'{awayColor}', boxstyle='round'))

        if red_cards[0] > red_cards[1]:
            ax.text(12., -.6, f'{red_cards[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=17, color='white', bbox=dict(facecolor=f'{homeColor}', boxstyle='round'))
            ax.text(50., -.6, f'Tarjetas rojas', ha='center', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(92., -.6, f'{red_cards[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=17)
        elif red_cards[0] == red_cards[1]:
            ax.text(12., -.6, f'{red_cards[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(50., -.6, f'Tarjetas rojas', ha='center', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(92., -.6, f'{red_cards[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=17)
        else:
            ax.text(12., -.6, f'{red_cards[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(50., -.6, f'Tarjetas rojas', ha='center', va='center', fontproperties=cuerpo.prop, size=17)
            ax.text(92., -.6, f'{red_cards[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=17, color='white', bbox=dict(facecolor=f'{awayColor}', boxstyle='round'))
        ax.set_ylim(-0.7, 0.7)
        ax.set_xlim(0, total_value)

    def get_mapa_calor(ax, heatmap):
        pitch = Pitch(pitch_type='opta', line_color='#000', line_zorder=2, corner_arcs=True, stripe=True)
        pitch.draw(ax=ax)
        bin_statistic = pitch.bin_statistic(heatmap.x, heatmap.y, statistic='count', bins=(25, 25))
        bin_statistic['statistic'] = gaussian_filter(bin_statistic['statistic'], 1)
        pitch.heatmap(bin_statistic, ax=ax, cmap='autumn')

    def get_match_momentum_horizontal(ax, goals_momentum, match_momentum_local, match_momentum_visit, homeColor, awayColor):
        for minuto in goals_momentum:
            ax.axvline(x=minuto, color='darkslategrey', linestyle='--', linewidth=1)
        ax.bar(match_momentum_local.minute, match_momentum_local.value, color=f'{homeColor}')
        ax.bar(match_momentum_visit.minute, match_momentum_visit.value, color=f'{awayColor}')
        ax.spines[['top', 'right', 'left']].set_visible(False)
        ax.yaxis.set_visible(False)
        ax.legend(['Goles'], loc='upper left')

    def get_xg_flow_chart(ax, local_xG, visit_xG, home, away, goles_local, goles_visit, homeColor, awayColor):
        ax.grid(ls='dotted',lw=.9,color='black',axis='y',zorder=1)
        spines = ['top','bottom','left','right']
        for x in spines:
            if x in spines:
                ax.spines[x].set_visible(False)
        ax.step(x=local_xG['time'], y=local_xG['xG_cumsum'],where='post', linewidth=5,label=f'{home}', color=f'{homeColor}')
        ax.step(x=visit_xG['time'], y=visit_xG['xG_cumsum'],where='post', linewidth=5,label=f'{away}', color=f'{awayColor}')
        ax.axvline(45, ls=':', color='black', lw=1.5)
        for t in goles_local['time']:
            ax.axvline(t, color=f'{homeColor}', linestyle='-.')
        for t2 in goles_visit['time']:
            ax.axvline(t2, color=f'{awayColor}' , linestyle='--')
        ax.set_xticks([0,15,30,45,60,75,90])
        ax.legend()

    def get_mapa_tiros_home(ax, coord_x_goal_local, coord_y_goal_local, coord_x_nogoal_local, coord_y_nogoal_local, homeColor):
        pitch = VerticalPitch(pitch_type='custom',pitch_length=105, pitch_width=75,pitch_color='grass', spot_scale=0.01, line_color='white', half=True, corner_arcs=True, stripe=True)
        pitch.draw(ax=ax)

        pitch.scatter(coord_x_goal_local, coord_y_goal_local, ax=ax, marker='football', s=300)
        pitch.scatter(coord_x_nogoal_local, coord_y_nogoal_local, ax=ax, c=f'{homeColor}', s=70)
        
    def get_mapa_tiros_away(ax, coord_x_goal_visit, coord_y_goal_visit, coord_x_nogoal_visit, coord_y_nogoal_visit, awayColor):
        pitch = VerticalPitch(pitch_type='custom',pitch_length=105, pitch_width=75,pitch_color='grass', spot_scale=0.01, line_color='white', half=True, corner_arcs=True, stripe=True)
        pitch.draw(ax=ax)

        pitch.scatter(coord_x_goal_visit, coord_y_goal_visit, ax=ax, marker='football', s=300)
        pitch.scatter(coord_x_nogoal_visit, coord_y_nogoal_visit, ax=ax, c=f'{awayColor}', s=100)

    def get_campo_tiros(ax, coord_x_goal_home, coord_y_goal_home, coord_x_nogoal_home, coord_y_nogoal_home, coord_x_goal_away, coord_y_goal_away, coord_x_nogoal_away, coord_y_nogoal_away, color_home, color_away):
        pitch = Pitch(pitch_color='grass', spot_scale=0.01, corner_arcs=True, stripe=True, line_color='white', pitch_type='custom', pitch_length=105, pitch_width=70)
        pitch.draw(ax=ax)

        coord1_x_goal_local = [pitch.dim.right - x for x in coord_x_goal_home]
        coord1_x_nogoal_local = [pitch.dim.right - x for x in coord_x_nogoal_home]

        pitch.scatter(coord1_x_goal_local, coord_y_goal_home, s=300,
                        edgecolor='black', ax=ax, marker='football')
        pitch.scatter(coord1_x_nogoal_local, coord_y_nogoal_home, s=100,
                        edgecolor='black', ax=ax, color=f'{color_home}')
        pitch.scatter(coord_x_goal_away, coord_y_goal_away, s=300, edgecolor='black', ax=ax, marker='football')
        pitch.scatter(coord_x_nogoal_away, coord_y_nogoal_away, s=100,
                        edgecolor='black', ax=ax, color=f'{color_away}')  

    def get_campo_tiros_vertical(ax, coord_x_goal_home, coord_y_goal_home, coord_x_nogoal_home, coord_y_nogoal_home, coord_x_goal_away, coord_y_goal_away, coord_x_nogoal_away, coord_y_nogoal_away, color_home, color_away):
        pitch = VerticalPitch(pitch_color='grass', spot_scale=0.01, corner_arcs=True, stripe=True, line_color='white', pitch_type='custom', pitch_length=105, pitch_width=70)
        pitch.draw(ax=ax)

        coord1_x_goal_local = [pitch.dim.right - x for x in coord_x_goal_home]
        coord1_x_nogoal_local = [pitch.dim.right - x for x in coord_x_nogoal_home]

        pitch.scatter(coord1_x_goal_local, coord_y_goal_home, s=200,
                        edgecolor='black', ax=ax, marker='football')
        pitch.scatter(coord1_x_nogoal_local, coord_y_nogoal_home, s=50,
                        edgecolor='black', ax=ax, color=f'{color_home}')
        pitch.scatter(coord_x_goal_away, coord_y_goal_away, s=200, edgecolor='black', ax=ax, marker='football')
        pitch.scatter(coord_x_nogoal_away, coord_y_nogoal_away, s=50,
                        edgecolor='black', ax=ax, color=f'{color_away}')  
        
    # -------------------------------------------------------------------------------------------------
        
    def color_ax_vertical(ax):
        ax.set_facecolor('ivory')

    def get_player_match_vertical(ax, name_player_match, rating_player_match, rol_player_match,  team_player_match, min_player_match, goals_player_match, assist_player_match, chances_player_match, touches_player_match, pass_final_player_match, entradas_player_match, actions_player_match, recuperaciones_player_match, duels_player_match, aereos_player_match, cometidas_player_match, equipos, cuerpo):
        ax.text(.22, .9, f'{name_player_match}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
        ax.text(.0, .75, f'Rating: {rating_player_match}', ha='left', va='center', fontproperties=equipos.prop, size=12)
        ax.text(.0, .7, f'Posición: {rol_player_match}', ha='left', va='center', fontproperties=equipos.prop, size=12)
        ax.text(.0, .65, f'Equipo: {team_player_match}', ha='left', va='center', fontproperties=equipos.prop, size=12)
        ax.text(.0, .6, f'Minutos: {min_player_match}', ha='left', va='center', fontproperties=cuerpo.prop, size=12)
        ax.text(.0, .55, f'Goles: {goals_player_match}', ha='left', va='center', fontproperties=cuerpo.prop, size=12)
        ax.text(.0, .5, f'Asistencias: {assist_player_match}', ha='left', va='center', fontproperties=cuerpo.prop, size=12)
        ax.text(.0, .45, f'Chances creadas: {chances_player_match}', ha='left', va='center', fontproperties=cuerpo.prop, size=12)
        ax.text(.0, .4, f'Toques: {touches_player_match}', ha='left', va='center', fontproperties=cuerpo.prop, size=12)
        ax.text(.0, .35, f'Pases en el último tercio: {pass_final_player_match}', ha='left', va='center', fontproperties=cuerpo.prop, size=12)
        ax.text(.0, .3, f'Entradas existosas: {entradas_player_match}', ha='left', va='center', fontproperties=cuerpo.prop, size=12)
        ax.text(.0, .25, f'Acciones defensivas: {actions_player_match}', ha='left', va='center', fontproperties=cuerpo.prop, size=12)
        ax.text(.0, .2, f'Recuperaciones: {recuperaciones_player_match}', ha='left', va='center', fontproperties=cuerpo.prop, size=12)
        ax.text(.0, .15, f'Duelos ganados: {duels_player_match}', ha='left', va='center', fontproperties=cuerpo.prop, size=12)
        ax.text(.0, .1, f'Duelos aéreos: {aereos_player_match}', ha='left', va='center', fontproperties=cuerpo.prop, size=12)
        ax.text(.0, .05, f'Faltas cometidas: {cometidas_player_match}', ha='left', va='center', fontproperties=cuerpo.prop, size=12)

    def get_estadisticas_match_vertical(ax, widths_possession, posesion, xgs_match, shots_match, targets_match, corners_match, pass_match, offsides_match, foul_match, ball_long, won_duel, dribble_match, yellow_cards, red_cards, total_value, cuerpo, colores, homeColor, awayColor):
        ax.text(50., .6, f'Posesión', ha='center', va='center', fontproperties=cuerpo.prop, size=13, color="white")
        ax.barh(0.6, widths_possession[0], height=0.1, left=0, color=colores[0])
        ax.barh(0.6, widths_possession[1], height=0.1, left=widths_possession[0], color=colores[1])
        ax.text(10., .6, f'{posesion[0]}%', ha="left", va="center", fontproperties=cuerpo.prop, fontsize=16, color="white", zorder=2)
        ax.text(90., .6, f'{posesion[1]}%', ha="right", va="center", fontproperties=cuerpo.prop, fontsize=16, color="white", zorder=2)

        # xg
        if xgs_match[0] > xgs_match[1]:
            ax.text(10., .5, f'{xgs_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{homeColor}', boxstyle='round'))
            ax.text(50., .5, f'Goles experados (xG)', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., .5, f'{xgs_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        elif xgs_match[0] == xgs_match[1]:
            ax.text(10., .5, f'{xgs_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., .5, f'Goles experados (xG)', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., .5, f'{xgs_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        else:
            ax.text(10., .5, f'{xgs_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., .5, f'Goles experados (xG)', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., .5, f'{xgs_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{awayColor}', boxstyle='round'))

        # shots
        if int(shots_match[0]) > int(shots_match[1]):
            ax.text(10., .4, f'{shots_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{homeColor}', boxstyle='round'))
            ax.text(50., .4, f'Tiros totales', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., .4, f'{shots_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        elif int(shots_match[0]) == int(shots_match[1]):
            ax.text(10., .4, f'{shots_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., .4, f'Tiros totales', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., .4, f'{shots_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        else:
            ax.text(10., .4, f'{shots_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., .4, f'Tiros totales', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., .4, f'{shots_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{awayColor}', boxstyle='round'))
        
        # shots target
        if int(targets_match[0]) > int(targets_match[1]):
            ax.text(10., .3, f'{targets_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{homeColor}', boxstyle='round'))
            ax.text(50., .3, f'Tiros al arco', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., .3, f'{targets_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        elif int(targets_match[0]) == int(targets_match[1]):
            ax.text(10., .3, f'{targets_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., .3, f'Tiros al arco', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., .3, f'{targets_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        else:
            ax.text(10., .3, f'{targets_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., .3, f'Tiros al arco', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., .3, f'{targets_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{awayColor}', boxstyle='round'))

        # corners
        if int(corners_match[0]) > int(corners_match[1]):
            ax.text(10., .2, f'{corners_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{homeColor}', boxstyle='round'))
            ax.text(50., .2, f'Corners', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., .2, f'{corners_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        elif int(corners_match[0]) == int(corners_match[1]):
            ax.text(10., .2, f'{corners_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., .2, f'Corners', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., .2, f'{corners_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        else:
            ax.text(10., .2, f'{corners_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., .2, f'Corners', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., .2, f'{corners_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{awayColor}', boxstyle='round'))
        
        # pases
        if int(pass_match[0].split(" ")[0]) > int(pass_match[1].split(" ")[0]):
            ax.text(10., .1, f'{pass_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{homeColor}', boxstyle='round'))
            ax.text(50., .1, f'Pases precisos', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., .1, f'{pass_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        elif int(pass_match[0].split(" ")[0]) == int(pass_match[1].split(" ")[0]):
            ax.text(10., .1, f'{pass_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., .1, f'Pases precisos', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., .1, f'{pass_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        else:
            ax.text(10., .1, f'{pass_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., .1, f'Pases precisos', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., .1, f'{pass_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{awayColor}', boxstyle='round'))

        # fuera de juego
        if int(offsides_match[0]) > int(offsides_match[1]):
            ax.text(10., .0, f'{offsides_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{homeColor}', boxstyle='round'))
            ax.text(50., .0, f'Offside', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., .0, f'{offsides_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        elif int(offsides_match[0]) == int(offsides_match[1]):
            ax.text(10., .0, f'{offsides_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., .0, f'Offside', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., .0, f'{offsides_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        else:
            ax.text(10., .0, f'{offsides_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., .0, f'Offside', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., .0, f'{offsides_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{awayColor}', boxstyle='round'))

        # faltas
        if int(foul_match[0]) > int(foul_match[1]):
            ax.text(10., -.1, f'{foul_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{homeColor}', boxstyle='round'))
            ax.text(50., -.1, f'Faltas', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., -.1, f'{foul_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        elif int(foul_match[0]) == int(foul_match[1]):
            ax.text(10., -.1, f'{foul_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., -.1, f'Faltas', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., -.1, f'{foul_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        else:
            ax.text(10., -.1, f'{foul_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., -.1, f'Faltas', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., -.1, f'{foul_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{awayColor}', boxstyle='round'))
        
        # balones largos
        if int(ball_long[0].split(" ")[0]) > int(ball_long[1].split(" ")[0]):
            ax.text(10., -.2, f'{ball_long[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{homeColor}', boxstyle='round'))
            ax.text(50., -.2, f'Tiros largos', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., -.2, f'{ball_long[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        elif int(ball_long[0].split(" ")[0]) == int(ball_long[1].split(" ")[0]):
            ax.text(10., -.2, f'{ball_long[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., -.2, f'Tiros largos', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., -.2, f'{ball_long[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        else:
            ax.text(10., -.2, f'{ball_long[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., -.2, f'Tiros largos', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., -.2, f'{ball_long[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{awayColor}', boxstyle='round'))
        
        # duelos ganados
        if int(won_duel[0].split(" ")[0]) > int(won_duel[1].split(" ")[0]):
            ax.text(10., -.3, f'{won_duel[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{homeColor}', boxstyle='round'))
            ax.text(50., -.3, f'Duelos', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., -.3, f'{won_duel[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        elif int(won_duel[0].split(" ")[0]) == int(won_duel[1].split(" ")[0]):
            ax.text(10., -.3, f'{won_duel[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., -.3, f'Duelos', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., -.3, f'{won_duel[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        else:
            ax.text(10., -.3, f'{won_duel[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., -.3, f'Duelos', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., -.3, f'{won_duel[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{awayColor}', boxstyle='round'))
        
        # regates
        if int(dribble_match[0].split(" ")[0]) > int(dribble_match[1].split(" ")[0]):
            ax.text(10., -.4, f'{dribble_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{homeColor}', boxstyle='round'))
            ax.text(50., -.4, f'Regates', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., -.4, f'{dribble_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        elif int(dribble_match[0].split(" ")[0]) == int(dribble_match[1].split(" ")[0]):
            ax.text(10., -.4, f'{dribble_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., -.4, f'Regates', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., -.4, f'{dribble_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        else:
            ax.text(10., -.4, f'{dribble_match[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., -.4, f'Regates', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., -.4, f'{dribble_match[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{awayColor}', boxstyle='round'))
        
        # t. amarillas
        if int(yellow_cards[0]) > int(yellow_cards[1]):
            ax.text(10., -.5, f'{yellow_cards[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{homeColor}', boxstyle='round'))
            ax.text(50., -.5, f'Tarjetas amarillas', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., -.5, f'{yellow_cards[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        elif int(yellow_cards[0]) == int(yellow_cards[1]):
            ax.text(10., -.5, f'{yellow_cards[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., -.5, f'Tarjetas amarillas', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., -.5, f'{yellow_cards[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=15)
        else:
            ax.text(10., -.5, f'{yellow_cards[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., -.5, f'Tarjetas amarillas', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., -.5, f'{yellow_cards[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{awayColor}', boxstyle='round'))

        # t. rojas
        if int(red_cards[0]) > int(red_cards[1]):
            ax.text(10., -.6, f'{red_cards[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{homeColor}', boxstyle='round'))
            ax.text(50., -.6, f'Tarjetas rojas', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., -.6, f'{red_cards[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        elif int(red_cards[0]) == int(red_cards[1]):
            ax.text(10., -.6, f'{red_cards[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., -.6, f'Tarjetas rojas', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., -.6, f'{red_cards[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14)
        else:
            ax.text(10., -.6, f'{red_cards[0]}', ha='left', va='center', fontproperties=cuerpo.prop, size=14)
            ax.text(50., -.6, f'Tarjetas rojas', ha='center', va='center', fontproperties=cuerpo.prop, size=12)
            ax.text(90., -.6, f'{red_cards[1]}', ha='right', va='center', fontproperties=cuerpo.prop, size=14, color='white', bbox=dict(facecolor=f'{awayColor}', boxstyle='round'))
        ax.set_ylim(-0.7, 0.7)
        ax.set_xlim(0, total_value)

    def get_escudo_player(home, teamName, image_local, image_visit):
        if home == teamName:
            image = image_local
        else:
            image = image_visit
        return image   

    def get_info_player_match(ax, player_match, information_jug_match, nombre, equipos, cuerpo):
        ax.text(.5, .9, f'Jugador del partido', ha='center', va='center', fontproperties=equipos.prop, size=18)
        ax.text(.5, .2, f'{player_match}', ha='center', va='center', fontproperties=nombre.prop, size=18)
        ax.text(.65, .2, f'{information_jug_match["rating"]["num"]}', ha='center', va='center', fontproperties=cuerpo.prop, size=16, bbox=dict(facecolor='lightblue', boxstyle='round'))
        ax.text(.5, .1, f'{information_jug_match["role"]}', ha='center', va='center', fontproperties=cuerpo.prop, size=13)
    
    # def get_import_match(ax):
    #     ax.text(.198, .5, f'{stats_general["Minutes played"]["value"]}', ha='center', va='center', fontproperties=equipos.prop, size=18)
    #     ax.text(.5, .5, f'{stats_general["Goals"]["value"]}', ha='center', va='center', fontproperties=equipos.prop, size=18)
    #     ax.text(.81, .5, f'{stats_general["Assists"]["value"]}', ha='center', va='center', fontproperties=equipos.prop, size=16)
    #     ax.text(.198, .3, f'Minutos', ha='center', va='center', fontproperties=equipos.prop, size=18)
    #     ax.text(.5, .3, f'Goles', ha='center', va='center', fontproperties=equipos.prop, size=18)
    #     ax.text(.81, .3, f'Asistencias', ha='center', va='center', fontproperties=equipos.prop, size=16)

    # def get_data_attack(ax):
    #     ax.text(.1, .9, f'Tiros largos: {stats_attack["Accurate long balls"]["value"]}', ha='left', va='center', fontproperties=equipos.prop, size=11)
    #     ax.text(.1, .8, f'Regates: {stats_attack["Successful dribbles"]["value"]}', ha='left', va='center', fontproperties=equipos.prop, size=11)
    #     ax.text(.1, .7, f'Toques: {stats_attack["Touches"]["value"]}', ha='left', va='center', fontproperties=equipos.prop, size=11)
    #     ax.text(.1, .6, f'Pases en el último tercio: {stats_attack["Passes into final third"]["value"]}', ha='left', va='center', fontproperties=equipos.prop, size=11)
    #     ax.text(.1, .5, f'Tiros libres precisos: {stats_attack["Accurate crosses"]["value"]}', ha='left', va='center', fontproperties=equipos.prop, size=11)
    #     ax.text(.1, .4, f'Pérdidas de balón: {stats_attack["Dispossessed"]["value"]}', ha='left', va='center', fontproperties=equipos.prop, size=11)

    # def get_data_defense(ax):
    #     ax.text(.0, .9, f'Entradas: {stats_defensive["Tackles won"]["value"]}', ha='left', va='center', fontproperties=equipos.prop, size=11)
    #     ax.text(.0, .8, f'Intercepciones: {stats_defensive["Interceptions"]["value"]}', ha='left', va='center', fontproperties=equipos.prop, size=11)
    #     ax.text(.0, .7, f'Bloqueos: {stats_defensive["Blocks"]["value"]}', ha='left', va='center', fontproperties=equipos.prop, size=11)
    #     # ax.text(.0, .6, f'Despejes de cabeza: {stats_defensive["Headed clearance"]["value"]}', ha='left', va='center', fontproperties=equipos.prop, size=11)
    #     ax.text(.0, .6, f'Acciones defensivas: {stats_defensive["Defensive actions"]["value"]}', ha='left', va='center', fontproperties=equipos.prop, size=11)
    #     ax.text(.0, .5, f'Recuperaciones: {stats_defensive["Recoveries"]["value"]}', ha='left', va='center', fontproperties=equipos.prop, size=11)

    # def get_data_duel(ax):
    #     ax.text(.0, .9, f'Duelos ganados: {stats_duels["Duels won"]["value"]}', ha='left', va='center', fontproperties=equipos.prop, size=11)
    #     ax.text(.0, .8, f'Duelos perdidos: {stats_duels["Duels lost"]["value"]}', ha='left', va='center', fontproperties=equipos.prop, size=11)
    #     ax.text(.0, .7, f'Duelos terrestres: {stats_duels["Ground duels won"]["value"]}', ha='left', va='center', fontproperties=equipos.prop, size=11)
    #     ax.text(.0, .6, f'Duelos aéreos: {stats_duels["Aerial duels won"]["value"]}', ha='left', va='center', fontproperties=equipos.prop, size=11)
    #     ax.text(.0, .5, f'Faltas recibidas: {stats_duels["Was fouled"]["value"]}', ha='left', va='center', fontproperties=equipos.prop, size=11)
    #     ax.text(.0, .4, f'Faltas cometidas: {stats_duels["Fouls committed"]["value"]}', ha='left', va='center', fontproperties=equipos.prop, size=11)
