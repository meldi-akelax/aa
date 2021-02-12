from django.db import models

# Create your models here.
from django.db import models

class Section(models.Model):
    page        =    models.CharField(max_length=100, null=True)
    titre       =    models.CharField(max_length=100, null=True)
    description =    models.CharField(max_length=300, null=True)

    def __str__(self):
        return '{0}/{1}'.format(self.page, self.titre)

class Texte(models.Model):
    titre       =    models.CharField(max_length=500, null=True)
    para        =    models.TextField(null=True)
    section     =    models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return '{0}/{1}/{2}'.format(self.section.page, self.section.titre,self.titre or self.para) 

class Image(models.Model):
    section     =    models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    image       =    models.ImageField('')
    description =    models.TextField(null=True)
    
    def __str__(self):
        return '{0}/{1}/{2}'.format(self.section.page,self.section.titre, self.description) 