from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login

from accounts.forms import SignInForm, SignUpForm
from accounts.database.dbmanager import DBManager


def sign_in_view(request):
    if request.method == "POST":
        sign_in_form = SignInForm(data=request.POST)

        if sign_in_form.is_valid():
            user = sign_in_form.get_user()
            login(request, user)
            return redirect("listing:search")
        else:
            return render(request, "accounts/signin.html", {"form": sign_in_form})
    else:
        sign_in_form = SignInForm()
        return render(request, "accounts/signin.html", {"form": sign_in_form})


def signup_view(request):
    if request.method == "POST":
        sign_up_form = SignUpForm(data=request.POST)

        if sign_up_form.is_valid():
            user = sign_up_form.cleaned_data
            success = DBManager.create_user(user)
            if success:
                return redirect('accounts:signin')
            else:
                sign_up_form.add_error(None,
                                       "This email address is already in use. Please use a different email address.")
                return render(request, "accounts/signup.html", {'form': sign_up_form})
        else:
            return render(request, "accounts/signup.html", {'form': sign_up_form})

    else:
        sign_up_form = SignUpForm()
        return render(request, "accounts/signup.html", {"form": sign_up_form})



# listing_ids = DBManager.get_listing_id()
# customer_ids = DBManager.get_customer_id()
# Code To Generate Random Bookings
#
# def generate_booking_data():
#     main_list = []
#     booking_id = 599186
#
#     # booking = generate_booking(1, 346911)
#     # DBManager.add_booking(booking)
#     for listing_id in listing_ids:
#         bookings = []
#         max_loop = random.randint(5, 10)
#         for i in range(1, max_loop):
#             booking = generate_booking(booking_id, listing_id)
#             incorrect = [oldBooking for oldBooking in bookings
#                          if
#                          oldBooking.check_in <= booking.check_in <= oldBooking.check_out or
#                          oldBooking.check_in <= booking.check_out <= oldBooking.check_out]
#             while len(incorrect) > 0:
#                 booking = generate_booking(booking_id, listing_id)
#                 incorrect = [oldBooking for oldBooking in bookings
#                              if
#                              oldBooking.check_in <= booking.check_in <= oldBooking.check_out or
#                              oldBooking.check_in <= booking.check_out <= oldBooking.check_out]
#             bookings.append(booking)
#             booking_id += 1
#
#         main_list.extend(bookings)
#
#     print("SIZE : "+str(len(main_list)))
#     DBManager.add_booking(main_list)
#
# def generate_booking(booking_id, listing_id):
#     customer_id = random.choice(customer_ids)
#     number_of_days = random.randint(1, 10)
#     checkin = randomDate("1/1/2018", "3/1/2019", random.random())
#     checkin_date = datetime.datetime.strptime(checkin, "%m/%d/%Y")
#     checkout = checkin_date + datetime.timedelta(days=number_of_days)
#     #
#     # print(checkin_date)
#     # print(checkout)
#
#     price = (random.randint(100, 500)) * number_of_days
#     number_of_guests = random.randint(1, 10)
#     booking = Booking(booking_id, listing_id, customer_id, checkin_date, checkout, price, number_of_guests)
#
#     # print(booking)
#     return booking
#
# def strTimeProp(start, end, format, prop):
#     """Get a time at a proportion of a range of two formatted times.
#
#     start and end should be strings specifying times formated in the
#     given format (strftime-style), giving an interval [start, end].
#     prop specifies how a proportion of the interval to be taken after
#     start.  The returned time will be in the specified format.
#     """
#
#     stime = time.mktime(time.strptime(start, format))
#     etime = time.mktime(time.strptime(end, format))
#
#     ptime = stime + prop * (etime - stime)
#
#     return time.strftime(format, time.localtime(ptime))
#
# def randomDate(start, end, prop):
#     return strTimeProp(start, end, '%m/%d/%Y', prop)