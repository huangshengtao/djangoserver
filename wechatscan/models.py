from django.db import models
from django.http import JsonResponse,HttpResponse  #接口返回的是json，需要引入的信息
from django.views.decorators.csrf import csrf_exempt   #post接口需要引入的信息

# Create your models here.
def home(request):
    return HttpResponse('hello world,cai jia zhu !')