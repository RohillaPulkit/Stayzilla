from django.urls import path
from .views import search_result,get_details, get_reviews, get_past_prices, get_future_prices
from .api import get_popularity_trend, get_price_trend

app_name = "listing"

urlpatterns = [
    # path('', views.index, name="index"),
    path('details', get_details, name="details"),
    path('results',search_result,name="results"),
    path('review/data', get_reviews, name='review-data'),
    path('popularity/data', get_popularity_trend, name='popularity-data'),
    path('price/data', get_price_trend, name='price-data'),
    path('past/price/data', get_past_prices, name='past-price-data'),
    path('future/price/data', get_future_prices, name='future-price-data'),
]