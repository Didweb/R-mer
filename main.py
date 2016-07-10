#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
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


from logica.deci_roma import DeciRoma
from logica.roma_deci import RomaDeci

from tics.consola import clear



clear()
deciRoma = DeciRoma()
romaDeci = RomaDeci()


def menu():
	"""
	Creación del menú.

	Menü-Erstellung.
	"""
	print "---------MENÚ-------------"
	print "\t1 - Decimal >> Romano "
	print "\t2 - Romano >> Decimal  "
	print "\t9 - Salir "

menu()
while True:
	""" Ciclo por dnde hacemos correr el menú y las distintas opciones.

	Zyklus, in dem wir das Menü und die verschiedenen Optionen laufen. """
	opcionMenu = raw_input("Inserta opción del menú >> ")

	if opcionMenu=="1":
		print ""
		deciRoma.insertar()
		clear()

		deciRoma.errores(deciRoma.numerosoli)
		if deciRoma.apto == False:
			deciRoma.mensa(deciRoma.txt,deciRoma.numerosoli)
			menu()
			deciRoma.insertar()
			clear()
			deciRoma.errores(deciRoma.numerosoli)
		else:
			deciRoma.calcula()
			deciRoma.pintarResultado('d',deciRoma.numerosoli,deciRoma.romano)
			menu()

	elif opcionMenu=="2":
		print ""
		romaDeci.insertarR()
		clear()
		romaDeci.calculaR()
		menu()

	elif opcionMenu=="9":
		break

	else:
		clear()
		print "No has pulsado una opción correcta..."
		menu()


