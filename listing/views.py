from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect, HttpResponse

from .forms import SearchForm


def search_listing(request):

    form = SearchForm()

    return render(request, 'listing/search.html', {"searchform":form})


def search_result(request):
    return render(request, 'listing/result.html', None)


def get_details(request):
   return render(request,'listing/details.html', {'previous_price_trend': range(0, 4),
                                                  'next_price_trend': range(0, 4)})
