from apiflask import APIFlask
from Jobs.Jobs import scheduler
# from DataAccess.PostgresAccess import PostgresAccess

app = APIFlask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nhut2409:oniichan123@localhost:5432/odoo16'   



class Config:
    SCHEDULER_API_ENABLED = True
# postgresAccess =PostgresAccess()
# postgresAccess.init_app(app)
app.config.from_object(Config())
import Controllers.ProjectController
scheduler.init_app(app)
scheduler.start()