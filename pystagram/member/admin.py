from django.contrib import admin
from member.models import User

@admin.register(User)
class userAdmin(admin.ModelAdmin):
    ...
