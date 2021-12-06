from django.shortcuts import render


# Create your views here.
def fnform(request):
    return render(request,'index.html')