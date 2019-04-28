from django.shortcuts import render, redirect
from host.database.dbmanager import DBManager
from .forms import HostForm
from .models import NewListing
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/signin")
def host_listing(request):
    user = request.user

    if request.method == "POST":
        listing_form = HostForm(data=request.POST)
        print(listing_form.errors)
        if listing_form.is_valid():

            listing = listing_form.cleaned_data
            print(listing)
            success = DBManager.create_listing(listing)
            if success:
                return HttpResponse("Your listing has been added.")
            else:
                listing_form.add_error(None,"Please enter valid listing details.")
                return render(request, "host/host_listing.html", {"form": listing_form})
        else:
            return render(request, "host/host_listing.html", {'form': listing_form})
    else:
        listing = NewListing()
        listing.host_id = user.user_id
        listing_form = HostForm(instance=listing)
        return render(request, "host/host_listing.html", {"form": listing_form})

