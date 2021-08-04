from django.db import models

# Create your models here.
class Todo(models.Model):
    #anr = models.IntegerField(primary_key=True)
    add_date = models.DateTimeField(primary_key=True)
    text=models.CharField(max_length=200)
    #anr = models.IntegerField(primary_key=True)
    #anzahl = models.CharField(max_length=5)
    #bez = models.CharField(max_length=255)
    #preis = models.DecimalField(max_digits=7, decimal_places=2)
    #info = models.CharField(max_length=255)

    def __str__(self):
        return 'add_date: {}, text: {}'.format(self.add_date, self.text)
