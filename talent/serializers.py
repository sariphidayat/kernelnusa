from dataclasses import field, fields
from rest_framework import serializers

from .models import AddQuestionList, Candidate, ComputerSkill, EducationList, Course, Experience, Interview, InterviewNote, Language, LEVEL_CHOICES, Reference
from master_data.models import AdditionalQuestion, Majoring, WorkPosition, Religion, \
    StatusPerkawinan, Education

LEVEL = {}
for m in LEVEL_CHOICES:
    LEVEL[m[0]] = m[1]


class InterviewSerializer(serializers.ModelSerializer):
    candidate = None
    candidate_id = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    domicile = serializers.SerializerMethodField()
    applied_for = serializers.SerializerMethodField()
    phone_number = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = Interview
        fields = '__all__'

    def get_phone_number(self, obj):
        return obj.candidate.phone_number

    def get_email(self, obj):
        return obj.candidate.email

    def get_candidate_id(self, obj):
        return obj.candidate.id

    def get_full_name(self, obj):
        return obj.candidate.full_name

    def get_gender(self, obj):
        return obj.candidate.gender

    def get_age(self, obj):
        return obj.candidate.age

    def get_domicile(self, obj):
        return obj.candidate.domicile

    def get_applied_for(self, obj):
        try:
            position = WorkPosition.objects.get(
                pk=obj.candidate.applied_position.id)
            return position.name
        except Exception as e:
            print(e)
            return 'unkown'


class CandidateSerializer(serializers.ModelSerializer):
    applied_for = serializers.SerializerMethodField()
    marriage_status = serializers.SerializerMethodField()
    religion_name = serializers.SerializerMethodField()

    class Meta:
        model = Candidate
        fields = '__all__'

    def get_marriage_status(self, obj):
        try:
            marriage_status = StatusPerkawinan.objects.get(pk=obj.status.id)
            return marriage_status.name
        except Exception as e:
            print(e)
            return 'unknown'

    def get_religion_name(self, obj):
        try:
            religion = Religion.objects.get(pk=obj.religion.id)
            return religion.name
        except Exception as e:
            print(e)
            return 'unknown'

    def get_applied_for(self, obj):
        try:
            position = WorkPosition.objects.get(pk=obj.applied_position.id)
            return position.name
        except Exception as e:
            print(e)
            return 'unkown'


class EducationListSerializer(serializers.ModelSerializer):
    education_name = serializers.SerializerMethodField()
    majoring_name = serializers.SerializerMethodField()

    class Meta:
        model = EducationList
        fields = '__all__'

    def get_education_name(self, obj):
        edu = Education.objects.get(id=obj.education.id)
        return edu.name

    def get_majoring_name(self, obj):
        major = Majoring.objects.get(id=obj.majoring.id)
        return major.name


class CourseListerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LanguageListSerializer(serializers.ModelSerializer):
    level_name = serializers.SerializerMethodField()

    class Meta:
        model = Language
        fields = '__all__'

    def get_level_name(self, obj):
        return LEVEL[obj.level]


class ComputerListSerializer(serializers.ModelSerializer):
    level_name = serializers.SerializerMethodField()

    class Meta:
        model = ComputerSkill
        fields = '__all__'

    def get_level_name(self, obj):
        return LEVEL[obj.level]


class ExperienceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'


class LainLainSerializer(serializers.ModelSerializer):
    question_text = serializers.SerializerMethodField()

    class Meta:
        model = AddQuestionList
        fields = "__all__"

    def get_question_text(self, obj):
        q = AdditionalQuestion.objects.get(id=obj.question.id)
        return q.text


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = InterviewNote
        read_only_fields = ('date_input', 'date_updated')
        fields = '__all__'

    def get_username(self, obj):
        return obj.user.username
