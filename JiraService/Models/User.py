from DataAccess.MySqlAccess import db

class User(db.Model):
    __tablename__ = 'cwd_user'
 
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(), nullable=False)
    active = db.Column(db.Integer)
    display_name= db.Column(db.String())
    email_address = db.Column(db.String())
    
    
    def __init__(self, username, active):
        self.user_name= username
        self.active= active

    def __repr__(self):
        return f'{self.id}'