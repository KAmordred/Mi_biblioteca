from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.titulo
