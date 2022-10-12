from django.urls import path
from . import views

app_name = 'ecom_admin'

urlpatterns = [
    path('',views.admin_home,name='admin_home'),
    path('approve-resellers',views.approve_resellers,name='approve_reseller'),
    path('customers-list',views.customers_list,name='list'),
    path('registered_resellers',views.registered_resellers,name='registered'),
    path('password_change',views.change_password,name='change-password')
    
]