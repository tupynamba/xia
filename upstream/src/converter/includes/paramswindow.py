#! /usr/bin/python
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
# @author : pascal.fautrero@ac-versailles.fr

import Tkinter
import tkFileDialog
from tooltip import ToolTip

import gettext
import locale
try:
    t = gettext.translation("messages", "i18n", languages=[locale.getdefaultlocale()[0]])
except:
    t = gettext.translation("messages", "i18n", languages=['en'])
translate = t.ugettext

class IAParams(Tkinter.Frame):

    def __init__(self, root, parent, localdir="."):

        Tkinter.Frame.__init__(self, root)

        self.root = root
        self.localdir = localdir
        self.parent = parent
        self.resizeCoeff = parent.resize
        
        # define images
        self.resize_img = {}
        self.resize_img[0]= Tkinter.PhotoImage(file=self.localdir + \
            "/images/resize1.gif")            
        self.resize_img[1]= Tkinter.PhotoImage(file=self.localdir + \
            "/images/resize2.gif")            
        self.resize_img[2]= Tkinter.PhotoImage(file=self.localdir + \
            "/images/resize3.gif")            
        self.resize_img[3]= Tkinter.PhotoImage(file=self.localdir + \
            "/images/resize4.gif")            
            
        params_img= Tkinter.PhotoImage(file=self.localdir + \
            "/images/params2.gif")            

        # define buttons

        self.button_resize = Tkinter.Button(self, \
          image=self.resize_img[self.resizeCoeff % 4], \
          relief=Tkinter.FLAT, bd=0, height=150, width=150, \
          command=self.resize)
        self.button_resize.image = self.resize_img[self.resizeCoeff % 4]
        self.button_resize.grid(row=0,column=0, columnspan=1,sticky='W')
        tooltip2 = ToolTip(self.button_resize,translate("modify image resolution"), None, 0.1)

        

        # title

        label = Tkinter.Label(self, image=params_img)
        label.photo = params_img
        label.grid(row=1,column=0,columnspan=2, sticky='W')

    def resize(self):
        self.resizeCoeff = (self.resizeCoeff + 1) % 4
        self.parent.resize = self.resizeCoeff
        self.button_resize.configure(image=self.resize_img[self.resizeCoeff])
    def quit(self):
        self.root.destroy()
