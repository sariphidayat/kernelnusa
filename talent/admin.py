from contextlib import nullcontext
from django.contrib import admin

from admin_searchable_dropdown.filters import AutocompleteFilter

from hris.admin import AdminBase
from .models import AddQuestionList, ComputerSkill, Course, EducationList, \
    Interview, Experience, Candidate, InterviewNote, Language, Reference


class ZoneFilter(AutocompleteFilter):
    title = "Zone"
    field_name = "zone"


class PositionFilter(AutocompleteFilter):
    title = 'Position'
    field_name = 'applied_position'


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 0


class EducationInline(admin.TabularInline):
    model = EducationList
    extra = 0


class CourseInline(admin.TabularInline):
    model = Course
    extra = 0


class LanguageInline(admin.TabularInline):
    model = Language
    extra = 0


class ComputerSkillInline(admin.TabularInline):
    model = ComputerSkill
    extra = 0


class AddQuestionListInline(admin.TabularInline):
    model = AddQuestionList
    extra = 0


class ReferenceInline(admin.TabularInline):
    model = Reference
    extra = 0


# ==========================================
# Transactions                            ||
# ==========================================

class InlineNote(admin.TabularInline):
    model = InterviewNote
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False

    # def has_add_permission(self, request, obj=None):
    #     return False


@admin.register(Interview)
class InterviewAdmin(AdminBase):
    raw_id_fields = ('candidate',)
    search_fields = ('candidate__full_name',)
    list_display = ('id', 'candidate', 'users', 'date_time', 'is_present')
    list_filter = ('date_time', 'is_present')
    inlines = [InlineNote]

    def users(self, obj=None):
        try:
            return ', '.join([u.username for u in obj.user.all()])
        except Exception as e:
            return ''


@admin.register(Candidate)
class CandidateAdmin(AdminBase):
    inlines = [EducationInline, CourseInline, LanguageInline,
               ComputerSkillInline, ExperienceInline,
               AddQuestionListInline, ReferenceInline]
    list_display = (
        'id',
        'full_name',
        'phone_number',
        'domicile',
        'applied_position',
        'gender_',
        'age',
        'status',
        'result',
    )
    list_filter = (
        ZoneFilter,
        PositionFilter,
        'status',
        'gender',
        'is_phoned',
        'is_texted',
        'is_emailed',
        'is_confirmed',
    )
    search_fields = ('full_name', 'phone_number')

    def gender_(self, obj=None):
        return '👩' if obj.gender else '👨'
    gender_.short_description = "Jenis Kelamin"


admin.site.site_title = 'Alcor System'
admin.site.site_header = 'Alcor Prime Dashboard'
admin.site.index_title = 'Talent Acquisition'
