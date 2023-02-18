from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.


def home(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.send()
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            messages.success(
                request, "Your Message has been sent. Thank you for reaching out!")
            return redirect("home")

    return render(request, "home/index.html", {'form': form})
