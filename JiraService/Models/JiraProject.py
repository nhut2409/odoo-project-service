from DataAccess.MySqlAccess import db

class JiraProject(db.Model):
    __tablename__ = 'project'
 
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    pkey = db.Column(db.String())

    def __init__(self, pname, description,pkey):
        self.pname = pname
        self.description = description
        self.pkey = pkey
    def __repr__(self):
        return f'{self.id}'