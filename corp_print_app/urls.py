"""Определяет схемы URL для приложения corp_print_app"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
 # Домашняя страница
    path('', views.index, name='index'),
    path('companies/', views.company_list, name='company_list'),
    path('companies/<int:company_id>/', views.company_detail, name='company_detail'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/<int:product_id>/order/', views.order_create, name='order_create'),
    path('order_success/', views.order_success, name='order_success'),
]