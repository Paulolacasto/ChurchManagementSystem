from django.contrib import admin
from django.urls import path, include
from church_app import views  # Import views from `church_app`

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', views.homepage, name='homepage'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('add-member/', views.add_member, name='add_member'),
    path('add-first-timer/', views.add_first_timer, name='add_first_timer'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # ✅ Add missing paths
    path('edit-member/<int:pk>/', views.edit_member, name='edit_member'),
    path('edit-first-timer/<int:pk>/', views.edit_first_timer, name='edit_first_timer'),
    path('delete-member/<int:pk>/', views.delete_member, name='delete_member'),
    path('delete-first-timer/<int:pk>/', views.delete_first_timer, name='delete_first_timer'),
    path("print-members/", views.print_members, name="print_members"),
    path("print-first-timers/", views.print_first_timers, name="print_first_timers"),
]
