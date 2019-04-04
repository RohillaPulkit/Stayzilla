from django.urls import path
from . import views
from .views import get_details

app_name = "listing"

urlpatterns = [
    path('', views.index, name="index"),
    path('details', get_details, name="details")
]