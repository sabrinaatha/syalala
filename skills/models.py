from django.db import models

# Create your models here.
class Skills(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False
    )
    skills_name = models.TextField()
    ability_level = models.TextField()
    type = models.TextField(blank=True)

    class Meta:
        db_table = 'skills'
        managed = False

    def __str__(self):
        return self.name
