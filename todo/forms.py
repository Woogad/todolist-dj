from django.forms import ModelForm, DateInput
# from django import forms
from .models import *


class datePickerInput(DateInput):
    input_type = 'date'


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'deadline', 'done']

        widgets = {
            'deadline': datePickerInput(),
        }
