from django.contrib import admin

from showdata.models import students , Author , Book , Publisher
# Register your models here.

@admin.register(students)
class studentAdmin(admin.ModelAdmin):
    list_display=('id','name','lname','password')
    
    
# other way to add 
# admin.site.register(students)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
