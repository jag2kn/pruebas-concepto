#!/usr/bin/env python
# * coding: utf-8 *

from datetime import datetime 
from django.core.management import setup_environ

import settings
setup_environ(settings)

from servidor.models import Dato
from ConectorSerial import ConectorSerial


print("Leyendo mensajes del puerto serial:")
salir = False

c = ConectorSerial("/dev/ttyACM0")  # Camiar por el correspondiente en su maquina

while (not salir):
	# OJO en el archivo ConectorSerial.py se establece el protocolo a utilizar
	datos = c.solicitarDatos()

	d = Dato()
	d.mensaje = datos
	d.fecha = datetime.now()
	
	d.save()
	print ("Registro almacenado "+d)
