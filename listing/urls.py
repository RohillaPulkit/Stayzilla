from django.urls import path
from . import views

app_name = "listing"

urlpatterns = [
    path('', views.index, name="index")
    ]

