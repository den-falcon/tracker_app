from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from .models import Task, Type


# class TaskForm(forms.Form):
#     summary = forms.CharField(max_length=200, required=True, label='Название')
#     description = forms.CharField(max_length=2000, required=False, label="Описание",
#                                   widget=widgets.Textarea(attrs={"rows": 5, "cols": 50}))
#     type = forms.ModelChoiceField(queryset=Type.objects.all(), label='Тип')
#     status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Статус')

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        exclude = []
        widgets = {
            'type': forms.CheckboxSelectMultiple
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['description'] == cleaned_data['summary']:
            raise ValidationError("Text of the article should not duplicate it's summary!")
        return cleaned_data
