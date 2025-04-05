from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.TextField()

    def __str__(self):
        return self.title
