from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'realtor', 'list_date', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'state', 'city')
    list_editable = ('is_published',)
    search_fields = ('title', 'state', 'city', 'price', 'zipcode', 'address', 'description')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)