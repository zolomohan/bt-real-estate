from django.shortcuts import render

from listings.models import Listing
from realtors.models import Realtor

def index(request):
    recent_listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        "recent_listings": recent_listings
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')[:3]
    mvp = Realtor.objects.all().filter(is_mvp=True)
    if mvp: mvp = mvp[0]
    context = {
        "realtors": realtors,
        "mvp": mvp
    }
    return render(request, 'pages/about.html', context)