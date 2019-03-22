from django.shortcuts import render,redirect
from . import forms

def sign_in_view(request):
    if request.method == "POST":
        return redirect("dashboard:dashboard")
    else:
        form = forms.SignInForm
        return render(request, "accounts/signin.html", {"form": form})
