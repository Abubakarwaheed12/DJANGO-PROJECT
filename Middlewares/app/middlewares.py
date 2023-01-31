
# Custom Middlewares in Django 
# Funtion Base View

def my_middleware(get_reponse):
    print('this is middlware first time initilization')
    def myfunction(request):
        print('this line is print before views executed')
        respone=get_reponse(request)
        print('this line is print after views executed')
        return respone
    return myfunction


# Class base middleware

class my_middleware:
    def __init__(self, get_response):
        self.get_response=get_response
        print('this is middlware first time initilization')
        
    def __call__(self , request):
        print('this line is print before views executed')
        response=self.get_response(request)
        print('this line is print after views executed')
        return response
    
# MULTIPLLE MIDDLWARE
class father_middleware:
    def __init__(self, get_response):
        self.get_response=get_response
        print('this is father_middleware first time initilization')
        
    def __call__(self , request):
        print('this line is print before views executed')
        response=self.get_response(request)
        print('this line is print after views executed')
        return response
    
class mother_middleware:
    def __init__(self, get_response):
        self.get_response=get_response
        print('this is mother_middleware first time initilization')
        
    def __call__(self , request):
        print('this line is print before views executed')
        response=self.get_response(request)
        print('this line is print after views executed')
        return response
    
class child_middleware:
    def __init__(self, get_response):
        self.get_response=get_response
        print('this is child_middleware first time initilization')
        
    def __call__(self , request):
        print('this line is print before views executed')
        response=self.get_response(request)
        print('this line is print after views executed')
        return response