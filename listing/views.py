from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .database.dbmanager import DBManager
from .forms import SearchForm
from booking.forms import BookingForm
from booking.models import Booking

import datetime


def search_listing(request):
    form = SearchForm()

    return render(request, 'listing/search.html', {"searchform":form})


def search_result(request):
    return render(request, 'listing/result.html', None)


@login_required(login_url="/accounts/signin")
def get_details(request):
    id = '22354'
    available_dates_with_price = DBManager.get_available_dates_with_price(id)
    listing = DBManager.get_listing_for_id(id)
    best_time = DBManager.get_best_time_to_visit(id)

    check_in_date = datetime.datetime.now()
    check_in_string = check_in_date.strftime('%d-%m-%y')
    dict_dates = {'check_in': check_in_string,
                  'check_out': check_in_string,
                  'available_dates_with_price': available_dates_with_price}

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking = booking_form.cleaned_data
            success = DBManager.add_booking(booking)
            if success == True:
                return HttpResponse("Added")
            else:
                booking_form.errors['DB Error '] = success
        return render(request, 'listing/details.html', {'listing': listing,
                                                        'booking_form': booking_form,
                                                        'dict_dates': dict_dates,
                                                        'best_time': best_time,
                                                        'previous_price_trend': range(0, 4),
                                                        'next_price_trend': range(0, 4)})
    else:
        booking = Booking(1, 22354, 245914492, check_in_date,  check_in_date, 10, 4)
        booking_form = BookingForm(instance=booking)


        print(check_in_string)
        return render(request, 'listing/details.html', {'listing': listing,
                                                        'booking_form': booking_form,
                                                        'dict_dates': dict_dates,
                                                        'best_time': best_time,
                                                        'previous_price_trend': range(0, 4),
                                                        'next_price_trend': range(0, 4)})


def get_reviews(request):
    listing_id = request.GET['listing_id']
    reviews = DBManager.get_reviews(listing_id)
    return render(request, "listing/reviews.html", {"reviews": reviews})
