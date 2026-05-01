from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    About,
    ContactMessage,
    Education,
    Experience,
    Language,
    Project,
    Skill,
)
from .serializers import (
    AboutSerializer,
    ContactMessageSerializer,
    EducationSerializer,
    ExperienceSerializer,
    ProjectSerializer,
)


class ApiRootView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        base_url = request.build_absolute_uri('/api/v1/')
        return Response(
            {
                'message': 'Portfolio backend API',
                'endpoints': {
                    'portfolio': f'{base_url}portfolio/',
                    'contact': f'{base_url}contact/',
                    'admin_messages': f'{base_url}admin/messages/',
                    'jwt_login': request.build_absolute_uri('/api/v1/auth/login/'),
                    'jwt_refresh': request.build_absolute_uri('/api/v1/auth/refresh/'),
                    'drf_login': request.build_absolute_uri('/api-auth/login/'),
                    'django_admin': request.build_absolute_uri('/admin/'),
                },
            }
        )


class PortfolioDataView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        about = About.objects.first()
        experiences = Experience.objects.prefetch_related('responsibilities')
        education = Education.objects.all()
        projects = Project.objects.prefetch_related('descriptions')
        skills = Skill.objects.all()
        languages = Language.objects.all()

        return Response(
            {
                'about': AboutSerializer(about).data if about else None,
                'experience': ExperienceSerializer(experiences, many=True).data,
                'education': EducationSerializer(education, many=True).data,
                'projects': ProjectSerializer(projects, many=True).data,
                'skills': [skill.name for skill in skills],
                'languages': [language.name for language in languages],
            }
        )


class ContactMessageView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {'message': 'Your message has been sent successfully!'},
            status=status.HTTP_201_CREATED,
        )


class AdminContactMessagesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        messages = ContactMessage.objects.all()
        serializer = ContactMessageSerializer(messages, many=True)
        return Response(serializer.data)
