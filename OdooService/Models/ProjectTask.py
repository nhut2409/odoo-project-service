
# from app import postgresAccess as dbAccess
from DataAccess.PostgresAccess import db
class ProjectTask(db.Model):
    __tablename__ = 'project_task'
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    active = db.Column(db.Boolean(), nullable=False)
    sequence = db.Column(db.Integer, nullable=False, default=0)
    company_id= db.Column(db.Integer, nullable = False)
    priority= db.Column(db.String)
    kanban_state= db.Column(db.String())
    create_uid=db.Column(db.Integer)
    user_id= db.Column(db.Integer)
    x_issue= db.Column(db.String())
    date_deadline= db.Column(db.DateTime)
    stage_id= db.Column(db.Integer)
    total_hours_spent= db.Column(db.Integer)
    project_id= db.Column(db.Integer)
    display_project_id= db.Column(db.Integer)
    x_jira_project= db.Column(db.String())

    def __init__(self, name, description, active, sequence,company_id, kanban_state,user_id,create_uid,x_issue,priority, date_deadline, stage_id, total_hours_spent, project_id, display_project_id, x_jira_project):
        self.name = name
        self.description = description
        self.active = active
        self.sequence = sequence
        self.company_id = company_id
        self.priority=priority
        self.kanban_state=kanban_state
        self.user_id=user_id
        self.create_uid=create_uid
        self.x_issue=x_issue
        self.date_deadline = date_deadline
        self.stage_id = stage_id
        self.total_hours_spent = total_hours_spent
        self.project_id = project_id
        self.display_project_id = display_project_id
        self.x_jira_project= x_jira_project
        
    def __repr__(self):
        return f'{self.id}'

