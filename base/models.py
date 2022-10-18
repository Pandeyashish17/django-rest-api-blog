from dataclasses import field
from django.db import models

# Create your models here.
class author(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField()

    def __str__(self) -> str:
        return self.name

class article(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField()
    author = models.ForeignKey(author,on_delete=models.CASCADE ,db_index=True)
    description=models.TextField()
    updatedAt=models.DateTimeField(auto_now=True)
    publishedAt=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title