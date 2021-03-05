from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect



class NewTaskForm(forms.Form):
    task = forms.CharField(label="Task ")
# Create your views here.
def index(request):
    if not "tasks" in request.session:
        request.session["tasks"] = []
    return render(request, "todolist/index.html",
    {"tasks":request.session["tasks"]}
    )

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("todo:index"))
        else:
            return render(request, "todolist/add.html",
                        {"form": form})
    return render(request, "todolist/add.html",
                {"form": NewTaskForm()})

def remove(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            if task in request.session["tasks"]:
                i = request.session["tasks"].index(task)
                request.session["tasks"].pop(i)
                request.session.modified = True
            return HttpResponseRedirect(reverse("todo:index"))
        else:
            return render(request, "todolist/remove.html",
                        {"form": form})
    return render(request, "todolist/remove.html",
                {"form": NewTaskForm()})