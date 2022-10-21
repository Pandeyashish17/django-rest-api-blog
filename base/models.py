from django.db import models

# Create your models here.
class author(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField()

    def __str__(self) -> str:
        return self.name

class categories(models.Model):
    categoryName = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.categoryName


class tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.tag

class article(models.Model):
    imagetitle=models.CharField(max_length=80,null=True)
    title=models.CharField(max_length=100,)
    excerpt = models.CharField(max_length=200,null=True)
    author = models.ForeignKey(author,on_delete=models.CASCADE ,db_index=True)
    authorimage = models.ImageField(null=True)
    image = models.ImageField(null=True,blank=True)
    tags = models.ManyToManyField(tag)
    category = models.ForeignKey(categories,on_delete=models.CASCADE ,db_index=True,null=True)
    description=models.TextField()
    updatedAt=models.DateTimeField(auto_now=True)
    publishedAt=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title} - {self.category}"