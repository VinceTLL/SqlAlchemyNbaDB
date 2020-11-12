import pandas as pd
import numpy as np
from nba_api.stats.static import teams
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import json
pd.set_option('max_columns', 500)
pd.set_option('max_colwidth', 500)
pd.set_option('max_rows', 500)
import urllib.parse
import re


teams_df = pd.DataFrame(teams.get_teams())
players_df = pd.DataFrame(players.get_players())
season_data = pd.DataFrame(np.arange(1946,2021,1),columns = ['Season_id'])
#player_stats_tables = player_stats_tables = [ json.loads(data)['resultSets'][index]['name']  for index in range(len(json.loads(data)['resultSets'])) ]

def return_player_stats(player_id = 76003 ,stats_type = 'SeasonTotalsRegularSeason'):
    data = playercareerstats.PlayerCareerStats(player_id).get_json() # stats player in json format
    player_stats_tables = [ json.loads(data)['resultSets'][index]['name']  for index in range(len(json.loads(data)['resultSets']))] # extracting the names of tables of statsplayer
    stats_table_df = pd.DataFrame(player_stats_tables, columns = ['stats_tables'])
    index = stats_table_df.loc[stats_table_df.stats_tables.str.contains(stats_type),:].index.values[0]  # returninig the index matching the stats table
    temp  = pd.DataFrame(json.loads(data)['resultSets'][index]['rowSet'], columns=json.loads(data)['resultSets'][index]['headers']) # tranforming the stats table in a dataframe
    temp['data_type'] = json.loads(data)['resultSets'][index]['name'] # adding the name of  the type of stats to the table
    return temp
