from init import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gameDB.sqlite'
db = SQLAlchemy(app)