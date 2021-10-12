from django.http import HttpResponse
from  models import library
from django.shortcuts import render, redirect


# Create your views here.
def index (request):
    return render(request,"signup.html")

def login (request):
    return render(request,"login.html")

def signup (request):
    return render(request,"signup.html")
def add(request):
    if request.method=="POST":
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        movie=library(name=name,desc=desc,year=year,img=img)
        movie.save()

    return render(request,'add.html')

def delete(request,id):
    if request.method=='POST':
        movie=library.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
def detail(request,book_id):
    movie=library.objects.get(id=library_id)
    return render(request,"detail.html",{'movie':movie})