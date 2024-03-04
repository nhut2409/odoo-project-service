from Models.OdooProject import Project
import requests
from DataAccess.PostgresAccess import select, insert, engine_postgres

# @scheduler.task('interval', id='datasync', seconds=300,  misfire_grace_time=900, next_run_time=datetime.datetime.now())
def syncProject():
    print('Starting job Project: Sync Project.......')
    id= ['12300','12401', '12502', '12200']
    with engine_postgres.connect() as conn:
        projects_sql = select(Project.x_jira_project)
        records= conn.execute(projects_sql).fetchall()
        records= [ x.x_jira_project for x in records]
        for i in id:
            url = 'http://localhost:3000/project/{}'
            receive = requests.get(url.format(i))
            receive = receive.json().get('project')
            # print(item['projectName'])
            if receive['projectKey'] in records:
                pass
            else:
                stmt= insert(Project).values(name ="{\"en_US\":\"" + receive['projectName'] + "\"}", x_jira_project= receive['projectKey'], description = ' ', active = True,sequence = 10,company_id = 1, label_tasks = "{\"en_US\":\"" + "Tasks"+ "\"}",privacy_visibility = 'portal',rating_status = 'stage', rating_status_period = 'monthly', allow_timesheets = True,alias_id=1, last_update_status="to_define")
                conn.execute(stmt)
                conn.commit()
    print("Job sync Projects done")
    conn.close()