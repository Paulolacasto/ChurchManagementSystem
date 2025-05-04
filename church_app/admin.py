from django.contrib import admin
from .models import Member, FirstTimer

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'gender', 'phone', 'date_joined')
    search_fields = ('first_name', 'last_name', 'phone')
    list_filter = ('gender', 'date_joined')
    ordering = ('-date_joined',)

@admin.register(FirstTimer)
class FirstTimerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'invited_by', 'born_again', 'date_visited')
    search_fields = ('first_name', 'last_name', 'phone')
    list_filter = ('born_again', 'date_visited')
    ordering = ('-date_visited',)
