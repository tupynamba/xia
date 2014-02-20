#!/usr/bin/python
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#   
# @author : pascal.fautrero@crdp.ac-versailles.fr

import os
from lib.iaobject import iaObject

#currentDir = os.path.dirname(os.path.realpath(__file__))

imageActive = iaObject()
imageActive.analyzeSVG("fixtures/test.svg")
imageActive.generateJSON("images_actives/datas/data.js")
imageActive.generateAccordion("images_actives/index.html")
imageActive.createBackground("images_actives/datas")