from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.


def activateemail(request):
    email = request.GET.get('email', '')
    id = request.GET.get('id','')
    
    if email and id:
        user = User.objects.get(id=id, email=email)
        user.is_active = True
        user.save()

        return HttpResponse('The account has been activated!, Now you can login.')
    else:
        return HttpResponse('The e-mail has not been verified yet!')