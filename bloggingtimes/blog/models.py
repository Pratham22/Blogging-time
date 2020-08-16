from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=100)
    thumnail_image=models.ImageField()
    main_img=models.ImageField(null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,related_name='author_of_the_blog', on_delete=models.CASCADE)
    ##Needs to be set
    #approvedBy = models.ForeignKey(User,related_name='approver_of_the_block',on_delete=models.CASCADE)
    #approved=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
'''
    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})
'''