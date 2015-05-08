import datetime
import threading
import Queue
import time
import random


class ImplementadoLoggerHilo(threading.Thread):

	colaMensajes = None
	terminar = False
	f = None
	
	def __init__(self):
		threading.Thread.__init__(self)
		self.colaMensajes = Queue.Queue()
		self.terminar = False
		self.f = open('archivo.log', 'w')
		print ("Inicio\tLogger")

	def escribir(self,mensaje):
		self.f.write(mensaje+"\n")

	def run(self):
		while not (self.terminar and self.colaMensajes.empty()):
			mensajeActual = self.colaMensajes.get()
			self.escribir(mensajeActual)
			if not self.terminar:
				time.sleep(4)

		print ("Fin\tLogger")


	def registrar(self, mensaje):
		self.colaMensajes.put(mensaje)


class ProcesosHilo(threading.Thread):
	logger = None
	nombre = ""
	def __init__(self, n, l):
		self.nombre = n
		self.logger = l
		threading.Thread.__init__(self)
		print ("Inicio\t"+self.nombre)

	def run(self):
		for i in range(10):
			time.sleep(random.random()*0.5)
			date = datetime.datetime.now()
			msg = "["+str(date)+"]\t"+self.nombre+" mensaje "+str(i)
			self.logger.registrar(msg)
		print ("Fin\t"+self.nombre)







l = ImplementadoLoggerHilo()
l.start()

listaP = []


print ("\tLanzando procesos.")
for i in range(10):
	p = ProcesosHilo("Proceso "+str(i), l)
	p.start()
	listaP.append(p)

print ("\tProcesos lanzados, esperando terminar hilos.")


time.sleep(2)
l.terminar = True
l.join()
for p in listaP:
	p.join()

print ("\tHilo principal terminado.\n")













