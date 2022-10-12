from django.contrib import admin

from hris.admin import AdminBase
from .models import AdditionalQuestion, Education, Majoring, \
    StatusPerkawinan, Zone, WorkPosition, Religion


@admin.register(Education)
class EducationAdmin(AdminBase):
    list_display = ('id', 'name', 'note')
    search_fields = ('name',)


@admin.register(Religion)
class ReligionAdmin(AdminBase):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Majoring)
class MajoringAdmin(AdminBase):
    list_display = ('id', 'name', 'note')
    search_fields = ('name',)


@admin.register(StatusPerkawinan)
class StatusPerkawinanAdmin(AdminBase):
    list_display = ('id', 'name', 'note')
    search_fields = ('name',)


@admin.register(Zone)
class ZoneAdmin(AdminBase):
    list_display = ('id', 'name', 'type', 'province')
    search_fields = ('name',)


@admin.register(WorkPosition)
class WorkPositionAdmin(AdminBase):
    list_display = ('id', 'name', 'note')
    search_fields = ('name',)


@admin.register(AdditionalQuestion)
class AdditionalQuestionAdmin(AdminBase):
    list_display = ('text',)
