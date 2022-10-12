from django.contrib import admin


class AdminBase(admin.ModelAdmin):
    list_per_page = 10
