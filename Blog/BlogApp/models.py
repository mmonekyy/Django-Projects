from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='images/',default=None)
    add_time = models.DateTimeField(auto_now_add=True)
    key_words = models.JSONField(default=list)