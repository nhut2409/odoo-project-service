
# from app import postgresAccess as dbAccess
from DataAccess.PostgresAccess import db
class ResUsers(db.Model):
    __tablename__ = 'res_users'
 
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(), nullable=False)
    active = db.Column(db.Boolean)
    company_id= db.Column(db.Integer)
    partner_id= db.Column(db.Integer)
    create_uid= db.Column(db.Integer)
    notification_type= db.Column(db.String())


    def __init__(self, login, active, company_id, partner_id, create_uid, notification_type):
        self.login = login
        self.active = active
        self.company_id = company_id
        self.partner_id = partner_id
        self.create_uid = create_uid
        self.notification_type = notification_type

        
    def __repr__(self):
        return f'{self.id}'