from django.db import models

# Create your models here.



class Post(models.Model):
    author = models.ForeignKey("auth.User")
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title
