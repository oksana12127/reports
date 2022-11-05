from django import forms
from .models import Result


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['name', 'file']


# class AllSalesForm(forms.ModelForm):
#     class Meta:
#         model = AllSales
#         fields = ['name', 'file']
