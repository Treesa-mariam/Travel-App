

from django.http import HttpResponse, request
from django.shortcuts import render
from  . models import Place,Person

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Person.objects.all()
    return render(request,"index.html", {'result':[obj,obj1]})
def about(request):
    return render(request,'about.html')


# def addition(request):
#     x = request.GET['num1']
#     y = request.GET['num2']
#     res = x + y
#     return render(request, "about.html", {'result': res})



# def contact(request):
#     return HttpResponse("you can contact")
