from django.shortcuts import render
# for per view cache 
from django.views.decorators.cache import cache_page
# we can use decorator function for making cache on view or we code on urls.py  
# add middleware and caches in setting.py 

# command for creating cache table 
# python3 manage.py createcachetable  
# File System Caching 
# Local Caching 
# On db caching 


# we can also use template caching in our templates 

# {% load cache %}
# {% cache %}

# Create your views here.

def home(request):
    return render(request, 'index.html')