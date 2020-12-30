from django.db import models

# Create your models here.
class BlogPost(models.Model):
    author=models.CharField(max_length=50)
    complete=models.BooleanField(default=True)
    article_field=models.TextField()
    def __str__(self):
        return self.author
