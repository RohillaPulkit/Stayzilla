from django.shortcuts import render, redirect
from django.forms import ValidationError
from .forms import SearchForm
import json
import datetime


def search_listing(request):
    print("Here")
    if request.method == 'POST':
        form = SearchForm(data=request.POST)

        if form.is_valid():
            search_query = form.cleaned_data
            json_object = json.dumps(search_query, default=date_converter)
            print(json_object)
            request.session['search_query'] = json_object
            print(search_query)

            return redirect('listing:results')
        else:
            print("FORM ERROR")
            return render(request, 'search.html', {"searchform": form})
    else:
        form = SearchForm()
        return render(request, 'search.html', {"searchform": form})


def date_converter(o):
    if isinstance(o, datetime.date):

        return o.strftime('%d-%m-%y')


