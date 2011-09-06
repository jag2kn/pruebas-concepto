# coding: utf-8
import os
import serial
import sys


class ConectorSerial:
	datos={}
	def __init__(self, Puerto = '/dev/ttyACM0' ):
		self.datos={}
		self.puerto = Puerto
		
	def solicitarDatos(self):
		s=None
		try:
			s = serial.Serial(self.puerto, 115200)
			#-- Timeout: 1 seg
			s.timeout=0.5;

		except serial.SerialException:
			#-- Error al abrir el puerto serie
			sys.stderr.write("Error al abrir puerto: " + str(self.puerto)+"\n")
			return {}

		print ("Puerto serie (%s): %s") % (str(self.puerto),s.portstr)
		
		#Protocolo
		s.write('1')
		
		#Cantidad elementos a procesar
		recibido = s.read(4)
		cantidad = ord(recibido[0])
		print "La cantidad de datos a procesar son: "+str(cantidad)

		
		s.write('2')
		
		for i in range(0, cantidad):
			recibido = s.read(15);
			print "Analizando "+str(i)+" = ["+str(recibido)+"]"
			print "\tC\tD\tH"
			cc=0
			self.datos[i]={}
			for c in recibido:
				print "\t"+c+"\t"+str(ord(c))+"\t"+str(hex(ord(c)))
				self.datos[i][cc]=hex(ord(c))
				cc+=1
		s.close()      
		return self.datos
