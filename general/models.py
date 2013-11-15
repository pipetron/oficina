from django.db import models

class Banner(models.Model):
    titulo = models.CharField(max_length=200)
    img_es = models.ImageField(upload_to="banner")
    #img_en = models.ImageField(upload_to="banner")
    activo = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.titulo

class SeccionPie(models.Model):
    titulo_es = models.CharField(max_length=20)
    #titulo_en = models.CharField(max_length=20)
    img_titulo = models.ImageField(upload_to="secciones",null=True,blank=True)
    descripcion_es = models.TextField()
    #descripcion_en = models.TextField()
    imagen = models.ImageField(upload_to="secciones")
    url = models.CharField(max_length=100)
    visible = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.titulo_es

class Contacto(models.Model):
    asunto = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    correo = models.EmailField()
    consulta = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return "Consulta de %s el %s" % (self.correo,self.fecha.strftime("%d/%m/%Y %H:%i"))
    
    
