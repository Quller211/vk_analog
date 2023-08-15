from django.db import models

class Login(models.Model):
    user_login = models.CharField(max_length = 100)

    def __str__(self):
        return self.user_login


class MainPage(models.Model):
    login_in = models.ForeignKey(Login, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    date_of_birth = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class News(models.Model):
    topic_news = models.CharField(max_length = 150)
    post_news = models.TextField()
    topic_images = models.ImageField(upload_to = 'images/')
    posted_by = models.ForeignKey(Login, on_delete = models.CASCADE)
    posted_time = models.DateField(auto_now = True)
    posted = models.BooleanField(null = True)

    def __str__(self):
        return self.topic_news