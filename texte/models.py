from django.db import models

class CategorieTexte(models.Model):
    page        =    models.CharField(max_length=100, null=True)
    partie      =    models.CharField(max_length=100, null=True)
    designation =    models.CharField(max_length=300, null=True)

    def __str__(self):
        return '{0}/{1}'.format(self.page, self.partie)

class Texte(models.Model):
    titre       =    models.CharField(max_length=500, null=True)
    sous_titre  =    models.CharField(max_length=1000, null=True)
    para        =    models.TextField(null=True)
    categorie   =    models.ForeignKey(CategorieTexte, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.titre or self.sous_titre or self.para