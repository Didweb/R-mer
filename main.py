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

import pygtk
pygtk.require('2.0')
import gtk


class Entrada:
	def __init__(self):

		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_size_request(400, 300)
		window.set_title("Conversor numérico")
		window.connect("delete_event", lambda w,e: gtk.main_quit())


		vbox = gtk.VBox(False, 0)


		resultadoDR = gtk.Label("Pon Datos DR")
		resultadoRD = gtk.Label("Pon Datos RD")



		window.add(vbox)
		vbox.show()

		entryDR = gtk.Entry()
		entryDR.set_max_length(50)
		entryDR.connect("activate", self.EjecutarCalculo,entryDR,resultadoDR,"dr")
		entryDR.set_text("")
		entryDR.insert_text("", len(entryDR.get_text()))
		entryDR.select_region(0, len(entryDR.get_text()))

		entryRD = gtk.Entry()
		entryRD.set_max_length(50)
		entryRD.connect("activate", self.EjecutarCalculo,entryRD,resultadoRD,"rd")
		entryRD.set_text("")
		entryRD.insert_text("", len(entryRD.get_text()))
		entryRD.select_region(0, len(entryRD.get_text()))


		vbox.pack_start(resultadoDR, True, True, 0)
		vbox.pack_start(entryDR, True, True, 0)

		vbox.pack_start(resultadoRD, True, True, 0)
		vbox.pack_start(entryRD, True, True, 0)

		entryDR.show()
		resultadoDR.show()

		entryRD.show()
		resultadoRD.show()
		window.show()

	def EjecutarCalculo(self,widget,entry,resultado,tipo):

		entry_text = entry.get_text()
		text = ""
		if tipo == "dr":
			modoDR = DeciRoma()
			modoDR.errores(entry_text)


			if modoDR.apto == True:
				modoDR.calcula()
				texto = "El decimal =  {} es {} " . format(modoDR.numerosoli,modoDR.romano)
			else:
				texto = modoDR.txt



		elif tipo =="rd":
			modoRD = RomaDeci()
			modoRD.erroresR(entry_text.upper())


			if modoRD.apto == True:
				modoRD.calculaR()
				texto = "El romano =  {} es {} " . format(modoRD.numerosoliR,modoRD.resultadoR)
			else:
				texto = modoRD.txt



		resultado.set_text(texto)





def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    Entrada()
    main()
