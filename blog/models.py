from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField('date added')

    def __str__(self):
        return self.title


class Post(models.Model):
    topic = models.ForeignKey(Topic)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    date_added = models.DateTimeField('date added')
    votes = models.IntegerField()

    def __str__(self):
        return self.title
