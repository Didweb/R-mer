#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  romanos.py
#
#  Copyright 2016 Eduard Pinuaga Linares <info@did-web.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


class RomaDeci():
	"""
	Clase para convertir números romanos a sistmea dicemal y de sistema
	decimal a romano.

	Erstellt Klasse Römer in Dezimalzahlen und Dezimalzahlen in
	römische System zu konvertieren.
	"""
	def __init__(self):
		"""
		Inicializamos y creamos diccionarios.
		Situamos el límite hasta donde la aplicación es capaz de
		calcular los números romanos. Que es hasta los 3999.

		Initialisieren und erstellen Wörterbücher.
		Wir legen die Grenze, auf die die Anwendung römischen Ziffern
		zu berechnen kann.
		Das ist, bis 3999.
		"""


		self.unidadesRomanas = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}



	def calculaR(self):
		"""
		Calculos  para convertir el número romano en entero.

		Berechnungen die gesamte römische Zahl zu konvertieren.
		"""
		resultadoR = 0

		for i in range(0,len(self.numeroR)):

			actual = self.unidadesRomanas[self.numeroR[i]]
			anterior = self.unidadesRomanas[self.numeroR[i-1]]
			if i==0:
				dante = actual
			elif actual > anterior:
				dante = (actual - anterior)-anterior
			else:
				dante = actual

			resultadoR = resultadoR + dante

		self.resultadoR = resultadoR

		return self.numerosoliR,self.resultadoR






	def erroresR(self,numeroR):
		"""
		Filtro para procesar los posibles errores y devolver un mensaje.
		Errores durante el proceso de Romano a entero.

		Filter Fehler zu verarbeiten und eine Nachricht zurück.
		Fehler, die bei Romano Ganzen.
		"""
		lis = list(numeroR)
		n_lis = len(lis)
		contador = 0
		tipo_error = ""
		marca = 0

		self.numeroR = list(numeroR)
		self.numero = 0
		self.numerosoli = numeroR
		self.txt=""

		for i in lis:
			if self.unidadesRomanas.get(i)==None:
				contador +=1
				tipo_error=" CARACTER NO ACEPTADO "

		if contador==0 and n_lis > 1:
			for x in range(0,n_lis):
				actual = self.unidadesRomanas[lis[x]]
				anterior = self.unidadesRomanas[lis[x-1]]


				"""
				Error de Dos a tras.
				"""
				if x>=2:
					dosAtras = self.unidadesRomanas[lis[x-2]]

				else:
					dosAtras = 10000


				"""
				Error de Dos a tras.
				"""
				if  x>0  and dosAtras!=None and actual > dosAtras  :
					contador=1
					tipo_error=" dosAtras MENOR "

				"""
				Error de 3 iguales a la derecha
				"""

				if  (x-3) >= 0  :

					if self.unidadesRomanas[lis[x-3]] == actual:
						contador=1
						tipo_error=" Cuatro iguales juntos no esta permitido "


		if contador>0:
			self.txt=" TIPO: "+tipo_error+" --> ERROR No es un número romano"
			self.apto = False
		else:

			self.numerosoliR = numeroR
			self.apto = True


		return self.numeroR,self.txt,self.apto









