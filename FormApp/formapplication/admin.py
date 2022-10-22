from django.contrib import admin
from .models import user_form
# Register your models here.

@admin.register(user_form)
class userAdmin(admin.ModelAdmin):
    list_display=('name' ,'email' ,'password',)
