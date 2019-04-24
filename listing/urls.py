from django.urls import path
from .views import get_details, search_listing, search_result, get_reviews
from .api import get_popularity_trend

app_name = "listing"

urlpatterns = [
    # path('', views.index, name="index"),
    path('details', get_details, name="details"),
    path('search', search_listing, name="search"),
    path('results', search_result, name="results"),
    path('review/data', get_reviews, name='review-data'),
    path('popularity/data', get_popularity_trend, name='popularity-data')
]