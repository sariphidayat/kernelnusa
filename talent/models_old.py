from django.db import models

from master_data.models import Zone, Majoring, WorkPosition, StatusPerkawinan, Education


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


# class Candidate(models.Model):
#     RESULT_CHOICES = (
#         (1, 'PENDING'),
#         (2, 'ACCEPTED'),
#         (3, 'IGNORED')
#     )
#     GENDER_OPTIONS = (
#         (False, 'MALE'),
#         (True, 'FEMALE')
#     )
#     name = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=15)
#     email = models.CharField(max_length=100)
#     domicilie = models.TextField(blank=True, null=True)
#     zone = models.ForeignKey(
#         Zone, on_delete=models.CASCADE, blank=True, null=True)
#     education = models.ForeignKey(Education, on_delete=models.CASCADE)
#     majoring = models.ForeignKey(
#         Majoring, on_delete=models.CASCADE, blank=True, null=True)
#     applied_position = models.ForeignKey(
#         WorkPosition, on_delete=models.CASCADE)
#     sofware_skills = models.TextField(default='-', null=True, blank=True)
#     gender = models.BooleanField(default=0, choices=GENDER_OPTIONS)
#     status = models.ForeignKey(
#         StatusPerkawinan, on_delete=models.CASCADE, null=True, blank=True)
#     age = models.PositiveSmallIntegerField(null=True, blank=True)
#     expected_salary = models.DecimalField(
#         max_digits=12, decimal_places=2, null=True, blank=True)

#     is_phoned = models.BooleanField(default=False)
#     is_texted = models.BooleanField(default=False)
#     is_emailed = models.BooleanField(default=False)
#     is_confirmed = models.BooleanField(default=False)
#     result = models.PositiveSmallIntegerField(
#         choices=RESULT_CHOICES, default=1)
#     remarks = models.TextField(blank=True, null=True, default='-')

#     def __str__(self) -> str:
#         try:
#             return f'{self.name} ({self.id})'
#         except:
#             return ''

#     class Meta:
#         verbose_name = 'Talent'
#         verbose_name_plural = 'Talents'


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

    full_name = models.CharField(_("Nama Lengkap"), max_length=100)
    birth_place = models.CharField(
        _("Tempat Lahir"), max_length=100, null=True, blank=True)
    birth_date = models.DateField(_("Tanggal Lahir"), null=True, blank=True)
    domicile = models.TextField(blank=True, null=True)
    phone_number = models.CharField(_("No. Tlp (Rumah & HP)"), max_length=30)
    religion = models.ForeignKey(
        Religion, on_delete=models.CASCADE, null=True, blank=True,
        verbose_name=_("Agama"))
    no_ktp = models.CharField(
        _("No. KTP"), max_length=50, null=True, blank=True)
    status = models.ForeignKey(
        StatusPerkawinan, on_delete=models.CASCADE, null=True, blank=True)
    nationality = models.CharField(_("Kewarganegaraan"), max_length=50)
    applied_position = models.ForeignKey(
        WorkPosition, verbose_name=_("Posisi yang diinginkan"), on_delete=models.CASCADE)
    gabung_pada = models.CharField(
        _("Bersedia bergabung dalam waktu"), max_length=50)
    # hidden data from candidate
    email = models.CharField(max_length=100)
    zone = models.ForeignKey(
        Zone, on_delete=models.CASCADE, blank=True, null=True)
    # education = models.ForeignKey(Education, on_delete=models.CASCADE)
    # sofware_skills = models.TextField(default='-', null=True, blank=True)
    gender = models.BooleanField(
        _("Jenis Kelamin"), default=0, choices=GENDER_OPTIONS)
    # age = models.PositiveSmallIntegerField(null=True, blank=True)
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
