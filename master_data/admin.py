from django.contrib import admin

from .models import Education, Majoring, StatusPerkawinan, Zone, WorkPosition


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'note')
    search_fields = ('name',)


@admin.register(Majoring)
class MajoringAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'note')
    search_fields = ('name',)


@admin.register(StatusPerkawinan)
class StatusPerkawinanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'note')
    search_fields = ('name',)


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'province')
    search_fields = ('name',)


@admin.register(WorkPosition)
class WorkPositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'note')
    search_fields = ('name',)

