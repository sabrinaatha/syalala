from django.db import models
from django.utils.text import slugify
from skills.models import Skills

class Project(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False
    )
    title = models.TextField()

    description = models.TextField(blank=True)

    image_url = models.URLField(blank=True)

    link = models.URLField(blank=True)

    type = models.TextField(blank=True)

    start_date = models.DateField(
        null=True,
        blank=True
    )

    end_date = models.DateField(
        null=True,
        blank=True
    )

    skills = models.ManyToManyField(
        Skills,
        through='MappingProjectsSkills'
    )

    class Meta:
        db_table = 'projects'
        managed = False

    def __str__(self):
        return self.title


class MappingProjectsSkills(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    skill = models.ForeignKey(
        Skills,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'mapping_projects_skills'
        managed = False

    def __str__(self):
        return f"{self.project} - {self.skill}"