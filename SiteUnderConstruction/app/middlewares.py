from django.shortcuts import render
#  if our full site is break or some code is break then we custom middle ware shows this page
class SiteUnderConstructionMiddleware:
    def __init__(self , get_reponse):
        self.get_reponse=get_reponse
        
    def __call__(self , request):
        print('call from middleware')
        response=render(request, 'index.html')
        print('call from middleware after View')
        return response