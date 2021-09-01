from django.contrib import admin
from .models import Employee
from .forms import EmployeeForm


class EmployeeAdmin(admin.ModelAdmin):

    form = EmployeeForm

    list_display = ('name', 'name_furigana', 'entering_date' ,'id')

    list_filter = ['entering_date']
    search_fields = ['name', 'name_furigana']


admin.site.register(Employee, EmployeeAdmin)
