from django.db import models

class Documento(models.Model):
    titulo = models.CharField(max_length=300)
    archivo = models.FileField(upload_to="docs")
    visible = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.titulo