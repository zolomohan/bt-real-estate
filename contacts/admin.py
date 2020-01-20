from django.contrib import admin

from .models import Contact

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing_id', 'listing', 'name', 'email', 'phone', 'contacted_at',)
    list_display_links = ('id', 'listing_id', 'listing',)
    list_per_page = 25
    search_fields = ('listing', 'name', 'email', 'phone')

admin.site.register(Contact, ContactsAdmin)
