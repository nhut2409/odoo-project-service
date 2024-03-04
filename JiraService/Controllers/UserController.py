from Models.User import User
from app import app
from DataAccess.MySqlAccess import engine_mysql, select



@app.route('/users', methods=['GET'])
def getUsers():
    user_sql= select(User).where(User.active == 1)
    with engine_mysql.connect() as conn:
        records= conn.execute(user_sql).fetchall()
        if len(records) == 0:
            return {'items': [], 'count': 0, 'message': 'success'}  # returning empty response
        else:
            result = [
                {
                    'user_name': r.user_name,
                    'display_name': r.display_name,
                    'email_address': r.email_address
                } for r in records]
            return {'users': result, 'count': len(records), 'message': 'success'}  # returning response