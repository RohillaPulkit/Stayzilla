from django.shortcuts import render,redirect

from .forms import SearchForm
from search.database.dbmanager import DBManager


def search_listing(request):
    print("Here")
    if request.method == 'POST':
        form = SearchForm(data=request.POST)

        if form.is_valid():
            search_query = form.cleaned_data
            print(search_query)
            success = DBManager.search_customer_listing(search_query)
            if success:
                return redirect('listing:results')
            else:

                return render(request, "search.html", {"searchform": form})
        else:
            return render(request, 'search.html', {"searchform": form})
    else:
        form = SearchForm()
        return render(request, 'search.html', {"searchform": form})




