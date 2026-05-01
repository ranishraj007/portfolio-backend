from django.contrib import admin

from .models import (
    About,
    ContactMessage,
    Education,
    Experience,
    Language,
    Project,
    ProjectDescription,
    Responsibility,
    Skill,
)


class ResponsibilityInline(admin.TabularInline):
    model = Responsibility
    extra = 1


class ProjectDescriptionInline(admin.TabularInline):
    model = ProjectDescription
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['role', 'company', 'duration', 'order']
    list_editable = ['order']
    inlines = [ResponsibilityInline]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'duration', 'order']
    list_editable = ['order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'order']
    list_editable = ['order']
    inlines = [ProjectDescriptionInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['created_at']
