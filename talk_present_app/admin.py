from django.contrib import admin

from talk_present_app.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'salary']


admin.site.register(Employee, EmployeeAdmin)
