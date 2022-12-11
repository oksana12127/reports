import os
from pathlib import Path
from django.contrib import messages

from django.contrib import admin

# Register your models here.
from .models import Result
from .reports_data import save_all_data
# from .reports_data import save_data_by_department


# class SaveData(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)
#         save_data_by_department()
#         p = Path('media/files/departments.xlsx')
#         p.unlink()


class SaveData(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        dir = Path('media/files')
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
            print('ONE')
        super().save_model(request, obj, form, change)
        print('TWO')  # здесь падает, если проблемы с файлом
        save_all_data()

        # try:
        #     save_data_by_department()
        # except Exception:
        #     print('some error')
        #     messages.error(request, "INCORRECT FILE OR DATA FORMAT! TRY AGAIN AFTER THE FIX!")
        #     messages.error(request,
        #                    "НЕ ВІРНИЙ ФОРМАТ ФАЙЛУ АБО ДАНИХ! СПРОБУЙТЕ ЗНОВУ ПІСЛЯ ВИПРАВЛЕННЯ!")
        #
        # print('THREE')






admin.site.register(Result, SaveData)

# admin.site.register(AllSales)
