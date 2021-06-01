from django.db import models

# Create your models here.

CHOICES = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
]
class Tasks(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(choices=CHOICES, max_length=10)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Tasks'

