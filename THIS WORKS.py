# -*- coding: utf-8 -*-
import dataClass as dc
import isotopeDataExportingDat as ided
from data_array import final
from searching_function import acquire
from GUIgrid import guioutputs


#Exports data necessary for plot to be made
userInput = ided.datExp(True,True)

#Makes plot
ided.pltFileExp(userInput[0],userInput[1],userInput[2],True,userInput[3],True)

#The section of code that implements Hayden's part into the GUI is in the GUIgrid python script (at the end)








#Problems:
#1. In order for the submit button to do anything the GUI has to close
#2. Formatting....... 
#4. Want 'warning' messages to appear in textbox
#5. Plots do NOT appear inside GUI
#6. Only uses data from Marcus' program, need to expand to all the data
#7. How to handle Theory and Sym inputs
