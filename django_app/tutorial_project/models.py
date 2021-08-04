from django.db import models


# Create your models here.

class show_it(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    roll = models.IntegerField()


class text_massage(models.Model):
    NAME = models.CharField(max_length=200)
    MASSAGE = models.CharField(max_length=10000)


class LinkElements(models.Model):
    links = models.CharField(max_length=999999999)