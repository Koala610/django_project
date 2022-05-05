from django.contrib import admin
from users.models import User, UserManager
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'requests', 'friends')
    search_fields = ('username', 'email')
    ordering = ('username', )
    filter_horizontal = ()
    list_filter = ('username', 'email')
    fieldsets = ()


