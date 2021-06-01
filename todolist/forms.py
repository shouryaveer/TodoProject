from django import forms
from todolist.models import Tasks
from django.forms import ModelForm, MultipleChoiceField, widgets

class TasksDeleteForm(ModelForm):

    task = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                        queryset=Tasks.objects.all())

    class Meta:
        model = Tasks
        fields = ['task',]
