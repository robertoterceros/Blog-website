from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eb9f68411f660544845fb2043eaf62b5' # To protect coockies
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #Determines where the db will be located
db = SQLAlchemy(app)

from flaskblog import routes
