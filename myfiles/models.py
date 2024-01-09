from django.db import models

# Create your models here.
class Subscribe(models.Model):
    ism = models.CharField(max_length=30)
    fam = models.CharField(max_length=30,null=True,blank=True)
    username = models.CharField(max_length=30,null=True,blank=True)
    tg_id = models.IntegerField(unique=True)

class Menu(models.Model):
    nomi = models.CharField(max_length=30)
    def __str__(self):
        return self.nomi

class Maxsulotlar(models.Model):
    nomi = models.CharField(max_length=30)
    rasm = models.CharField(max_length=300)
    malumot = models.TextField(null=True,blank=True)
    tur = models.ForeignKey(Menu,on_delete=models.CASCADE)

class Korzinka(models.Model):
    nomi = models.CharField(max_length=30)
    rasm = models.CharField(max_length=300)
    malumot = models.CharField(max_length=30, null=True, blank=True)
    tur = models.CharField(max_length=30)
    soni = models.IntegerField()
    username = models.CharField(max_length=30,null=True, blank=True)
