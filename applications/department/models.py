from django.db import models

# Create your models here.

class Department(models.Model):
    name_deparment = models.CharField('Name', max_length=20, default='')
    short_name = models.CharField('Short name', max_length=20, default='')
    anulate = models.BooleanField('Anulate', default=False)

    def __str__(self):
        return self.name_deparment+ ' - '+self.short_name
    
    class Meta:
        ordering = ['-name_deparment']
        verbose_name_plural = 'Department'