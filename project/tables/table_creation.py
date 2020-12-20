from sqlalchemy import create_engine, Column,Integer, String,ForeignKey,Float, Sequence,BigInteger
from sqlalchemy.orm import relationship
from project import Base


#Creating the first table called teams defined interms of our base class
class Teams(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key = True)
    full_name = Column(String)
    abbreviation = Column(String)
    nickname = Column(String)
    city = Column(String)
    state = Column(String)
    year_funded = Column(Integer)
    children = relationship("SeasonTotalsRegularSeason")

    def __repr__(self):
        return "Teams(id = {}, full_name = {})".format(self.id,self.full_name)



class Players(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key = True)
    full_name = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    is_active = Column(String)
    children = relationship("SeasonTotalsRegularSeason")

    def __init__(self,id,full_name,first_name,last_name,is_active):

        self.id = id
        self.full_name = full_name
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = is_active

    def __repr__(self):
        return "Teams(id = {}, full_name = {})".format(self.id,self.full_name)


class Seasons(Base):
    __tablename__ = 'regular_season'
    season_id = Column(Integer, primary_key = True)
    children = relationship("SeasonTotalsRegularSeason")


class SeasonTotalsRegularSeason(Base):
    __tablename__='regular_season_fact_table'

    reg_season_id = Column(Integer,Sequence('user_id_seq'), primary_key = True)
    player_id = Column(Integer,ForeignKey('players.id'))
    season_id = Column(Integer,ForeignKey('regular_season.season_id'))
    team_id = Column(Integer,ForeignKey('teams.id'))
    player_age = Column(Float,nullable = True)
    game_played = Column(Integer,nullable=True)
    game_started =Column(Integer, nullable=True)
    minutes = Column(Float, nullable=True)
    field_goal_made = Column(Integer, nullable=True)
    field_goal_attempts = Column(Integer, nullable=True)
    fg_pct =Column(Float, nullable=True)
    field_3goal_made = Column(Float, nullable=True)
    field_3goal_attempts = Column(Float, nullable=True)
    fg3_pct = Column(Float, nullable=True)
    free_throws_made = Column(Integer, nullable=True)
    free_throws_attempts = Column(Integer, nullable=True)
    ft_pct = Column(Float, nullable=True)
    offensive_rebounds_pct = Column(Float, nullable=True)
    defensive_rebounds_pct = Column(Float, nullable=True)
    rebounds = Column(Integer, nullable=True)
    assists = Column(Integer, nullable=True)
    steals = Column(Float, nullable=True)
    blocks = Column(Float, nullable=True)
    turnovers = Column(Float, nullable=True)
    personal_fouls = Column(Integer, nullable=True)
    points  = Column(Integer, nullable=True)


    def __repr__(self):
        return "SeasonTotalsRegularSeason(reg_season_id = {}, player_id = {})".format(self.reg_season_id,self.player_id)
