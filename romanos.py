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

import os

class romanos():

	def __init__(self):
		unidades = {0:'',1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}
		decenas = {0:'',1:'X',2:'XX',3:'XXX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC'}
		centenas = {0:'',1:'C',2:'CC',3:'CC',4:'CD',5:'D',6:'DC',7:'DCC',8:'DCCC',9:'CM'}
		millares = {0:'',1:'M',2:'MM',3:'MMM'}
		self.eco = unidades,decenas,centenas,millares

		self.unidadesRomanas = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

		self.bcolors()
		self.limite = 3999


	def insertar(self):

		numero = raw_input("Introduce un número para convertirlo en romano: ")
		self.errores(numero)



	def insertarR(self):

		numeroR = raw_input("Introduce un número Romano: ")
		self.erroresR(numeroR.upper())


	def calculaR(self):

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
		print "El número romano  ",self.numerosoliR," es el ",resultadoR," en decimal."
		print "---------------------------------------------"



	def calcula(self):

		volteamos = self.numero[::-1]

		resultado = []
		for i in range(0,len(volteamos)):
			#print "posicion: ",i," = ",volteamos[i]," en romano= ",self.eco[i][int(volteamos[i])]
			resultado.append(self.eco[i][int(volteamos[i])])

		crim = resultado[::-1]
		romano = "".join(crim)

		print self.OKBLUE+"El número ",self.numerosoli," en Romano es = "+ self.ENDC+self.BOLD+romano+ self.ENDC
		print self.OKBLUE+"---------------------------------------------"+ self.ENDC




	def erroresR(self,numeroR):

		lis = list(numeroR)
		n_lis = len(lis)
		contador = 0
		tipo_error = ""
		marca = 0

		for i in lis:
			if self.unidadesRomanas.get(i)==None:
				contador +=1
				tipo_error=" CARACTER NO ACEPTADO "

		if contador==0 and n_lis > 1:
			for x in range(0,n_lis):
				actual = self.unidadesRomanas[lis[x]]
				anterior = self.unidadesRomanas[lis[x-1]]
				if x>=2:
					dosAtras = self.unidadesRomanas[lis[x-2]]
				else:
					dosAtras = 10000

				print "KEY = ",dosAtras
				print "(actual)",self.unidadesRomanas.get(x),"-",actual," > (dosAtras)",self.unidadesRomanas.get(x-2),"-",dosAtras,"  --  and ",x,">0 )"


				if  x>0  and dosAtras!=None and actual > dosAtras  :
					contador=1
					tipo_error=" dosAtras MENOR "
					print "<<<----ERROR ",dosAtras



		if contador>0:
			self.mensa(" TIPO: "+tipo_error+" --> ERROR No es un número romano", numeroR)
			self.insertarR()
		else:
			self.numeroR = list(numeroR)
			self.numerosoliR = numeroR





	def errores(self,n):

		if n.isdigit()== False:
			self.mensa(" NO es un número. debe introducir un número.",n)
			self.insertar()

		elif int(n) > 3999:
			self.mensa("No podemos calcular núemros superiores a 3999")
			self.insertar()

		else:
			self.numero = list(n)
			self.numerosoli = n



	def mensa(self,txt,n=""):
		#os.system('clear')
		print self.FAIL+"---------------------------------------------"
		print n+txt
		print "---------------------------------------------\n"+ self.ENDC
		self.numero = 0



	def menu(self):
		print "---------MENÚ-------------"
		print "\t1 - Decimal a Romano"
		print "\t2 - Romano a Decimal"
		print "\t9 - salir"



	def bcolors(self):
		self.HEADER = '\033[95m'
		self.OKBLUE = '\033[94m'
		self.OKGREEN = '\033[92m'
		self.WARNING = '\033[93m'
		self.FAIL = '\033[91m'
		self.ENDC = '\033[0m'
		self.BOLD = '\033[1m'
		self.UNDERLINE = '\033[4m'

os.system('clear')
a = romanos()
a.menu()

while True:

	opcionMenu = raw_input("Inserta opción del menú >> ")

	if opcionMenu=="1":
		print ""
		a.insertar()
		os.system('clear')
		a.calcula()
		a.menu()

	elif opcionMenu=="2":
		print ""
		a.insertarR()
		os.system('clear')
		a.calculaR()
		a.menu()

	elif opcionMenu=="9":
		break

	else:
		a.mensa("No has pulsado una opción correcta...")
		a.menu()

