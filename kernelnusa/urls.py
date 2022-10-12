from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, re_path
from django.shortcuts import render

from rest_framework.routers import DefaultRouter
from talent.serializers import ComputerListSerializer
from talent.views import (CandidateViewSet, CommentListApi, ComputerListApi,
                          CourseListApi, ExperienceListApi, InterviewViewSet, LainLainListApi,
                          LanguageListApi, LogUserIn, ReferenceListApi, chat_count, interview,
                          logout, whoami, EducationListApi)

router = DefaultRouter(trailing_slash=False)

router.register(r'candidates', CandidateViewSet, basename='candidate')
router.register(r'interviewees', InterviewViewSet, basename='interviewee')


def index_view(request):
    return render(request, 'dist/index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', LogUserIn.as_view(), name="login"),
    path('api/logout', logout, name="logout"),
    path('api/', include(router.urls)),
    path('api/whoami', whoami),
    path('api/chat-count/<int:id>', chat_count),
    path('api/interview/<int:id>', interview),
    path('api/education-list/<int:id>', EducationListApi.as_view()),
    path('api/course-list/<int:id>', CourseListApi.as_view()),
    path('api/language-list/<int:id>', LanguageListApi.as_view()),
    path('api/computer-list/<int:id>', ComputerListApi.as_view()),
    path('api/experience-list/<int:id>', ExperienceListApi.as_view()),
    path('api/reference-list/<int:id>', ReferenceListApi.as_view()),
    path('api/additional-list/<int:id>', LainLainListApi.as_view()),
    path('api/interview-notes/<int:interview_id>', CommentListApi.as_view()),
    re_path('.*', index_view),
    # path('', lambda x: redirect('/admin/')),
]
