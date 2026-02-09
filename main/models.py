from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    achievements = models.TextField()

    def __str__(self):
        return self.full_name