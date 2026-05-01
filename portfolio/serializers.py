from rest_framework import serializers

from .models import (
    About,
    ContactMessage,
    Education,
    Experience,
    Language,
    Project,
    Skill,
)


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = [
            'name',
            'title',
            'address',
            'contact',
            'email',
            'github',
            'linkedin',
            'summary',
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    responsibilities = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = ['company', 'location', 'role', 'duration', 'responsibilities']

    def get_responsibilities(self, obj):
        return [responsibility.text for responsibility in obj.responsibilities.all()]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['institution', 'location', 'degree', 'duration']


class ProjectSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['name', 'description', 'url']

    def get_description(self, obj):
        return [description.text for description in obj.descriptions.all()]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name']


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'message', 'created_at', 'is_read']
        read_only_fields = ['id', 'created_at', 'is_read']
