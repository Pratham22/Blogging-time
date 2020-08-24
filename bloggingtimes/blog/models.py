from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=100)
    thumnail_image=models.ImageField()
    main_img=models.ImageField(null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    passed_by_mentor=models.BooleanField(default=False)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})

class comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='coments')
    name=models.CharField(max_length=180)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    class Meta:
        ordering=['created_on']
    def __str__(self):
        return 'Comment {} by {}'.format(self.body,self.name)
    