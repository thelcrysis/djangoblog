from email.quoprimime import body_check
from multiprocessing import AuthenticationError
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def body_preview(self):
        body_words = self.body.split()

        # cutoff location is after the fiftieth word
        if len(body_words) < 50:
            return self.body
        else:
            cutoff_location = self.body.index(
                body_words[50]) + len(body_words[50])

            return self.body[:cutoff_location]
