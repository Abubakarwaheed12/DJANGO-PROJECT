from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
# Create your views here.

def home(request):
    
    return render(request, 'index.html')


def savename(request):
    if request.method=='POST':
        nm=request.POST.get('name')
        # a=len(nm)
        count=0
        for i in nm:
            if i==' ':
                count=count
            else:
                count+=1
        
        data={
            'length':count,
            'name':nm,
        }
        print(data)
        return JsonResponse(data)    
