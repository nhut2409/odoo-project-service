
# from app import postgresAccess as dbAccess
from DataAccess.PostgresAccess import db
class Project(db.Model):
    __tablename__ = 'project_project'
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    active = db.Column(db.Boolean(), nullable=False)
    sequence = db.Column(db.Integer, nullable=False, default=0)
    company_id= db.Column(db.Integer, nullable = False)
    label_tasks= db.Column(db.String())
    privacy_visibility= db.Column(db.String())
    rating_status = db.Column(db.String())
    rating_status_period = db.Column(db.String())
    allow_timesheets= db.Column(db.Boolean(), nullable=False)
    alias_id = db.Column(db.Integer, nullable = False)
    x_jira_project = db.Column(db.String())
    last_update_status = db.Column(db.String())
    
    def __init__(self, name, description, active, sequence,company_id,label_tasks,privacy_visibility,rating_status,rating_status_period,allow_timesheets,alias_id,x_jira_project,last_update_status):
        self.name = name
        self.description = description
        self.active = active
        self.sequence = sequence
        self.company_id = company_id
        self.label_tasks = label_tasks
        self. privacy_visibility = privacy_visibility
        self.rating_status = rating_status
        self.rating_status_period = rating_status_period
        self.allow_timesheets = allow_timesheets
        self.alias_id = alias_id
        self.x_jira_project= x_jira_project
        self.last_update_status= last_update_status
        
    def __repr__(self):
        return f'{self.id}'

