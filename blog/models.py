from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=100)


class Post(models.Model):
    subject = models.ForeignKey(Subject)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    date_added = models.DateTimeField('date added')

