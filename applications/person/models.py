from django.db import models
from applications.department.models import Department
from ckeditor.fields import RichTextField

# Create your models here.

class Ability(models.Model):
    ability = models.CharField('Ability', max_length=50)

    class Meta:
        verbose_name_plural = 'Abilities'

    def __str__(self):
        return self.ability

class Employee(models.Model):

    JOB_CHOICES = (
        ('0', 'Finances'),
        ('1', 'Admin'),
        ('2', 'Developer'),
        ('3', 'Other'),
    )

    name = models.CharField('Name', max_length=20, default='')
    last_name = models.CharField('Last name', max_length=20, default='')
    position = models.CharField('Position', max_length=20, default='', choices=JOB_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default='')
    anulate = models.BooleanField('Anulate', default=False)
    ability = models.ManyToManyField(Ability)
    full_name = models.CharField('Full Name', max_length=20, blank=True) #Podemos comentar lo del admin
    avatar = models.ImageField(upload_to='Employee', blank=True, null=True)
    life_sheet = RichTextField()

    class Meta:
        ordering = ['last_name', 'name']
        verbose_name_plural = 'My employee'
        verbose_name_plural = 'Company employee'

    

    def __str__(self):
        return str(self.id) + ' - ' + self.last_name + ' - ' + self.name + ' - ' + str(self.department)