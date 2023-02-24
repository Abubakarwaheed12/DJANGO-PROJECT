from django.shortcuts import render , HttpResponse
from django.views import View 
from django.views.generic.base import TemplateView
from django.contrib.admin.views.decorators import staff_member_required   
from django.utils.decorators import method_decorator 
 
# Create your views here. 

def profile(request):
    return render(request, 'registration/profile.html')



# Django Authentication with Class Based Views
# And Authentication Way  
@method_decorator(staff_member_required, name='dispatch')
class clasbase_profile_view(TemplateView):
    template_name='registration/profile.html' 
    
#  Now Customization of Django Authentication
