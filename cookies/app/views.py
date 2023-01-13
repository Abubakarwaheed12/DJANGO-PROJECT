from django.shortcuts import render , HttpResponse , HttpResponseRedirect

# Create your views here.

def setcook(request):
    response= render(request, "cookie/setcookie.html")
    response.set_cookie("name","abu bakar waheed")
    return response


def getcook(request):
    name=request.COOKIES['name']
    return render(request , "cookie/getcookie.html" , {"name":name})
    
def delcook(request):
    response=render(request, "cookie/delcookie.html")
    response.delete_cookie('name')
    return response