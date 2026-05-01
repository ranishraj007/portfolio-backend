from django.db import models


class About(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    github = models.URLField()
    linkedin = models.URLField()
    summary = models.TextField()

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.role} at {self.company}'


class Responsibility(models.Model):
    experience = models.ForeignKey(
        Experience,
        related_name='responsibilities',
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.text[:60]


class Education(models.Model):
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.degree} - {self.institution}'


class Project(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.name


class ProjectDescription(models.Model):
    project = models.ForeignKey(
        Project,
        related_name='descriptions',
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.text[:60]


class Skill(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Message from {self.name} ({self.email})'
