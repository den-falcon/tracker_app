from django import forms
from django.forms import widgets

from .models import Type, Status


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label='Название')
    description = forms.CharField(max_length=2000, required=False, label="Описание",
                                  widget=widgets.Textarea(attrs={"rows": 5, "cols": 50}))
    type = forms.ModelChoiceField(queryset=Type.objects.all(), label='Тип')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Статус')
