from django.db import models

# Create your models here.
class Tasks(models.Model):
    task = models.CharField(max_length=500)

    def __str__(self):
        return self.task

    class Meta:
        verbose_name_plural = 'Tasks'

