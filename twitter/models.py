from django.db import models
from django.contrib.auth.models import User

TWITTER_MAXIMUM_TWEET_LENGTH = 280
TWITTER_MAXIMUM_COMMENT_LENGTH = 60


class Tweet(models.Model):
    content = models.CharField(max_length=TWITTER_MAXIMUM_TWEET_LENGTH)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '[{}] TWEET by {}: {}'.format(
            self.creation_date,
            self.author, self.content[:20])


class Comment(models.Model):
    content = models.CharField(max_length=TWITTER_MAXIMUM_COMMENT_LENGTH)
    date_comment = models.DateTimeField(auto_now_add=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
