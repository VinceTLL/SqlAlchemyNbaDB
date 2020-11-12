from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project.tables.table_execution import Schema
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

engine = create_engine('{}://{}:{}@{}/{}'.format(config['DATABASE']['dialect'],
 config['DATABASE']['user'],
  config['DATABASE']['password'],
  config['DATABASE']['host'],
  config['DATABASE']['db_name'] ),echo = True)
#engine = create_engine('postgresql://postgres:Lord1988!@localhost:5432/NBA_db_test',echo = True)
session = sessionmaker(bind = engine) # it will serve as a factory for new session object to talk with the DB
ses =session()
Base = declarative_base()
obj = Schema(Base,engine,ses)

# dialect name
#dbuser
#password
#localhost
#dbname
