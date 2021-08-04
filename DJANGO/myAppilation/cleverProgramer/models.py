from django.db import models


class UserDatabase(models.Model):
    RegTime = models.DateTimeField(auto_now=True)
    userName = models.CharField(max_length=300)
    userPassword = models.CharField(max_length=100)
    userAuthor = models.CharField(max_length=500)
    userEmail = models.CharField(max_length=300)


    def __str__(self):
        return '{}'.format(self.userName)

    class Meta:
        verbose_name_plural = 'USERS'


# Create your models here.
class SearchHistory(models.Model):
    searchUser = models.CharField(max_length=300)
    searchUrl = models.CharField(max_length=2000)
    searchTime = models.DateTimeField(auto_now=True)
    searchResultFound = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.searchUrl)

    class Meta:
        verbose_name_plural = 'SearchHistory'


class SearchData(models.Model):
    searchUrl = models.CharField(max_length=2000)
    searchData = models.CharField(max_length=500000)

    def __str__(self):
        return '{}'.format(self.searchUrl)

    class Meta:
        verbose_name_plural = 'SearchData'
