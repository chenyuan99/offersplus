from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index")


def privacy(request):
    return render(request, "accounts/privacy-policy.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("index")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request=request,
                          template_name="accounts/register.html",
                          context={"form": form})
    form = UserCreationForm
    return render(request=request,
                  template_name="accounts/register.html",
                  context={"form": form})


# Create your views here.
def display_profile(request):
    return render(request, "registration/profile.html")