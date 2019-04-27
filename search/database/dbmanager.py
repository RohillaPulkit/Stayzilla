from django.db import connection
print (connection.queries)
from collections import namedtuple
from search.database import dbqueries
from search.models import Search


class DBManager:

    @staticmethod
    def named_tuple_fetchall(cursor):  # "Return all rows from a cursor as a namedtuple"
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]

    @staticmethod

    def search_customer_listing(searchquery):
        cursor = connection.cursor()
        try:
            destination = searchquery.get('destination')
            print(destination)
            from_date = searchquery.get('from_date')
            print (from_date)
            to_date = searchquery.get('to_date')
            print(to_date)
            num_guests = searchquery.get('num_guests')
            cursor.execute(dbqueries.search_customer_listing,[num_guests])
            results = DBManager.named_tuple_fetchall(cursor)
            if results is None:
                print("None")
            else:
                print(results)
        except Exception as error:
            print(error)
            return False
        finally:
            cursor.close()

