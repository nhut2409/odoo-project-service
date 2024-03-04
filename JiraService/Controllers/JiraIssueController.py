from Models.JiraIssue import JiraIssue
from flask import request
from DataAccess.MySqlAccess import select, insert, update, engine_mysql
from app import app

# async def get_data():
#     jr_sql= select(JiraIssue)
#     try:
#         with engine.connect() as conn:
#             cur = conn.execute(jr_sql)
#             records= cur.fetchall()
#     except Exception:
#         pass
#     finally:
#         conn.close()
#         return records


@app.route('/issues', methods=['GET'])
def get_jiraissues():
    jr_sql= select(JiraIssue)
    with engine_mysql.connect() as conn:
        cur = conn.execute(jr_sql)
        records= cur.fetchmany(20)
    # records= await get_data()
        if len(records) == 0:
            return {'items': [], 'count': 0, 'message': 'success'}  # returning empty response
        else:
            result = [
                {
                    'issueId': r.id,
                    'pkey': r.pkey,
                    'issueDescription': r.description,
                    'issuePriority': r.priority,
                    'projectId': r.project
                } for r in records]
    conn.close()
    return {'items': result, 'count': len(records), 'message': 'success'}  # returning response
        

@app.route('/issues/<int:projectId>',methods=['GET'])
def getProjects(projectId):
    stmt = select(JiraIssue).where(JiraIssue.project == projectId)
    # project = Project.query.get_or_404(project_id)
    if request.method == 'GET':   
        with engine_mysql.connect() as conn:
            records = conn.execute(stmt).fetchall()
            if len(records) ==0:
                return {'message': 'not found','items': [] }
            else:
                response = [{   
                            'pkey': r.pkey,
                            'issueDescription':r.description,
                            'issuePriority': r.priority,
                            'projectId': r.project,
                            'summary':r.summary,
                            'timespent':r.timespent,
                            'duedate':r.duedate,
                            'issuestatus':r.issuestatus,
                            'reporter':r.reporter,
                            'assignee':r.assignee,
                        } for r in records ]
                return {'message': 'success', 'count': len(records), 'items': response}  # returning response