"""Определяет схемы URL для приложения corp_print_app"""

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse_lazy

app_name = 'corp_print_app'

urlpatterns = [
 # Домашняя страница
   #path('login/', views.user_login, name='login'),
   path('login/', auth_views.LoginView.as_view(), name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   path('', views.index, name='index'),
   path('printed_production/', views.printed_production, name='printed_production'),
   path('password_change/', auth_views.PasswordChangeView.as_view(
      success_url=reverse_lazy('corp_print_app:password_change_done')), name='password_change'),
   path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
   path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
   path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
   path('register/', views.register, name='register'),
   path('edit/', views.edit, name='edit'),
   path('edit_template/<int:template_id>/', views.edit_template, name='edit_template'),
]