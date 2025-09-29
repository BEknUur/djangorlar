#python modules 
import os 
from datetime import datetime 
import pytz 
from typing import Any

#django modules 
from django.shortcuts import render

from django.http import HttpResponse, HttpRequest 
from django.views.decorators.csrf import csrf_exempt

def city_time_view(request:HttpRequest,*args:tuple[Any, ...],**kwargs:dict[str,Any])->HttpResponse:
    '''
   Params:
         request: HttpRequest object
         args: tuple of positional arguments
         kwargs: dict of keyword arguments

    '''
    tz_almaty=pytz.timezone('Asia/Almaty')
    tz_calgary=pytz.timezone('Canada/Mountain')
    tz_moscow=pytz.timezone('Europe/Moscow')
    tz_utc=pytz.UTC 

    almaty_time=datetime.now(tz_almaty)
    calgary_time=datetime.now(tz_calgary)
    moscow_time=datetime.now(tz_moscow)
    utc_time=datetime.now(tz_utc)
    
    return render(
        request=request,
        template_name='city-time.html',
        context={
            "Almaty":almaty_time.strftime('%Y-%m-%d %H:%M:%S '),
            "Calgary":calgary_time.strftime('%Y-%m-%d %H:%M:%S '),
            "Moscow":moscow_time.strftime('%Y-%m-%d %H:%M:%S '),
            "UTC":utc_time.strftime('%Y-%m-%d %H:%M:%S ')
        }
    )

def welcome_view(request:HttpRequest,*args:tuple[Any,...],**kwargs:dict[str,Any])->HttpResponse:
  '''
  Welcome page view
  params 
    request: HttpRequest object
    args: tuple of positional arguments
    kwargs: dict of keyword arguments
  
  '''

  return render(
    request=request,
    template_name='welcome.html',
    context={
      "message":"Welcome brother to Django world",
    },
    status=200,
    )


def user_view(request:HttpRequest,*args:tuple[Any, ...],**kwargs:dict[str,Any])->HttpResponse:
   '''
    User page view
    params 
      request: HttpRequest object
      args: tuple of positional arguments
      kwargs: dict of keyword arguments
   
   '''
   return render(
      request=request, 
      template_name="users.html",
      context={
         "users": ["Beknur", "Bla", "ALikhan", "Andrey", "Dmitriy", "Mariya"]
      },
      status=200
   )

    
@csrf_exempt
def count_view(request:HttpRequest,*args:tuple[Any, ...],**kwargs:dict[str,Any])->HttpResponse:
    '''
  
    Count the number of words in the input text
    params 
      request: HttpRequest object
      args: tuple of positional arguments
      kwargs: dict of keyword arguments
    
    '''
    if request.method=="POST":
       clicks+=1
       request.session["click"]=clicks
       return HttpResponse(F"{clicks}")
    
    if request.method=="DELETE":
       request.session["click"]=0
       return HttpResponse("0")
    
    return render(
       request=request,
       template_name="cnt.html",
       context={"count":clicks},
       status=200
    )