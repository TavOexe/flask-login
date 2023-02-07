from .entities.User import User
class ModelUser():
    @classmethod
    def login(self,db,user):
        try:
            cursor = db.cursor()
            cursor.execute("SELECT id, username,password, fullname FROM users WHERE username = '{}' ".format(user.username))
            row = cursor.fetchone()
            if row is not None:
                user = User(row[0], row[1],User.check_password(row[2],user.password), row[3])
                return user
            else:
                return  None
        except Exception as e:
            print(e)
    @classmethod
    def get_by_id(self,db,id):
        try:
            cursor = db.cursor()
            cursor.execute("SELECT id, username,password, fullname FROM users WHERE id = '{}' ".format(id))
            row = cursor.fetchone()
            if row is not None:
                return User(row[0], row[1], None, row[3])
            else:
                return  None
        except Exception as e:
            print(e)

            