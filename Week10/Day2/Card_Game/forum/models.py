from django.db import models
from django.contrib.auth.models import User


class Thread(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    headline = models.CharField(max_length=30,null=True)
    subject = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline


class Comment(models.Model):
    text = models.CharField(max_length=100)
    thread_id = models.ForeignKey(Thread,on_delete=models.CASCADE, related_name='comment')
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='new_thread')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date