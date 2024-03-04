from sqlalchemy import select, insert, update
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
engine_postgres = create_engine('postgresql://nhut2409:oniichan123@localhost:5432/odoo16')
# class PostgresAccess:
#     def __init__(self, app=None) :
#         self.app = None
#         self.engine_postgres =  create_engine('postgresql://odoo:odoo@192.168.1.116:5432/odoo14_1')
#         if app:
#             self.init_app(app)
#     def engine_postgres (self):
#         return self.engine_postgres
#     def init_app(self,app):
#         self.app=app
#     def queryObject(self,OjectModel):
#         return select(OjectModel)
#     def connect (self):
#         return self.engine_postgres.connect()

    # def db(self):
    #     return SQLAlchemy(self.app)
