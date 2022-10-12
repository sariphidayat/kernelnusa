from random import choices
from secrets import choice
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from master_data.models import Zone, Education, Majoring, StatusPerkawinan, \
    WorkPosition, Religion, AdditionalQuestion


LEVEL_CHOICES = (
    ('1', 'Kurang'),
    ('2', 'Sedang'),
    ('3', 'Baik')
)


## New Form ##
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
    ready_on = models.CharField(
        _("Bersedia bergabung dalam waktu"), max_length=50)
    # hidden data from candidate
    email = models.CharField(max_length=100)
    zone = models.ForeignKey(
        Zone, on_delete=models.CASCADE, blank=True, null=True)
    gender = models.BooleanField(
        _("Jenis Kelamin"), default=0, choices=GENDER_OPTIONS)
    expected_salary = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)

    is_phoned = models.BooleanField(default=False)
    is_texted = models.BooleanField(default=False)
    is_emailed = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    result = models.PositiveSmallIntegerField(
        _("Hasil"), choices=RESULT_CHOICES, default=1)
    remarks = models.TextField(blank=True, null=True, default='-')

    def __str__(self) -> str:
        try:
            return f'{self.full_name} ({self.id})'
        except:
            return ''

    @property
    def age(self):
        try:
            today = datetime.now().date()
            born = self.birth_date
            calculated = today.year - born.year - \
                ((today.month, today.day) < (born.month, born.day))
            return calculated
        except:
            return 0
    age.fget.short_description = "Umur   "

    class Meta:
        verbose_name = 'Talent'
        verbose_name_plural = 'Talents'


class EducationList(models.Model):
    candidate = models.ForeignKey(
        Candidate, verbose_name=_("Kandidat"), on_delete=models.CASCADE)
    education = models.ForeignKey(Education, verbose_name=_(
        "Tingkat Pendidikan"), on_delete=models.CASCADE)
    school_name = models.CharField(_("Nama Instansi"), max_length=50)
    address = models.CharField(_("Tempat"), max_length=50)
    majoring = models.ForeignKey(Majoring, verbose_name=_(
        "Jurusan"), on_delete=models.CASCADE)
    date_graduate = models.IntegerField(_("Tahun Lulus"))


class Course(models.Model):
    candidate = models.ForeignKey(
        Candidate, verbose_name=_("Kandidat"), on_delete=models.CASCADE)
    type = models.CharField(_("jenis"), max_length=50)
    organizer = models.CharField(_("penyelenggara"), max_length=50)
    venue = models.CharField(_("Tempat"), max_length=50)
    year = models.IntegerField(_("Tahun"))


class Language(models.Model):
    candidate = models.ForeignKey(
        Candidate, verbose_name=_("Kandidat"), on_delete=models.CASCADE)
    name = models.CharField(_("Bahasa"), max_length=50)
    level = models.CharField(_("Level"), max_length=1, choices=LEVEL_CHOICES)


class ComputerSkill(models.Model):
    candidate = models.ForeignKey(
        Candidate, verbose_name=_("Kandidat"), on_delete=models.CASCADE)
    type = models.CharField(_("Jenis"), max_length=50)
    level = models.CharField(_("Level"), max_length=1, choices=LEVEL_CHOICES)


class Experience(models.Model):
    candidate = models.ForeignKey(
        Candidate, verbose_name="Talent", on_delete=models.CASCADE)
    company_name = models.CharField(_("Nama Perusahaan"), max_length=150)
    position = models.CharField(_("Jabatan"), max_length=150)
    start_date = models.DateField(_("Tgl Mulai"))
    end_date = models.DateField(_("Tgl Berakhir"), blank=True, null=True)
    is_current_company = models.BooleanField(_("Masih Bekerja"), default=False)
    salary = models.DecimalField(_("Gaji"), max_digits=11, decimal_places=2)
    resign_reason = models.CharField(_("Alasan Keluar"), max_length=150)

    def __str__(self) -> str:
        try:
            return f'{self.candidate.name} ({self.candidate.id})'
        except:
            return ''


class AddQuestionList(models.Model):
    candidate = models.ForeignKey(
        Candidate, verbose_name=_("Kandidat"), on_delete=models.CASCADE)
    question = models.ForeignKey(AdditionalQuestion, verbose_name=_(
        "Pertanyaan"), on_delete=models.CASCADE)
    answer = models.CharField(_("Jawaban"), max_length=150)


class Reference(models.Model):
    candidate = models.ForeignKey(
        Candidate, verbose_name=_("Kandidat"), on_delete=models.CASCADE)
    name = models.CharField(_("Nama"), max_length=150)
    position = models.CharField(_("Jabatan/Perusahaan"), max_length=150)
    relation = models.CharField(_("Hubungan"), max_length=50)
    phone = models.CharField(_("No HP"), max_length=20)


class Interview(models.Model):
    NO_INTERVIEW_CHOICES = (
        ('1', 'PERTAMA'),
        ('2', 'KEDUA'),
    )
    candidate = models.ForeignKey(
        Candidate, verbose_name='Nama', on_delete=models.CASCADE)
    date_time = models.DateTimeField(_("Waktu"))
    is_present = models.BooleanField(_("Kehadiran"), default=False)
    user = models.ManyToManyField(User, verbose_name=_("User"))
    no_interview = models.CharField(
        _("Interview yang"), max_length=1, choices=NO_INTERVIEW_CHOICES, default='1')
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        try:
            return f'{self.candidate.full_name} ({self.candidate.id})'
        except:
            return ''


class InterviewNote(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField(_("Catatan"), default="-")
    date_input = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.id}'
