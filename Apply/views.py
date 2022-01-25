# from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegistrationForm


# Create your views here.
def base(request):
    return render(request, 'Apply/home.html')


# Create your views here.
def register(response):
    # it means we adding new user from the form when someone press register,
    if response.method == "POST":
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = RegistrationForm()
    return render(response, "registration/registration.html", {"form": form})


