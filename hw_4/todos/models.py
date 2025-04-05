from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.BooleanField(default=False)
    category=models.ForeignKey(Category, null=False, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
