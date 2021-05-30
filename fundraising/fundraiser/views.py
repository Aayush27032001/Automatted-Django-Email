from django.shortcuts import render
from datetime import datetime
from fundraiser.models import Donate
from django.core.mail import send_mail
# Create your views here.

def index(request):
    return render(request, "index.html")

def donate(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        donate = Donate(fname=fname, lname=lname, email=email, phone=phone, date=datetime.today())
        donate.save()
        send_mail('Donate us, together we are making change','UPI_Id:******@kotak\nBank_account: 123456789\nHappy Donation\nTimeorft Trust','timeorft@gmail.com',[email],fail_silently=False)
        return render(request, "Sucess.html")
    return render(request, "donate.html")