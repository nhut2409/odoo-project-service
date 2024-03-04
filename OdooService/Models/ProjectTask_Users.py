
# from app import postgresAccess as dbAccess
from DataAccess.PostgresAccess import db
class ProjectTaskUsers(db.Model):
    __tablename__ = 'project_task_user_rel'
 
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable= False)
    stage_id= db.Column(db.Integer)
    create_uid= db.Column(db.Integer)


    def __init__(self, task_id, user_id, stage_id, create_uid):
        self.task_id = task_id
        self.user_id= user_id
        self.stage_id= stage_id
        self.create_uid = create_uid

        
    def __repr__(self):
        return f'{self.id}'