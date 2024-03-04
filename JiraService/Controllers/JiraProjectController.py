from Models.JiraProject import JiraProject
from flask import request
from app import app
from DataAccess.MySqlAccess import select, engine_mysql



@app.route('/projects', methods=['GET'])
def getJiraprojects():
    jr_sql= select(JiraProject)
    with engine_mysql.connect() as conn:
        records= conn.execute(jr_sql).fetchall()
        if len(records) == 0:
            return {'items': [], 'count': 0, 'message': 'success'}  # returning empty response
        else:
            result = [
                {
                    'projectId': r.id,
                    'projectName': r.pname,
                    'projectKey': r.pkey,
                    'projectDescription': r.description,
                } for r in records]
            return {'items': result, 'count': len(records), 'message': 'success'}  # returning response
        

@app.route('/project/<int:project_id>',methods=['GET'])
def get_jiraproject(pj_id):
    stmt = select(JiraProject).where(JiraProject.id== pj_id)
    # project = Project.query.get_or_404(project_id)
    if request.method == 'GET':   
        with engine_mysql.connect() as conn:
            records =conn.execute(stmt).fetchall()
            if len(records) ==0:
                return {'message': 'not found','project': [] }
            else:
                    response = {
                            'projectId': records[0].id,
                            'projectName': records[0].pname,
                            'projectKey': records[0].pkey,
                            'projectDescription':records[0].description,
                                }
            return {'message': 'success', 'project': response}  # returning response