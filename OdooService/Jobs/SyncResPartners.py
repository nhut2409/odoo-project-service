from Models.ResPartners import ResPartners
import requests
from DataAccess.PostgresAccess import select, insert, update, engine_postgres

# @scheduler.task('interval', id='datasync', seconds=300,  misfire_grace_time=900, next_run_time=datetime.datetime.now())
def syncPartners():
    try:
        print('Starting job Partners: Sync Partners.......')
        with engine_postgres.connect() as conn:
            partners_sql = select(ResPartners.name)
            records= conn.execute(partners_sql).fetchall()
            records= [ x.name for x in records]
            url = 'http://localhost:3000/users'
            receive = requests.get(url)
            receive = receive.json().get('users')
            # print(item['projectName'])
            for item in receive:
                if item['user_name'] in records:
                    partners_update= update(ResPartners).where(ResPartners.name == item['user_name']).values(name = item['user_name'], company_id = 1, display_name = item['display_name'], lang = 'en_US', email= item['email_address'],phone='', mobile = '',email_normalized = item['email_address'])
                    conn.execute(partners_update)
                    conn.commit()
                else:
                    stmt= insert(ResPartners).values(name = item['user_name'], company_id = 1, display_name = item['display_name'], lang = 'en_US', email= item['email_address'],phone='', mobile = '',email_normalized = item['email_address'])
                    conn.execute(stmt)
                    conn.commit()
    finally:
        print("Job sync Partners done")
        conn.close()