from django.db import models


class GetInTouch(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=255)
    email_address = models.EmailField()
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField(blank=True)

    class Meta:
        db_table = 'get_in_touch'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} <{self.email_address}>"