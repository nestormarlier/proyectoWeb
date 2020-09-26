from django.db import models

# Create your models here.

class Categorias(models.Model):
    categoria_id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=False, null=False)

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


