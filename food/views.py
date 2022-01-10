from django.http import request
from django.shortcuts import get_object_or_404, redirect, render

from food.forms import foodform
from .models import foodname,foods
def foodss(request):
    a=foods.objects.all()
    return render(request,'index.html',{'a':a})
def about(request,pk):
    c=get_object_or_404(foods,pk=pk)
    return render(request,'about.html',{'c':c})
def contact(request):
    return render(request,'contact.html')
def components(request):
    return render(request,'components.html')
def project(request):
    return render(request,'project.html')
def services(request):
    return render(request,'services.html')
def delete(request,pk):
    c=get_object_or_404(foods,pk=pk)
    if request.method=='POST':
        c.delete()
        return redirect(foodss)
    return render(request,'delete.html',{'c':c})
    
def edit(request,pk):
    c=get_object_or_404(foods,pk=pk)
    f=foodform(request.POST or None,instance=c)
    if f.is_valid():
        f.save()
        return redirect(foodss)
    return render(request,'edit.html',{'f':f})



# Create your views here.
