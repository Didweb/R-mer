#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  consola.py
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

def clear():
    if os.name == "posix":
		os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
		os.system ("cls")



def bcolors(name):
	"""
	Colores para las salidas de consola.

	Farben für die Konsolenausgabe .
	"""
	colores = {
	'HEADER' : '\033[95m',
	'OKBLUE' : '\033[94m',
	'OKGREEN' : '\033[92m',
	'WARNING' : '\033[93m',
	'FAIL' : '\033[91m',
	'ENDC' : '\033[0m',
	'BOLD' : '\033[1m',
	'UNDERLINE' : '\033[4m'
	}

	return colores[name]


