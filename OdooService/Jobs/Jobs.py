from Jobs.SyncProjectJob import syncProject
from Jobs.SyncProjectTask import syncProjectTask
from Jobs.SyncResUsers import syncUsers
from Jobs.SyncResPartners import syncPartners
import datetime

from flask_apscheduler import APScheduler
scheduler = APScheduler()

scheduler.add_job(id='syncProject', func= syncProject, trigger='interval', seconds= 600, next_run_time=datetime.datetime.now())
scheduler.add_job(id='syncProjectTask', func= syncProjectTask, trigger='interval', seconds= 600, next_run_time=datetime.datetime.now())
scheduler.add_job(id='syncResUsers', func= syncUsers, trigger='interval', seconds= 600, next_run_time=datetime.datetime.now())
scheduler.add_job(id='syncPartners', func= syncPartners, trigger='interval', seconds= 600, next_run_time=datetime.datetime.now())

# scheduler.add_job(id='syncProjectTaskUsers', func= syncProjectTaskUsers, trigger='interval', seconds= 600, next_run_time=datetime.datetime.now())