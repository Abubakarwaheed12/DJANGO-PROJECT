from django.shortcuts import render
from app.models import post
from django.core.paginator import Paginator 
# Create your views here.

def home(request):
    posts=post.objects.all()
    paginator=Paginator(posts, 2)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={
        'posts':posts,
    }
    return render(request , 'index.html' , context)