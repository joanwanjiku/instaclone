from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.



class Post(models.Model):
    desc = models.TextField()
    image = models.ImageField(upload_to='post_pics', default='default.jpg')
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.desc

    @classmethod
    def get_all_posts(cls):
        return cls.objects.order_by('-date_posted')

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk}) 
    


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content

   
    
        