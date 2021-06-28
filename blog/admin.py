from django.contrib import admin

# Register your models here.
from . models import *

class blogpostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display=["title","datepost","publish"]
    search_fields = ("title",)

class countviewsAdmin(admin.ModelAdmin):
    list_display = ["post","location","date"]
    
class commentAdmin(admin.ModelAdmin):
    list_display=["name","date","email","commentpost"]


admin.site.register(blogpost,blogpostAdmin)
admin.site.register(comments,commentAdmin)
admin.site.register(cviews,countviewsAdmin)
admin.site.register(tags)
