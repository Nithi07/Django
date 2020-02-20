from django.shortcuts import render, redirect  
from .forms import Edatass  
from .models import Edata  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = Edatass(request.POST)  
        if form.is_valid():
            form.save()
            return redirect("/show")   
    else:  
        form = Edatass()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Edata.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Edata.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Edata.objects.get(id=id)  
    form = Edatass(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Edata.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  