#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  testDeciRoma.py
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

import unittest, os, sys
sys.path.append(os.path.abspath('..'))

from logica.deci_roma import DeciRoma



class tester (unittest.TestCase):
    def test_1(self):

		a = DeciRoma()
		resultado = a.limite

		self.assertEqual(9000, resultado)

    def test_2(self):

		a = DeciRoma()
		resultado = a.limite

		self.assertNotEqual(1, resultado)

    def test_3(self):

		a = DeciRoma()
		resultado = a.errores('a')

		self.assertFalse(resultado)

if __name__ == "__main__":
    unittest.main()

