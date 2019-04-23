from django.db import connection
from collections import namedtuple
from listing.database import dbqueries


class DBManager:

    @staticmethod
    def named_tuple_fetchall(cursor):  # "Return all rows from a cursor as a namedtuple"
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]


    @staticmethod
    def get_listing_id():
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_listing_id)
            results = DBManager.named_tuple_fetchall(cursor)

            if results is None:
                return None
            else:
                listing_ids = []
                for dict in results:
                    listing_ids.append(dict.ID)
                return listing_ids
        except Exception as error:
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def add_booking(bookings):
        rows = []
        for booking in bookings:
            id = booking.id
            listing_id = booking.listing_id
            customer_id = booking.customer_id
            check_in = booking.check_in
            check_out = booking.check_out
            price = booking.price
            number_of_guests = booking.number_of_guests
            row = {'1': id,
                   '2': listing_id,
                   '3': customer_id,
                   '4': check_in,
                   '5': check_out,
                   '6': price,
                   '7': number_of_guests}
            rows.append(row)

        cursor = connection.cursor()
        try:
            print("Inserting values")
            cursor.executemany(dbqueries.insert_booking, rows)
            connection.commit()
        except ConnectionError as ex:
            obj, = ex.args
            print("Context:", obj.context)
            print("Message:", obj.message)
        finally:
            cursor.close()
