from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title + ' - ' + self.subtitle + ' - ' + str(self.quantity)
