from django.db import models


# Create your models here.
class Entry(models.Model):
    names = models.CharField(max_length=200)
    ages = models.IntegerField()
    gender = models.CharField(max_length=100)
    entryTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.names)

    class Meta:
        verbose_name_plural = 'ENTRY OF USERS'


class DeleteEntry(models.Model):
    entryID = models.IntegerField()
    names = models.CharField(max_length=200)
    ages = models.IntegerField()
    gender = models.CharField(max_length=100)
    createEntry = models.DateTimeField()
    entryTime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'DELETE ENTRY'

    def __str__(self):
        return '{}'.format(self.names)
