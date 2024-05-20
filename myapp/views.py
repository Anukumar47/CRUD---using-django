from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student

def home(request):
    obj = Student.objects.all()
    return render(request,'home.html',{'form':obj})
    
def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
        return render(request,'create.html',{'form':form})

def update(request,id):
    obj=Student.objects.get(id=id)
    if request.method =='POST':
        form = StudentForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=obj)
        return render(request,'update.html',{'form':form})
    
def delete(request,id):
    obj = Student.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    return render(request,'delete.html')