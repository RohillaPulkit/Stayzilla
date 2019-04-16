from django.db import models

# Create your models here.
class Search(models.Model):
    class Meta:
        managed=False

    destination = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    num_guests = models.IntegerField()
