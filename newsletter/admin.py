from django.contrib import admin

# Register your models here.
from . models import newsletters



class newsletterAdmin(admin.ModelAdmin):
    list_display=("email","date")

admin.site.register(newsletters,newsletterAdmin)
