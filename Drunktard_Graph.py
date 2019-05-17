# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:43:27 2019

@author: thewolvenfire 
import sys
import qdarkstyle
from PySide import QtGui

# create the application and the main window
app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()

# setup stylesheet
app.setStyleSheet(qdarkstyle.load_stylesheet_pyside())

# run
window.show()
app.exec_()