#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  salidas.py
#

from tics.consola import clear,bcolors

class salida():

	def mensa(self,txt,n=""):
		"""
		Procesando mensajes de error.

		Die Verarbeitung Fehlermeldungen .
		"""
		clear()
		print bcolors('FAIL')+"---------------------------------------------"
		print n + txt
		print "---------------------------------------------\n"+ bcolors('ENDC')
		self.numero = 0



	def pintarResultado(self,opcion,numConsultado,numResultado):
		"""
		Mostrar el resultado.

		Show
		"""
		texto_cap = ""
		if opcion == 'r':
			texto_cap = "El número Romano  {} en sistema decimal es : {}".format(numConsultado,numResultado)
		elif opcion == 'd':
			texto_cap = "El número en sistema decimal {}   en Romano es :  {}" .format(numConsultado,numResultado)



		print bcolors('OKBLUE') +"\n"+texto_cap
		print "---------------------------------------------\n"+ bcolors('ENDC')



