from django.shortcuts import render
from app1.form import person

# Create your views here.
def index(request):
    form=person


    return render(request,"main.html",{'forms':form})