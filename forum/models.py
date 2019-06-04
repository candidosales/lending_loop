from django.db import models

# Create your models here.
class Topic(models.Model):
    title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.title_text

class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.comment_text