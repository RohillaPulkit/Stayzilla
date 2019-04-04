from django.db import connection
from django.db.utils import IntegrityError
from collections import namedtuple
from . import queries
from .models import Users

class DBManager:

    @staticmethod
    def named_tuple_fetchall(cursor):  # "Return all rows from a cursor as a namedtuple"
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]

    @staticmethod
    def create_user(user):
        cursor = connection.cursor()
        try:
            email_address = user.get('email_address')
            first_name = user.get('first_name')
            last_name = user.get('last_name')
            password = user.get('password')

            cursor.execute(queries.get_user_id)

            results = DBManager.named_tuple_fetchall(cursor)
            user_id = results[0].User_ID

            if user_id is None:
                return False

            cursor.execute("INSERT INTO "
                           "USERS(User_ID, Password, Email_Address, First_Name, Last_Name)"
                           "VALUES(%s, %s, %s, %s, %s)",
                           [user_id, password, email_address, first_name, last_name])
            return True
        except IntegrityError as error:
            obj, = error.args
            print("Context:", obj.context)
            print("Message:", obj.message)
            return False
        finally:
            cursor.close()

    @staticmethod
    def authenticate_user(email_address, password):
        cursor = connection.cursor()
        try:
            cursor.execute(queries.authenticate_user, [email_address, password])
            results = DBManager.named_tuple_fetchall(cursor)

            if len(results) == 0:
                return None
            else:
                dict_user = results[0]
                print(dict_user)
                user = Users()
                user.user_id = dict_user.USER_ID
                user.password = dict_user.PASSWORD
                user.email_address = dict_user.EMAIL_ADDRESS
                user.first_name = dict_user.FIRST_NAME
                user.last_name = dict_user.LAST_NAME
                user.is_admin = dict_user.IS_ADMIN
                return user
        # except Exception as error:
        #     return None
        finally:
            cursor.close()

    @staticmethod
    def get_user(user_id):
        cursor = connection.cursor()
        try:
            cursor.execute(queries.get_user, [user_id])
            results = DBManager.named_tuple_fetchall(cursor)

            if results is None:
                return None
            else:
                dict_user = results[0]

                user = Users()

                user.user_id = dict_user.USER_ID
                user.password = dict_user.PASSWORD
                user.email_address = dict_user.EMAIL_ADDRESS
                user.first_name = dict_user.FIRST_NAME
                user.last_name = dict_user.LAST_NAME
                user.is_admin = dict_user.IS_ADMIN
                return user
        except Exception as error:
            return None
        finally:
            cursor.close()
