from django.contrib import admin
from django.urls import path
from main.views import read_orders, create_edit_delete_order, create_edit_delete_post, read_posts, read_employees, \
    create_edit_delete_employee


urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', read_orders),
    path('orders/<int:pk>/', read_orders),
    path('order/<int:pk>/', create_edit_delete_order),
    path('posts/', read_posts),
    path('posts/<int:pk>/', read_posts),
    path('post/<int:pk>/', create_edit_delete_order),
    path('employees/', read_employees),
    path('employees/<int:pk>/', read_employees),
    path('employee/<int:pk>/', create_edit_delete_employee),
]
