from django.db import models

# Create your models here.
class Topic(models.Model):
    title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')