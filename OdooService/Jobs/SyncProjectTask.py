from Models.OdooProject import Project
from Models.ProjectTask import ProjectTask
from Models.ResUsers import ResUsers
from Models.ProjectTask_Users import ProjectTaskUsers
# from Models.ResUsers import re
import requests
from DataAccess.PostgresAccess import select, insert, engine_postgres, update

def syncProjectTask():
        print('Starting job Project Task: Sync ProjectTask.......')
        id= ['12300','12401', '12502', '12200']
        projecttasks_sql = select(ProjectTask.id, ProjectTask.stage_id, ProjectTask.create_uid, ProjectTask.x_issue, ProjectTask.user_id)
        projects_sql = select(Project.id, Project.x_jira_project)
        projecttask_user_select = select(ProjectTaskUsers.task_id)
        with engine_postgres.connect() as conn:
            projecttasks= conn.execute(projecttasks_sql)
            projecttasks = projecttasks.mappings().all()
            
            # projecttasks_list = [projecttask.x_issue for projecttask in projecttasks]
            projects= conn.execute(projects_sql).fetchall()
            projects_list= [project for project in projects]
            projecttask_users= conn.execute(projecttask_user_select).fetchall()
            projecttask_users_list= [projecttask_user.task_id for projecttask_user in projecttask_users]
            for i in id:

                    url= 'http://localhost:3000/issues/{}'
                    receive = requests.get(url.format(i))
                    receive = receive.json().get('items')
                    for item in receive:
                        # try:
                            count= 0
                            try:
                                for projecttask in projecttasks:
                                    if item['pkey'] in projecttask.values():
                                        count+=1
                                if count== 1:
                                    total_hours_spent = 0
                                    duedate = None 
                                    if item['timespent']!=None :
                                        total_hours_spent = int(item['timespent'])/(60*60)
                                    if item['duedate']!=None :
                                        duedate=item['duedate']
                                    reporter_email = item['reporter']+ "@histaff.vn"
                                    assignee_email = item['assignee']+ "@histaff.vn"
                                    query_reporter_sql=select(ResUsers).where(ResUsers.login == reporter_email)
                                    query_assignee_sql= select(ResUsers).where(ResUsers.login == assignee_email)
                                    reporter= conn.execute(query_reporter_sql).fetchone()
                                    reporter= reporter[0]
                                    assignee=conn.execute(query_assignee_sql).fetchone()
                                    assignee= assignee[0]
                                    task_state = 0
                                    if item['issuestatus'] == '6' : #close
                                        task_state = 6
                                    elif item['issuestatus'] == '1'  :#Open
                                        task_state =1
                                    elif item['issuestatus'] == '3'  :#In Progress
                                        task_state = 2
                                    elif item['issuestatus'] == '4'  :#Reopened
                                        task_state = 3
                                    elif item['issuestatus'] == '5'  :#Resolved
                                        task_state = 4
                                    elif item['issuestatus'] == '10000'  :#Pending
                                        task_state=5
                                    elif item['issuestatus'] == '10001'  :#tested
                                        task_state=None   
                                    query_projecttask = select(ProjectTask.x_jira_project).where(ProjectTask.x_issue == item['pkey'])
                                    x_jira_project_projecttask = conn.execute(query_projecttask).fetchone()
                                    x_jira_project_projecttask = x_jira_project_projecttask[0]
                                    for project in projects_list:
                                        if (x_jira_project_projecttask != project[1]):
                                            pass
                                        else:
                                            projecttask_update= update(ProjectTask).where(ProjectTask.x_issue == item['pkey']).values(name = item['summary'], project_id= project[0], display_project_id= project[0], description = item['issueDescription'], active = True, priority = item['issuePriority'], sequence=10, kanban_state='normal', company_id = 1, stage_id = task_state, total_hours_spent= total_hours_spent, date_deadline= duedate, create_uid=reporter, user_id= assignee, x_issue = item['pkey'])
                                            conn.execute(projecttask_update)
                                            conn.commit()
                            
                                elif count ==0:
                                    stmt= insert(ProjectTask).values(name = item['summary'], description = item['issueDescription'], active = True, priority = item['issuePriority'], sequence=10, kanban_state='normal', company_id = 1, create_uid =1, x_issue = item['pkey'], x_jira_project= item['pkey'].split('-')[0])
                                    conn.execute(stmt)
                                    conn.commit()
                            except:
                                print("error at reporter: ",reporter_email)
                                print("error at assignee:", assignee_email)
                        # except:
                            
            # sync ProjectTask_User_Rel
            for projecttask in projecttasks:
                try:
                    if projecttask['id'] in projecttask_users_list:
                        pass
                    else:
                        projecttask_user_insert= insert(ProjectTaskUsers).values(task_id= projecttask['id'], user_id = projecttask['user_id'], stage_id = projecttask['stage_id'], create_uid = projecttask['create_uid'])
                        conn.execute(projecttask_user_insert)
                        conn.commit()
                except:
                    print(projecttask)

        print("Job sync ProjectTasks done")
        conn.close()