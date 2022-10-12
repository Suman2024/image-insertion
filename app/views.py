from django.shortcuts import render

# Create your views here.
def staticimages(request):
    return render(request,'images.html')