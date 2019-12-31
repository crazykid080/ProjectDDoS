import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = db.create_engine('sqlite:///gameDB.sqlite')
Session = sessionmaker(bind=engine)
metadata = db.MetaData()
connection = engine.connect()
Base = declarative_base()