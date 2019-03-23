from django.db import models


class User(models.model):
    user_id = models.IntegerField(primary_key=True)
    password = models.TextField()
    email_address = models.EmailField()
    first_name = models.TextField()
    last_name = models.TextField()
    is_admin = models.BooleanField()

    name_map = {'userid': 'user_id', 'password': 'password', 'emailaddress': 'email_address', 'pk': 'id'}
