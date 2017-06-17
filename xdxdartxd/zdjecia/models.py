from django.db import models

# Create your models here.

class Zdjecie(models.Model):
    tytul = models.CharField(max_length=200)
    szerokosc = models.IntegerField(default=0)
    wysokosc = models.IntegerField(default=0)
    obrazek = models.ImageField(null=False, blank=False, width_field="szerokosc", height_field="wysokosc")
    data = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.tytul

    class Meta:
        ordering = ["-data"]
