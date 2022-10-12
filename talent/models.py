from django.db import models

from django.contrib.auth.models import User
from master_data.models import Zone, Education, Majoring, StatusPerkawinan, WorkPosition


class Candidate(models.Model):
    RESULT_CHOICES = (
        (1, 'PENDING'),
        (2, 'ACCEPTED'),
        (3, 'IGNORED')
    )
    GENDER_OPTIONS = (
        (False, 'MALE'),
        (True, 'FEMALE')
    )
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    domicilie = models.TextField(blank=True, null=True)
    zone = models.ForeignKey(
        Zone, on_delete=models.CASCADE, blank=True, null=True)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    majoring = models.ForeignKey(
        Majoring, on_delete=models.CASCADE, blank=True, null=True)
    applied_position = models.ForeignKey(
        WorkPosition, on_delete=models.CASCADE)
    sofware_skills = models.TextField(default='-', null=True, blank=True)
    gender = models.BooleanField(default=0, choices=GENDER_OPTIONS)
    status = models.ForeignKey(
        StatusPerkawinan, on_delete=models.CASCADE, null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    expected_salary = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)

    is_phoned = models.BooleanField(default=False)
    is_texted = models.BooleanField(default=False)
    is_emailed = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    result = models.PositiveSmallIntegerField(
        choices=RESULT_CHOICES, default=1)
    remarks = models.TextField(blank=True, null=True, default='-')

    def __str__(self) -> str:
        try:
            return f'{self.name} ({self.id})'
        except:
            return ''

    class Meta:
        verbose_name = 'Talent'
        verbose_name_plural = 'Talents'


class Experience(models.Model):
    candidate = models.ForeignKey(
        Candidate, verbose_name="Talent", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current_company = models.BooleanField(default=False)

    def __str__(self) -> str:
        try:
            return f'{self.candidate.name} ({self.candidate.id})'
        except:
            return ''


class Interview(models.Model):
    candidate = models.ForeignKey(
        Candidate, verbose_name='talent', on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    is_present = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        try:
            return f'{self.candidate.name} ({self.candidate.id})'
        except:
            return ''


class TalentImportData(models.Model):
    no = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=255)
    phone_number = models.CharField(blank=True, null=True, max_length=255)
    email = models.CharField(blank=True, null=True, max_length=150)
    domicilie = models.CharField(blank=True, null=True, max_length=200)
    zone = models.CharField(blank=True, null=True, max_length=150)
    education = models.CharField(blank=True, null=True, max_length=200)
    majoring = models.CharField(blank=True, null=True, max_length=150)
    applied_position = models.CharField(blank=True, null=True, max_length=150)
    experience1 = models.CharField(blank=True, null=True, max_length=255)
    experience2 = models.CharField(blank=True, null=True, max_length=255)
    experience3 = models.CharField(blank=True, null=True, max_length=255)
    software_skill = models.CharField(blank=True, null=True, max_length=255)
    gender = models.CharField(blank=True, null=True, max_length=255)
    status = models.CharField(blank=True, null=True, max_length=255)
    age = models.IntegerField(blank=True, null=True)
    expected_salary = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'talent_import_data'

