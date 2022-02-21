from django import forms
from .models import Task, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['project']
        widgets = {
            'type': forms.CheckboxSelectMultiple
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['users']


class AddUsers(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['users']
        widgets = {
            'users': forms.CheckboxSelectMultiple
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")
