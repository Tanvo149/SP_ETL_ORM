from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

host=config.get("Postgres_Credentials", "hostname")
dbname=config.get("Postgres_Credentials", "database")
user=config.get("Postgres_Credentials", "username")
password=config.get("Postgres_Credentials", "password")
port=config.get("Postgres_Credentials", "port_id")

engine = create_engine("postgresql+psycopg2://{}:{}@{}:{}/{}"\
                       .format(user,password,host,port,dbname))

session = Session(engine)
Base = declarative_base()