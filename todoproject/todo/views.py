import form
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .form import ToDoForm
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


class Taskdeatailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'


class Tasklistview(ListView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'task'


class Taskupdatedview(UpdateView):
    model = Task
    template_name = 'updated.html'
    context_object_name = 'task'
    fields = ('Name', 'Priority', 'Date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails', kwargs={'pk': self.object.id})


class Taskdeletedview(DeleteView):
    model = Task
    template_name = 'deleted.html'
    context_object_name = 'task'
    success_url = reverse_lazy('cbvtask')


# Create your views here.
def first_task(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(Name=name, Priority=priority, Date=date)
        task.save()
        return redirect('/')
    return render(request, 'task.html', {'task': task1})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    form1 = ToDoForm(request.POST or None, instance=task)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form1, 'task': task})
