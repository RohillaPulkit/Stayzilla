from django.shortcuts import render, redirect, HttpResponse
from . forms import SignInForm, SignUpForm
from .dbmanager import DBManager
from django.contrib.auth import login, logout


def sign_in_view(request):
    if request.method == "POST":
        sign_in_form = SignInForm(data=request.POST)

        if sign_in_form.is_valid():
            user = sign_in_form.get_user()
            login(request, user)

            return HttpResponse("User Success")
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

