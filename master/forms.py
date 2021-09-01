from django import forms
from .models import Employee
from django.forms import widgets
from django.forms.fields import DecimalField, DateTimeField


class EmployeeForm(forms.ModelForm):
    name = forms.CharField(max_length=20, label='名前',
        help_text='フルネームを入力',
        widget = widgets.Input(attrs={'size':30}))

    created_date = forms.DateTimeField(label='作成日',
        widget = widgets.Input(attrs={'readonly':'readonly', 'size':30}))
