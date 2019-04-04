from django.shortcuts import render, HttpResponse


def index(request):
   return render(request,'listing/listingsearch.html')


def get_details(request):
   return render(request,'listing/details.html', {'previous_price_trend': range(0, 4),
                                                  'next_price_trend': range(0, 4)})
