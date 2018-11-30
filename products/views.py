from django.shortcuts import render

# reate your views here.
def home(request):
    return render(request,'products/home.html')
