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

from tics.consola import clear

from salidas import salida


class DeciRoma(salida):
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
		calcular los números romanos. Que es hasta los 9000.

		Initialisieren und erstellen Wörterbücher.
		Wir legen die Grenze, auf die die Anwendung römischen Ziffern
		zu berechnen kann.
		Das ist, bis 9000.
		"""
		unidades = {0:'',1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}
		decenas = {0:'',1:'X',2:'XX',3:'XXX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC'}
		centenas = {0:'',1:'C',2:'CC',3:'CC',4:'CD',5:'D',6:'DC',7:'DCC',8:'DCCC',9:'CM'}
		millares = {0:'',1:'M',2:'MM',3:'MMM',4:'ÏÜ',5:'Ü',6:'ÜÏ',7:'ÜÏÏ',8:'ÜÏÏÏ',9:'ÏẌ'}
		self.eco = unidades,decenas,centenas,millares


		self.limite = 9000


	def insertar(self):
		"""
		Entrada  del número entero.

		Integer-Eingang.
		"""
		numero = raw_input("Introduce un número para convertirlo en romano: ")
		self.errores(numero)




	def calcula(self):
		"""
		Calculos para convertir el número entero en número romano.

		Die Berechnungen, die ganze Zahl in eine römische Zahl zu konvertieren.
		"""
		volteamos = self.numero[::-1]

		resultado = []
		for i in range(0,len(volteamos)):
			resultado.append(self.eco[i][int(volteamos[i])])

		crim = resultado[::-1]
		self.romano = "".join(crim)

		return self.numerosoli,self.romano





	def errores(self,n):
		"""
		Filtro para procesar los posibles errores y devolver un mensaje.
		Errores durante el proceso de entero a Romano.

		Filter Fehler zu verarbeiten und eine Nachricht zurück.
		Fehler, die während der gesamten Romano.
		"""
		self.numero = 0
		self.numerosoli = n
		self.txt=""
		if n.isdigit()== False:
			self.txt = " NO es un número. debe introducir un número."
			self.apto = False
		elif int(n) > self.limite :
			self.txt = "No podemos calcular números superiores a "+str(self.limite)
			self.apto = False
		else:
			self.numero = list(n)
			self.numerosoli = n
			self.apto = True


		return n,self.numero,self.txt,self.apto










