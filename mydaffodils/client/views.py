from django.core.mail import send_mail 
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact


def index(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def project(request):
    return render(request, 'project.html')


def thankyou(request):
    return render(request, 'thankyou.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_number = request.POST.get('contact_number')

        # ✅ Debugging (terminal pe dekhne ke liye)
        print(f"Name: {name}, Email: {email}, Contact: {contact_number}, Message: {message}")

        # ✅ Validation (contact number should be exactly 10 digits)
        if not contact_number.isdigit() or len(contact_number) != 10:
            return HttpResponse("❌ Invalid Contact Number! Must be 10 digits.")

        # ✅ Save data in DB
        Contact.objects.create(
            name=name,
            email=email,
            message=message,
            contact_number=contact_number
        )

        # ✅ Send email
        send_mail(
            subject=f"New Contact from {name}",
            message=f"Message from: {email}\n\nContact Number: {contact_number}\n\n{message}",
            from_email='usertemp565@gmail.com',  # apna Gmail
            recipient_list=['usertemp565@gmail.com'],  # jaha mail receive karni hai
            fail_silently=False,
        )

        return redirect('thankyou')  # after submit redirect

    # GET request par simply form dikhao
    return render(request, 'contact.html')
