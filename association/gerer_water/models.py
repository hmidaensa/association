from django.db import models

# Create your models here.
class Lieu(models.Model):
    lieu=models.CharField(max_length=50)
    
class Member(models.Model):
    nom=models.CharField(max_length=50)
    nom_arabic = models.CharField(max_length=50)
    num_counteur = models.CharField(max_length=50)
    num_maison = models.IntegerField()
    date_adhesion=models.DateField(auto_now=False, auto_now_add=False)
    date_resiliation = models.DateField(auto_now=False, auto_now_add=False)
    cin = models.CharField(max_length=12)
    lieu= models.ForeignKey(Lieu,on_delete=models.CASCADE)
    status= models.CharField(max_length=20)

class Sasion(models.Model):
    annne = models.IntegerField()

class Periode(models.Model):
    mois=models.IntegerField()
    saison=models.ForeignKey(Sasion,on_delete=models.CASCADE)

class Facture(models.Model):
        periode=models.ForeignKey(Periode,on_delete=models.CASCADE)
        membre= models.ForeignKey(Member, on_delete=models.CASCADE)
        mountant_default=models.IntegerField()
        mountant_consomme=models.IntegerField()
        total=models.IntegerField()
        old_counteur=models.IntegerField()
        new_counteur=models.IntegerField()
        factute_paye=models.IntegerField()

