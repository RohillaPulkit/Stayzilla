from django.db import connection
from django.db.utils import IntegrityError
from collections import namedtuple

from dashboard.database import dbqueries


class DBManager:
    @staticmethod
    def named_tuple_fetchall(cursor):  # "Return all rows from a cursor as a namedtuple"
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]

    @staticmethod
    def get_location_percent():
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_location_percent)
            results = DBManager.named_tuple_fetchall(cursor)

            if results is None:
                return None
            else:
                location_data = []
                for data in results:
                    location_data.append(data)
                return location_data
        except Exception as error:
            print("Error in GET_LOCATION_PERCENT")
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_chart_data():
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_chart_data)
            results = DBManager.named_tuple_fetchall(cursor)

            if results is None:
                return None
            else:
                chart_data = []
                for data in results:
                    chart_data.append(data)
                return chart_data
        except Exception as error:
            print("Error in get_chart_data")
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_single_private_room_data():
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_single_private_rooms)
            results = DBManager.named_tuple_fetchall(cursor)

            if results is None:
                return None
            else:
                print(results)
                singlePrivateRoom = results[0].SINGLEPRIVATEROOM
                return singlePrivateRoom
        except Exception as error:
            print("Error in get single private room_data")
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_entire_apt_data():
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_entire_apt)
            results = DBManager.named_tuple_fetchall(cursor)

            if results is None:
                return None
            else:
                entire_apt_data = results[0].ENTIREROOMS
                return entire_apt_data
        except Exception as error:
            print("Error in get entire apt_data")
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_single_shared_room_data():
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_single_shared_rooms)
            results = DBManager.named_tuple_fetchall(cursor)

            if results is None:
                return None
            else:
                SharedRooms = results[0].SHAREDROOMS
                return SharedRooms
        except Exception as error:
            print("Error in get single shared room_data")
            print(error)
            return None
        finally:
            cursor.close()