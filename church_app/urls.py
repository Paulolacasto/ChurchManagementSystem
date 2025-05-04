from django.contrib import admin
from django.urls import path
from . import views  # Import views correctly

urlpatterns = [
    path('admin/', admin.site.urls),  # ✅ Ensures Django Admin works
    path('', views.homepage, name='homepage'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # Member Management
    path('add-member/', views.add_member, name='add_member'),
    path('edit-member/<int:pk>/', views.edit_member, name='edit_member'),  # ✅ Added missing route
    path('delete-member/<int:pk>/', views.delete_member, name='delete_member'),  # ✅ Added missing route
    
    # First-Time Visitors Management
    path('add-first-timer/', views.add_first_timer, name='add_first_timer'),
    path('edit-first-timer/<int:pk>/', views.edit_first_timer, name='edit_first_timer'),
    path('delete-first-timer/<int:pk>/', views.delete_first_timer, name='delete_first_timer'),
    
    # Print Views
    path('print-members/', views.print_members, name='print_members'),
    path('print-first-timers/', views.print_first_timers, name='print_first_timers'),
]
