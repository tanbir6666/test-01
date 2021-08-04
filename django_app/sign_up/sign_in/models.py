from django.db import models


# Create your models here.


class UserTable(models.Model):
    names = models.CharField(max_length=200)
    emails = models.CharField(max_length=400)
    passwords = models.CharField(max_length=200)


class DeleteUser(models.Model):
    names = models.CharField(max_length=200)
    emails = models.CharField(max_length=400)
    passwords = models.CharField(max_length=200)
