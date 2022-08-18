from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    isAdmin = models.BooleanField()
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(null=True, blank=True)