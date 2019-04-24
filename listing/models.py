from django.db import models


class Search(models.Model):
    class Meta:
        managed = False

    destination = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    num_guests = models.IntegerField()


class Listing(models.Model):
    class Meta:
        managed = False
        db_table = 'Listing'

    id = models.IntegerField(primary_key=True)
    host_id = models.IntegerField
    host_name = models.TextField
    name = models.TextField
    description = models.TextField
    house_rules = models.TextField
    accommodates = models.IntegerField
    cancellation_policy = models.TextField
    room_type = models.TextField
    property_type = models.TextField
    amenities = models.TextField
    picture_url = models.URLField
    latitude = models.FloatField
    longitude = models.FloatField
    city = models.TextField
    street = models.TextField
    state = models.TextField
    zip_code = models.TextField
    score = models.IntegerField

    def __init__(self, id, host_id, host_name, name, description, house_rules, accommodates, cancellation_policy,
                 room_type, property_type, amenities, picture_url, latitude, longitude, city, street,
                 state, zip_code, score):
        self.id = id
        self.host_id = host_id
        self.host_name = host_name
        self.name = name
        self.description = description
        self.house_rules = house_rules
        self.accommodates = accommodates
        self.cancellation_policy = cancellation_policy
        self.room_type = room_type
        self.property_type = property_type
        self.amenities = amenities
        self.picture_url = picture_url
        self.latitude = latitude
        self.longitude = longitude
        self.city = city
        self.street = street
        self.state = state
        self.zip_code = zip_code
        self.score = score

    def formatted_description(self):
        return self.description.title()

    def cleaned_amenities(self):
        amenities = self.amenities
        amenities = amenities.replace('{', '')
        amenities = amenities.replace('}', '')
        amenities = amenities.replace('"', '')
        amenities = amenities.replace(',', ', ')
        return amenities.title()


class Booking(models.Model):
    class Meta:
        managed = False
        db_table = 'Booking'

    id = models.IntegerField(primary_key=True)
    listing_id = models.IntegerField
    customer_id = models.IntegerField
    check_in = models.DateField
    check_out = models.DateField
    price = models.FloatField
    number_of_guests = models.IntegerField

    def __init__(self, id, listing_id, customer_id, check_in, check_out, price, number_of_guests):
        self.id = id
        self.listing_id = listing_id
        self.customer_id = customer_id
        self.check_in = check_in
        self.check_out = check_out
        self.price = price
        self.number_of_guests = number_of_guests

    def __str__(self):
        return str(self.id) + ' ' + str(self.listing_id) + ' ' + str(self.customer_id) + ' ' + str(self.check_in) + ' ' \
               + str(self.check_out) + ' ' + str(self.price) + ' ' + str(self.number_of_guests)


class Review(models.Model):
    class Meta:
        managed = False
        db_table = 'Review'

    id = models.IntegerField(primary_key=True)
    listing_id = models.IntegerField
    reviewer_id = models.IntegerField
    reviewer_name = models.TextField
    date = models.DateField
    score = models.IntegerField
    comments = models.TextField

    def __init__(self, id, listing_id, reviewer_id, reviewer_name, date, score, comments):
        self.id = id
        self.listing_id = listing_id
        self.reviewer_id = reviewer_id
        self.reviewer_name = reviewer_name
        self.date = date
        self.score = score
        self.comments = comments