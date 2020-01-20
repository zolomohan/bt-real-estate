from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']

        contact = Contact(listing=listing, listing_id=listing_id, user_id=user_id, name=name, email=email, phone=phone, message=message)
        contact.save()

        messages.success(request, "Your Inquiry has been submitted, The realtor will get back to you soon.")
        return redirect('/listings/'+listing_id)