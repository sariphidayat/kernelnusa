from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as log_out
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.decorators.http import require_GET

from rest_framework import filters, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import status
from rest_framework.exceptions import AuthenticationFailed, ParseError
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from talent.serializers import (CandidateSerializer, CommentSerializer,
                                ComputerListSerializer, CourseListerializer,
                                EducationListSerializer,
                                ExperienceListSerializer, InterviewSerializer,
                                LainLainSerializer, LanguageListSerializer,
                                ReferenceSerializer)

from .models import (AddQuestionList, Candidate, ComputerSkill, Course,
                     EducationList, Experience, Interview, InterviewNote,
                     Language, Reference)


class BasePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 1000


class BaseModelViewSet(viewsets.ModelViewSet):
    pagination_class = BasePagination
    # permission_classes = (IsAuthenticated,)


class BaseListView(generics.ListAPIView):
    pagination_class = BasePagination
    # permission_classes = (IsAuthenticated,)


class InterviewViewSet(BaseModelViewSet):
    serializer_class = InterviewSerializer

    def get_queryset(self):
        qs = Interview.objects.all()
        filter = self.request.query_params.get('search')
        if filter is not None:
            qs = qs.filter(
                Q(candidate__full_name__contains=filter) |
                Q(candidate__phone_number__contains=filter) |
                Q(candidate__email__contains=filter)
            )
        return qs

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        username = request.user

        # TODO: Dev only
        if settings.DEBUG:
            username = 'admin'

        if(username != 'Anonymous'):
            user = User.objects.filter(username=username).get().id
        else:
            raise AuthenticationFailed("User not Authenticated!")
        qs = self.get_queryset().filter(user__id=user)
        qs = self.filter_queryset(qs)
        serlializer = InterviewSerializer(qs, many=True)
        response.data = serlializer.data

        return response


class CandidateViewSet(BaseModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'phone_number', 'email']

    # TODO: uncomment on production
    # permission_classes = [IsAuthenticated, ]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        try:
            interview = get_list_or_404(
                Interview, user=request.user, candidate__result=1)
        except:
            # TODO: uncomment for production
            # raise ParseError("User not Authenticated!")

            # TODO: Dev only
            interview = get_list_or_404(
                Interview, user=1, candidate__result=1)
        candidates = []
        for i in interview:
            candidates.append(i.candidate.id)
        qs = self.queryset.filter(id__in=candidates)
        # print(qs.query)
        qs = self.filter_queryset(qs)
        serlializer = CandidateSerializer(qs, many=True)
        response.data = serlializer.data

        return response


class EducationListApi(BaseListView):
    queryset = EducationList.objects.all()
    serializer_class = EducationListSerializer

    def list(self, request, id, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        qs = EducationList.objects.filter(candidate__id=id)
        q = self.filter_queryset(qs)
        serializer = EducationListSerializer(q, many=True)
        response.data = serializer.data
        return response


class CourseListApi(BaseListView):
    queryset = Course.objects.all()
    serializer_class = CourseListerializer

    def list(self, request, id, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        qs = Course.objects.filter(candidate__id=id)
        q = self.filter_queryset(qs)
        serializer = CourseListerializer(q, many=True)
        response.data = serializer.data
        return response


class LanguageListApi(BaseListView):
    queryset = Language.objects.all()
    serializer_class = LanguageListSerializer

    def list(self, request, id, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        qs = Language.objects.filter(candidate__id=id)
        q = self.filter_queryset(qs)
        serializer = LanguageListSerializer(q, many=True)
        response.data = serializer.data
        return response


class ComputerListApi(BaseListView):
    queryset = ComputerSkill.objects.all()
    serializer_class = ComputerListSerializer

    def list(self, request, id, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        qs = ComputerSkill.objects.filter(candidate__id=id)
        q = self.filter_queryset(qs)
        serializer = ComputerListSerializer(q, many=True)
        response.data = serializer.data
        return response


class ExperienceListApi(BaseListView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceListSerializer

    def list(self, request, id, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        qs = Experience.objects.filter(candidate__id=id)
        q = self.filter_queryset(qs)
        serializer = ExperienceListSerializer(q, many=True)
        response.data = serializer.data
        return response


class ReferenceListApi(BaseListView):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer

    def list(self, request, id, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        qs = Reference.objects.filter(candidate__id=id)
        q = self.filter_queryset(qs)
        serializer = ReferenceSerializer(q, many=True)
        response.data = serializer.data
        return response


class LainLainListApi(BaseListView):
    queryset = AddQuestionList.objects.all()
    serializer_class = LainLainSerializer

    def list(self, request, id, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        qs = AddQuestionList.objects.filter(candidate__id=id)
        q = self.filter_queryset(qs)
        serializer = LainLainSerializer(q, many=True)
        response.data = serializer.data
        return response


class CommentListApi(generics.ListCreateAPIView):
    queryset = InterviewNote.objects.all()
    serializer_class = CommentSerializer

    def list(self, request, interview_id, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        i = InterviewNote.objects.filter(
            interview__id=interview_id).order_by('-id')
        s = CommentSerializer(i, many=True)
        response.data = s.data
        return response

    def create(self, request, *args, **kwargs):
        data = request.data
        data['user'] = User.objects.get(username=data['user']).id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['GET'])
def interview(req, id):
    try:
        i = Interview.objects.values_list(
            'candidate__id', flat=True).get(pk=id)
    except:
        raise ParseError('Data not found')

    return CandidateViewSet.as_view({'get': 'retrieve'})(req._request, pk=i)


@api_view(['GET'])
def chat_count(req, id):
    try:
        count = InterviewNote.objects.filter(interview__id=id).count()
    except:
        raise ParseError('Data not found')

    return Response({'count': count})


class LogUserIn(APIView):
    def post(self, request, *args, **kwargs):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            u = authenticate(
                request, username=username, password=password)
            if u is not None:
                login(request, u)
                return Response({'username': username, 'firstName': u.first_name, 'detail': 'Login berhasil.'})
            else:
                raise AuthenticationFailed('Username/Password salah!')
        except Exception as e:
            raise ParseError(f'Gagal Login: {e}')


@api_view(['GET'])
def whoami(request):
    return Response({'detail': f'You are {request.user}'})


@require_GET
def logout(req):
    log_out(req)
    return JsonResponse({'detail': 'Logout berhasil.'})
