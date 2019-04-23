from django.urls import path
from . import views
from .views import get_details
from .views import search_listing
from .views import search_result


app_name = "listing"

urlpatterns = [
    # path('', views.index, name="index"),
    path('details', get_details, name="details"),
    path('search',search_listing,name="search"),
    path('results',search_result,name="results")
]