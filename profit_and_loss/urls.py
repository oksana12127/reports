from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_statements', views.all_statements, name='all_statements'),
    path('profit_and_loss/p_and_l/', views.p_and_l, name='p_and_l'),
    path('profit_and_loss/sales_by_customer/', views.sales_by_customer, name='sales_by_customer'),
    path('profit_and_loss/sales_by_department/', views.sales_by_department, name='sales_by_department'),
    path('profit_and_loss/upload_result/', views.upload_result, name="upload_result"),
    # path('profit_and_loss/upload_sales/', views.upload_sales, name="upload_sales"),
]
