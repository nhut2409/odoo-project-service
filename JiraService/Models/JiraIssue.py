from DataAccess.MySqlAccess import db

class JiraIssue(db.Model):
    __tablename__ = 'jiraissue'
 
    id = db.Column(db.Integer, primary_key=True)
    pkey = db.Column(db.String(), nullable=False)
    summary= db.Column(db.String())
    description = db.Column(db.String())
    priority = db.Column(db.String(), nullable=False, default=0)
    project = db.Column(db.Integer, nullable= False)
    timespent=db.Column(db.Integer())
    duedate= db.Column(db.DateTime)
    reporter= db.Column(db.String())
    assignee = db.Column(db.String())
    issuestatus= db.Column(db.Integer())

    def __init__(self, pkey, summary, description, priority, project, timespent, duedate, reporter, assignee, issuestatus):
        self.pkey = pkey
        self.description = description
        self.priority= priority
        self.project=project
        self.summary= summary
        self.timespent= timespent
        self.duedate= duedate
        self.reporter= reporter
        self.assignee= assignee
        self.issuestatus= issuestatus

    def __repr__(self):
        return f'{self.id}'