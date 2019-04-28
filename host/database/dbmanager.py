from django.db import connection
from host.database import dbqueries
from datetime import datetime, date, timedelta


class DBManager:

    @staticmethod
    def create_listing(listing):
        cursor = connection.cursor()
        try:
            name = listing.get('name')
            room_type = listing.get('room_type')
            property_type = listing.get('property_type')

            street = listing.get('street')
            state = listing.get('state')
            city = listing.get('city')
            zip_code = listing.get('zip_code')

            amenities = listing.get('amenities')

            house_rules = listing.get('house_rules')
            description = listing.get('description')

            accommodates = listing.get('accommodates')
            picture_url = listing.get('picture_url')
            cancellation_policy = listing.get('cancellation_policy')

            start_date = listing.get('start_date')
            end_date=listing.get('end_date')

            cursor.execute(dbqueries.insert_listing,
                           [name, room_type, property_type, street,state,city,zip_code,amenities,house_rules,description,accommodates,picture_url,cancellation_policy])

            price=listing.get('price')

            d1 = start_date
            d2 = end_date

            dd = [d1 + timedelta(days=x)
            for x in range((d2 - d1).days + 1)]

            dates = []
            for d in dd:
                dates.append(d)

            availabilities = []
            for date in dates:
                date_string = datetime.strftime(date, '%d-%m-%y')
                avail = {'availability_date':date_string, 'price': price, 'is_available': 1}
                availabilities.append(avail)

            DBManager.add_availability(availabilities)

        except Exception as ex:
            print("Error Message:", ex)
        finally:
            cursor.close()

    @staticmethod
    def add_availability(data):
        rows = []
        for availability in data:
            available = availability['availability_date']
            pri = availability['price']
            is_avail = availability['is_available']

            row = {'1': available,
                   '2': pri,
                   '3': is_avail}
            rows.append(row)

        cursor = connection.cursor()
        try:
            print(rows)
            cursor.executemany(dbqueries.add_availability, rows)
            connection.commit()
        except Exception as ex:
            print(ex)
        finally:
            cursor.close()


