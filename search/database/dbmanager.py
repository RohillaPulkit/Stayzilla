from django.db import connection
print (connection.queries)
from collections import namedtuple
from search.database import dbqueries
from listing.models import Listing


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
            cursor.execute(dbqueries.search_customer_listing, [from_date, from_date, to_date, destination, num_guests])
            results = DBManager.named_tuple_fetchall(cursor)
            if len(results) == 0:
                print("None")
                return None
            else:
                valid_listings = []
                for listing in results:
                    print(listing)
                    id          = listing.LISTING_ID
                    name        = listing.NAME
                    description = listing.DESCRIPTION
                    price       = listing.PRICE
                    score       = listing.SCORE
                    card = Listing(id, name, description,price,score)
                    valid_listings.append(card)
                    print("Added")
                return valid_listings
        except Exception as error:
            print(error)
            return False
        finally:
            cursor.close()

