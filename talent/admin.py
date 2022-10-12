from django.contrib import admin

from django.utils.html import format_html

from admin_searchable_dropdown.filters import AutocompleteFilter

from .models import Interview, Experience, Candidate  # , TalentImportData


class ZoneFilter(AutocompleteFilter):
    title = "Zone"
    field_name = "zone"


class PositionFilter(AutocompleteFilter):
    title = 'Position'
    field_name = 'applied_position'


class UserFilter(AutocompleteFilter):
    title = 'User'
    field_name = 'user'


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 0


# ==========================================
# Transactions                            ||
# ==========================================

@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    search_fields = ('candidate__name',)
    list_display = ('id', 'candidate', 'date_time', 'is_present', 'user')
    list_filter = (UserFilter, 'date_time', 'is_present')


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    inlines = [ExperienceInline]
    list_display = (
        'id',
        'name',
        'phone_number',
        'domicilie',
        'education',
        'applied_position',
        'gender_',
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
    search_fields = ('name', 'phone_number')

    def gender_(self, obj=None):
        return '👩' if obj.gender else '👨'


# @admin.register(TalentImportData)
# class TalentImportDataAdmin(admin.ModelAdmin):
#     list_display = (
        # 'id',
        # 'name',
        # 'phone_number',
        # 'email',
        # 'domicilie',
        # 'zone',
        # 'education',
        # 'majoring',
        # 'applied_position',
        # 'experience1',
        # 'software_skill',
        # 'gender',
        # 'status',
        # 'age',
        # 'expected_salary',
    # )
    # list_filter = (
        # 'zone',
        # 'education',
        # 'applied_position',
        # 'gender',
        # 'status',
    # )
    # search_fields = ('name', 'phone_number')


admin.site.site_title = 'HRIS System'
admin.site.site_header = 'HRIS System Dashboard'
admin.site.index_title = 'Index Menu'

