from Models.ResUsers import ResUsers
from Models.ResPartners import ResPartners
import requests
from DataAccess.PostgresAccess import select, insert, engine_postgres, update

# @scheduler.task('interval', id='datasync', seconds=300,  misfire_grace_time=900, next_run_time=datetime.datetime.now())
def syncUsers():
    try:
        print('Starting job ResUsers: Sync Users.......')
        users_sql = select(ResUsers.login)
        with engine_postgres.connect() as conn:
            records= conn.execute(users_sql).fetchall()
            records= [ x.login.split('@')[0] for x in records]
            url = 'http://localhost:3000/users'
            receive = requests.get(url)
            receive = receive.json().get('users')
            # print(item['projectName'])
            for item in receive:
                if item['user_name'] in records:
                    partner_sql = select(ResPartners.id).where(ResPartners.name == item['user_name'])
                    partner= conn.execute(partner_sql).fetchone()
                    partner = partner[0]
                    
                    user_update= update(ResUsers).where(ResUsers.login == item['user_name']+"@histaff.vn").values(active = True, login = item['user_name']+"@histaff.vn", company_id =1, partner_id = partner, create_uid = 1, notification_type = 'email')
                    conn.execute(user_update)
                    conn.commit()
                else:
                    stmt= insert(ResUsers).values(active = True, login = item['user_name']+"@histaff.vn", company_id =1, partner_id = 1, create_uid = 1, notification_type = 'email')
                    conn.execute(stmt)
                    conn.commit()
    finally:
        print("Job sync Users done")
        conn.close()