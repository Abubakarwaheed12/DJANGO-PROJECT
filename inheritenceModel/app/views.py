from django.shortcuts import render
from app.models import Student , Teacher , Article , Publications
# Create your views here.

def home(request):
    t=Teacher.teachers.all()
    t=Teacher.objects.all()
    pub=Publications.objects.get(title='Abu Bakar Publications')
    a=Article.objects.filter(publications=pub)
    print(a)
    # print(t[1].name)
    return render(request, 'index.html')