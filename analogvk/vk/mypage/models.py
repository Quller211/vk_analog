from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    topic_news = models.CharField(max_length = 150)
    post_news = models.TextField()
    topic_images = models.ImageField(upload_to = 'images/')
    posted_by = models.ForeignKey(User, on_delete = models.CASCADE)
    posted_time = models.DateField(auto_now = True)
    posted = models.BooleanField(null = True)

    def __str__(self):
        return self.topic_news
    
class UserDescripe(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.user