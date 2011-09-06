from django.db import models

# Create your models here.
class Dato(models.Model):
	mensaje = models.TextField()
	fecha = models.DateTimeField(blank=False, null=False)
	def __unicode__(self):
		return self.fecha+" - "+self.mensaje

