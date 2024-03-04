
# from app import postgresAccess as dbAccess
from DataAccess.PostgresAccess import db
class ResPartners(db.Model):
    __tablename__ = 'res_partner'
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    company_id= db.Column(db.Integer)
    display_name= db.Column(db.String())
    lang = db.Column(db.String())
    phone = db.Column(db.String())
    mobile = db.Column(db.String())
    email = db.Column(db.String())
    email_normalized = db.Column(db.String())
    
    
    def __init__(self, name, company_id, display_name, lang, phone, email, email_normalized):
        self.name = name
        self.display_name = display_name
        self.company_id = company_id
        self.lang = lang
        self.phone = phone
        self.email = email
        self.email_normalized = email_normalized

        
    def __repr__(self):
        return f'{self.id}'