from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Unregister the default User model
admin.site.unregister(User)

# Re-register the User model with any customizations you want
class UserAdmin(BaseUserAdmin):
    # You can customize the admin here
    pass

admin.site.register(User, UserAdmin)
