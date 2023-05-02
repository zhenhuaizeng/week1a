from django.shortcuts import render
from .forms import Cupcake

def home(request):
    context={}
    form = Cupcake()
    return render(request, "myApp/home.html", {"form":form})
def process(request):
    context={}
    system = request.POST.get('name', None)
    flavors = request.POST.getlist('flavor[]', None)
    context['system'] =system
    context['flavors'] = flavors
    context['total'] = len(flavors)*3.50

    return render(request, "myApp/process.html",context)