from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

def create_default_summary(body):
    return '.'.join(body.split('.')[:2]) + '.'

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('blog')

class Post(models.Model):
    title = models.CharField(max_length=255)
    tags = models.CharField(max_length=255) #, default="Algo Trading & Investment Blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True)
    #body = models.TextField()
    summary = models.TextField(blank=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='Investing')

    def save(self, *args, **kwargs):
            if not self.summary:
                self.summary = create_default_summary(str(self.body))
            super().save(*args, **kwargs)

    # formatting for admin session
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('blog')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments" ,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)