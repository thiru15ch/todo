from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def index(request):
    if request.method == "POST":
        t = request.POST.get('title')
        desc = request.POST.get('description')
       
        if len(t)<1 or len(desc)<1:
            return redirect('/')

        task = Task(title=t, description=desc)
        task.save()

    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)

def edittask(request, pk):
    if request.method == "POST":
        newtitle = request.POST.get('title')
        newdesc = request.POST.get('description')       
        task = Task.objects.get(id=pk)
        if len(newtitle)<1 or len(newdesc)<1:
            return redirect('/')

        task.title = newtitle
        task.description = newdesc        
        task.save()
        return redirect('/')

    task = Task.objects.get(id=pk)
    context = {'title': task.title, 'description': task.description, "id": task.id}
    return render(request, 'edit.html', context)

def delete(request, pk):
    if request.method == "POST":
        task = Task.objects.get(id = pk)
        task.delete()
        return redirect('/')
    task = {"task": Task.objects.get(id = pk)}
    return render(request, 'delete.html', task)