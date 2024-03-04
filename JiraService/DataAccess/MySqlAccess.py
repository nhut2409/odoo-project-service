from sqlalchemy import select, insert, update
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
import os
db=SQLAlchemy()
database_url = os.getenv('DATABASE_URL') 
engine_mysql = create_engine(database_url)