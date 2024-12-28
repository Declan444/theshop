from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError

from .forms import ContactForm


def contact(request):
    """
    Render the contact form page and handle form submission.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your message has been sent successfully!"
                " We will get back to you soon.",
            )
            return redirect("contact_success")
        else:
            messages.error(request, "An error occurred. Please try again.")
    else:
        form = ContactForm()
    return render(request, "contact/contact.html", {"form": form})


def contact_success(request):
    """
    Render the contact success page.
    """
    return render(request, "contact/contact_success.html")
