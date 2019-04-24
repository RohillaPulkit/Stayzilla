from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .database.dbmanager import DBManager
from .forms import SearchForm


def search_listing(request):
    form = SearchForm()

    return render(request, 'listing/search.html', {"searchform":form})


def search_result(request):
    return render(request, 'listing/result.html', None)


@login_required(login_url="/accounts/signin")
def get_details(request):
    id = '22354'
    listing = DBManager.get_listing_for_id(id)
    return render(request, 'listing/details.html', {'listing': listing,
                                                    'previous_price_trend': range(0, 4),
                                                    'next_price_trend': range(0, 4)})


def get_reviews(request):
    listing_id = request.GET['listing_id']
    reviews = DBManager.get_reviews(listing_id)
    return render(request, "listing/reviews.html", {"reviews": reviews})
