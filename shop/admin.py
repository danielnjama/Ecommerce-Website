from django.contrib import admin

# Register your models here.
from . models import *

class shopAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display=('name','instock','price','shopviews',"image1")
    list_editable= ('price',"image1")



admin.site.register(shop,shopAdmin)
admin.site.register(reviews)
