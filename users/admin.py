from django.contrib import admin
from .models import User, HashTags
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(HashTags)

# admin.site.register(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    ''' User admin Custom '''

    fieldsets = (
        (None, {"fields": ("username", "password", "name", "image",
                           "phone_number", "email", "major", "university", "description")},),
    )

    list_display = (
        "username",
        "name",
        "image",
        "email",
        "phone_number",
        "major",
        "university",
        "description",
    )
