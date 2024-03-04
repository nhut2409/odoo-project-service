from apiflask import APIFlask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
load_dotenv()
app = APIFlask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 1


from Controllers import JiraIssueController, JiraProjectController, UserController

# app.run(host='localhost' , port = 3000)
