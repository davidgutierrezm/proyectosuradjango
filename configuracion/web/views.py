from django.shortcuts import render

# Create your views here.
#render (renderizar) es PINTAR 
def Home(request):
    return render(request,'index.html')
