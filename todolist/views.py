from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from .models import Tasks
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, DeleteView
from todolist.forms import TasksDeleteForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# class NewTaskForm(forms.Form):
#     task = forms.CharField(label="Task ")
# Create your views here.

class TasksListView(ListView):
    model = Tasks
    template_name = 'todolist/index.html'
    context_object_name = 'tasks_list'

class TasksCreateView(CreateView):
    model = Tasks
    fields = ['title', 'description', 'priority']
    template_name = 'todolist/add.html'
    success_url = reverse_lazy('todo:index')

    def form_valid(self, form):
        if Tasks.objects.filter(title=self.request.POST.get('title')):
            form.add_error('title', ValidationError(_("Task Already exists!"), code='invalid'))
            return super().form_invalid(form)
        return super().form_valid(form)



class TasksUpdateView(UpdateView):
    model = Tasks
    fields = ['title', 'description', 'is_completed', 'priority']
    template_name = 'todolist/update.html'
    success_url = reverse_lazy('todo:index')
    context_object_name = 'task'

class TasksDeleteView(FormView):
    model = Tasks
    fields = ['title',]
    form_class = TasksDeleteForm
    template_name = 'todolist/delete_form.html'
    success_url = reverse_lazy('todo:index')
    context_object_name = 'task'

    def form_valid(self, form):
        if self.request.POST:
            Tasks.objects.filter(id__in=self.request.POST.getlist('task')).delete()
        return super().form_valid(form)

class TaskDeleteView(DeleteView):
    model = Tasks
    fields = ['title', 'description', 'is_completed', 'priority']
    template_name = 'todolist/delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('todo:index')