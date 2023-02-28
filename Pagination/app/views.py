from django.shortcuts import render
from app.models import post
from django.core.paginator import Paginator 
# Create your views here.

def home(request):
    posts=post.objects.all().order_by('id')
    paginator=Paginator(posts, 4)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={
        'posts':page_obj,
     }
    return render(request , 'index.html' , context)