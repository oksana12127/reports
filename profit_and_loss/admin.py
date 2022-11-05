from pathlib import Path

from django.contrib import admin

# Register your models here.
from .models import Result
from .reports_data import save_data_by_department


class SaveData(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        save_data_by_department()
        p = Path('media/files/departments.xlsx')
        p.unlink()


admin.site.register(Result, SaveData)

# admin.site.register(AllSales)
