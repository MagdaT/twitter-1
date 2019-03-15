from django.db import models
from django.contrib.auth.models import User

TWITTER_MAXIMUM_TWEET_LENGTH = 280


class Tweet(models.Model):
    content = models.CharField(max_length=TWITTER_MAXIMUM_TWEET_LENGTH)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.creation_date}] ' \
               f'TWEET by {self.author}: {self.content[:20]}'
