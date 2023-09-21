from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Creation of the Posts table/schema
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE) # Author is a foriegn key
    # You also need to run makemigrations and migrate
    # Then you add the dunder str method for more descriptive answer
    def __str__(self):
        return self.title   

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

