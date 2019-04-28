from django.shortcuts import render, redirect
from host.database.dbmanager import DBManager
from .forms import HostForm
from .models import NewListing

def host_listing(request):
    host_id = request.user.id

    if request.method == "POST":
        listing_form = HostForm(data=request.POST)
        print(listing_form.errors)
        if listing_form.is_valid():

            print('hey')
            listing = listing_form.cleaned_data
            print(listing)
            success = DBManager.create_listing(listing)
            if success:
                return redirect('accounts:signin')
            else:
                listing_form.add_error(None,"Please enter valid listing")
                return render(request, "accounts/signup.html", {'form': listing_form})
        else:
            return render(request, "host/host_listing.html", {'form': listing_form})
    else:
        listing = NewListing()
        listing.host_id = host_id
        listing_form = HostForm(instance=listing)
        return render(request, "host/host_listing.html", {"form": listing_form})


