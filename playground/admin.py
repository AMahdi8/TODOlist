from django.contrib import admin
from .models import User, Post, Like


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'phone_number']
    list_filter = ['is_staff']


admin.site.register(Post)
admin.site.register(Like)
