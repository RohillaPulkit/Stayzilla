from django.db import models


class Search(models.Model):
    class Meta:
        managed = False

    destination = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    num_guests = models.IntegerField()


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
