from django.shortcuts import render , HttpResponse , HttpResponseRedirect

# Create your views here.
def set_session(request):
    request.session['name']='abu bakar'
    request.session['lname']='Waheed'
    return render(request, 'cookie/setsession.html')


def get_session(request):
    name=request.session['name']
    lname=request.session['lname']
    items=request.session.items()
    keys=request.session.keys()
    return render(request, 'cookie/getsession.html' , {'name':name , 'lname':lname , 'keys':keys , 'items':items})

def del_session(request):
    request.session.flush()
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'cookie/delsession.html')