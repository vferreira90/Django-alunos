from django.db import models

class Aluno(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    birthday = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    registration_number = models.CharField(max_length=20, unique=True)
    crated_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name