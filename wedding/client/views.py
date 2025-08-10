from django.core.mail import send_mail 
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact


def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def project(request):
    return render(request,'project.html')

def thankyou(request):
    return render(request,'thankyou.html')


def contact(request):
     form =ContactForm()
     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_number = request.POST.get('contact_number')
        print("Name:", name)
        print("Email:", email)
        print("Message:", message)
        print("contact_number:", contact_number)
        print(f"Name: {name}, Email: {email}, Message: {message}")
        

        
        Contact.objects.create(name=name, email=email, message=message,contact_number=contact_number)

        send_mail(
        subject=f"New Contact from {name}",
        message=f"Message from: {email}\n\n Contact Number: {contact_number} \n\n {message} ",
          # 👈 include email inside the message
        from_email='usertemp565@gmail.com',  # use your Gmail here
        recipient_list=['usertemp565@gmail.com'],  # use your actual email
        fail_silently=False,
        )

        return redirect('thankyou')  # after submit redirect to home page

     else:
        return render(request, 'contact.html',{'form':form})

