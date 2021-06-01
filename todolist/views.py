from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Tasks
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from todolist.forms import TasksDeleteForm

# class NewTaskForm(forms.Form):
#     task = forms.CharField(label="Task ")
# Create your views here.

class TasksListView(ListView):
    model = Tasks
    template_name = 'todolist/index.html'
    context_object_name = 'tasks_list'

class TasksCreateView(CreateView):
    model = Tasks
    fields = ['task']
    template_name = 'todolist/add.html'
    success_url = reverse_lazy('todo:index')


class TasksUpdateView(UpdateView):
    model = Tasks
    fields = ['task']
    template_name = 'todolist/update.html'
    success_url = reverse_lazy('todo:index')
    context_object_name = 'task'

class TasksDeleteView(FormView):
    model = Tasks
    fields = ['task']
    form_class = TasksDeleteForm
    template_name = 'todolist/delete_form.html'
    success_url = reverse_lazy('todo:index')
    context_object_name = 'task'

    def form_valid(self, form):
        if self.request.POST:
            Tasks.objects.filter(id__in=self.request.POST.getlist('task')).delete()
        return super().form_valid(form)
