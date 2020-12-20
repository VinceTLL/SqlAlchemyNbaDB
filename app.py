from project import ses,obj
from project.tables.table_execution import Schema
from project.tables.table_creation import Teams,Players,Seasons,SeasonTotalsRegularSeason
from project.player_stats.load_stats import teams_df, players_df,return_player_stats,season_data
import pandas as pd
import numpy as np

'''
# adding teams data
Teams_rows = []
for ids,full_name,abbreviation,nickname,city,state,year_funded in teams_df.itertuples(index = False):
    Teams_rows.append(Teams(id = ids,full_name=full_name,abbreviation= abbreviation,
    nickname = nickname,city = city,state=state,year_funded=year_funded))


# adding players data
Players_rows = []
for ids, full_name,first_name,last_name,is_active  in players_df.itertuples(index = False):
    Players_rows.append(Players(id = ids,full_name=full_name,first_name=first_name,
    last_name=last_name,is_active=is_active))



# adding season data
Seasons_rows = []
for season_id in season_data.itertuples(index = False):
    Seasons_rows.append(Seasons(season_id = season_id))




def load_rows(df,table,*args):
    container = []
    for args in df.itertuples(index = False):
        container.append(table(args))
    return container
Players_rows = load_rows(players_df,Players, 'id', 'full_name','first_name','last_name','is_active')
'''


data = []
temp_df = return_player_stats()
cols = temp_df.columns.tolist()
final_cols = temp_df.loc[:,[col for col in cols if col not in ('data_type','TEAM_ABBREVIATION','LEAGUE_ID')]].columns.tolist()
#lenght = len(ses.query(Players.id))
count = 1

for id in ses.query(Players.id):
    print(id,count)
    temp = return_player_stats(player_id = id)[final_cols].replace([None],np.nan)
    temp  = temp.replace(np.nan, 0).copy()
    temp['SEASON_ID'] = temp.SEASON_ID.map(lambda x: int(x[:4]))

    count+=1
    for player_id,season_id,team_id,player_age,game_played,\
        game_started,minutes,field_goal_made,field_goal_attempts,fg_pct,\
        field_3goal_made,field_3goal_attempts,fg3_pct,free_throws_made,free_throws_attempts,ft_pct,\
        offensive_rebounds_pct, defensive_rebounds_pct,rebounds,assists,steals,blocks,turnovers,personal_fouls, points in temp.itertuples(index = False):
        if team_id == 0 or team_id not in  teams_df['id'].values:
            print('{}, team not found'.format(id))
            continue
        data.append(SeasonTotalsRegularSeason(player_id=player_id,season_id=season_id,team_id=team_id,
        player_age=player_age,game_played=game_played,game_started=game_started,minutes=minutes,
        field_goal_made=field_goal_made,field_goal_attempts=field_goal_attempts,
        fg_pct=fg_pct,field_3goal_made=field_3goal_made,field_3goal_attempts=field_3goal_attempts,
        fg3_pct=fg3_pct,free_throws_made=free_throws_made,free_throws_attempts=free_throws_attempts,
        ft_pct=ft_pct, offensive_rebounds_pct=offensive_rebounds_pct,defensive_rebounds_pct=defensive_rebounds_pct,
        rebounds=rebounds,assists=assists,steals=steals,blocks=blocks,turnovers=turnovers,personal_fouls=personal_fouls,
        points=points))

#obj.create_tables()
obj.add_rows(row_data=[data])
obj.commit_rows()
