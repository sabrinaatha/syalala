from django.db import models
from django.utils.text import slugify

from projects.models import Skills

class Works(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    title = models.TextField()
    document_link = models.URLField(blank=True)
    image_link = models.URLField(blank=True)
    type = models.TextField(blank=True)
    company_name = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    company_url = models.URLField(blank=True)
    location = models.TextField(blank=True)
    employement_type = models.TextField(blank=True)
    is_current = models.BooleanField(default=False)

    skills = models.ManyToManyField(
        Skills,
        through='MappingWorkskills'
    )
    
    class Meta:
        db_table = 'works'
        managed = True

    def __str__(self):
        return self.title

class MappingWorkskills(models.Model):
    work = models.ForeignKey(Works, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)

    class Meta:
        db_table = 'mapping_works_skills'
        managed = False

    def __str__(self):
        return f"{self.work} - {self.skill}"
    
class ProjectsUnderWorks(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    work = models.ForeignKey(Works, on_delete=models.CASCADE)
    title = models.TextField()
    detail = models.TextField()
    type = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'projects_under_works'
        managed = False

    def __str__(self):
        return self.title