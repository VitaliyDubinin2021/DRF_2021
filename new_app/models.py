from django.db import models

from users.models import User


class Project(models.Model):

    name = models.CharField(max_length=256, unique=True)
    url_repository = models.URLField(blank=True)
    users = models.ManyToManyField(User)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.name}'


class ToDo(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at_time = models.DateField(auto_now_add=True)
    updated_at_time = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['pk']