from Models.OdooProject import Project
from flask import request
from app import app
from DataAccess.PostgresAccess import select, engine_postgres

@app.route('/projects', methods=['GET'])
def get_projects():
    print('Getting all projects')
    projects_sql = select(Project)
    with engine_postgres.connect() as conn:
        records= conn.execute(projects_sql).fetchall()
        if len(records) == 0:
            return {'items': [], 'count': 0, 'message': 'success'}  # returning empty response
        else:
            result = [
                {
                    'projectId': p.id,
                    'projectName': p.name,
                    'projectDescription': p.description,
                    'projectActive': p.active,
                    'projectSequence': p.sequence
                } for p in records]
            return {'items': result, 'count': len(records), 'message': 'success'}  # returning response



@app.route('/project/<int:project_id>',methods=['GET'])
def get_project(project_id):
    response = {}
    stmt = select(Project).where(Project.id== project_id)
    # project = Project.query.get_or_404(project_id)
    if request.method == 'GET':   
        with engine_postgres.connect() as conn:
            records= conn.execute(stmt).fetchall()
            if len(records) ==0:
                return {'message': 'not found','project': [] }
            else:
                    response = {
                            'projectId': records[0].id,
                            'projectName': records[0].name,
                            'projectDescription':records[0].description,
                            'projectActive': records[0].active,
                            'projectSequence': records[0].sequence
                    }
            return {'message': 'success', 'project': response}  # returning response