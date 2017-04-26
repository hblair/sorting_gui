##ENSDF File: Multiple Data PLT (for gnuplot) File Extractor
##By: Markus Garbiso
##Date Updated: April 14, 2016

import dataClass_Hayden as dc
from haydenFirstAttempt import guioutputs_Hayden

##This function is used to bulk export a range of isotopes in a given A range.
def datExp(UI=False,Filter=False,elementName="H",lowerBound=0,higherBound=1,wantedSpins='',energyLim=100000000):
    ##User input and checks for valid inputs.
    tryAgainCounter=1
    elementName= str(guioutputs_Hayden.Z)
    lowerBound = int(guioutputs_Hayden.isoLow)
    higherBound = int(guioutputs_Hayden.isoUp)
    energyLim = int(guioutputs_Hayden.E)
    if(Filter):
        wantedSpins=str(guioutputs_Hayden.J)
        ##"""This loop goes through a selection of data files from the data folder"""
        energyLim=int(guioutputs_Hayden.E)
        
    if(type(lowerBound) is int and type(higherBound) is int and type(energyLim) is int):
            tryAgainCounter=0
    
    ##This loop goes through each wanted nuclei in the range of A values.
    for i in range(lowerBound,higherBound+1):
        itervar= str(i)+elementName 
        try:
            indata=dc.data('ensdf.'+str(i).zfill(3),itervar,'EoL',energyLim)
            if(Filter):
                indata.filterData(wantedSpins,UI) 
                indata.export("_Fil.dat",wantedSpins)
            else:
                indata.export(".dat")
        except:
            if(UI):
                ERROR="No file found for or error with " +'ensdf.'+str(i).zfill(3)##Allows the user to see if a specific ENSDF file is giving them trouble.
                print ERROR

   ##### #This loop makes the variable to be used (and iterated through) to from b in the a=b expression in the data class.
                
            
    if UI:
        #readinput.message= "Data export complete"
        exit
    
    ##If wanted this will return the user inputs for further use
    return [elementName,lowerBound,higherBound,wantedSpins]



       
##This function will create a plt file for use in gnuplot to plot data from a eiter filtered data files or the whoel data file. This function is
##best used if used will datExp.
def pltFileExp(elementName,lowerBound,higherBound,Filter=False,wantedSpins='',UI=False,fileParsingFactor=0):

    fileParsingFactorStr="_every_"+str(fileParsingFactor)

    if(Filter):##Program will ask the use if they only want to include only every other every single file or on and on.
        tryAgainCounter=1
        while(tryAgainCounter and UI):
            try:
                fileParsingFactor=int(1)
                fileParsingFactorStr="_every_"+str(fileParsingFactor)
                if(type(fileParsingFactor) is int):
                    tryAgainCounter=0
            except:
                print("Invalid Input")
    else:
        fileParsingFactor=1

    ##plt file Naming and this is different.
    if(Filter):
        fileName= "Output\\" + "gnuPlot\\"+str(lowerBound)+str(elementName)+"_"+str(higherBound)+str(elementName)+wantedSpins+fileParsingFactorStr+"_Fil.plt"        
        pltFile = open(fileName.replace('/', '_'),'wb')
    else:
        fileName="Output\\" + "gnuPlot\\"+str(lowerBound)+str(elementName)+"_"+str(higherBound)+str(elementName)+".plt"
        pltFile = open(fileName,'wb')


    ## These following lines add the completely nessecary lines in the plt files

    ##Reset gnuplot.
    pltFile.write("reset\n")

    ##This sets the x axis with the names of the isotpes wanted.
    setLine="set xtics ("
    for i in range(lowerBound,higherBound+1,fileParsingFactor):
        if(i+fileParsingFactor>higherBound):
            setLine=setLine+"\""+str(i)+str(elementName)+"\" "+str(i+1-lowerBound)+")"
        else:
            setLine=setLine+"\""+str(i)+str(elementName)+"\" "+str(i+1-lowerBound)+","
    pltFile.write(setLine+"\n")
    pltFile.write("set xrange [0:"+str(higherBound-lowerBound+2)+"]\n")

    ##This removes the default legend in the final plot, because the legend is ugly and not useful in our case.
    pltFile.write("unset key\n")

    ##This labels the y axis and the Title
    pltFile.write("set ylabel \"Energy(keV)\"\n")
    pltFile.write("set title \"Energy Levels\"\n")

    ##This line Currently DOES NOT work but should make the graph greyscale.
    pltFile.write("set palette gray\n")

    ##This tells gnuplot that the delimiter of each column as ,
    pltFile.write("set datafile sep ','\n")

    ##This will write the plot coding for the labeling of each energy leven and a line that corrosponds to each one.
    for i in range(lowerBound,higherBound+1,fileParsingFactor):
        if(i==lowerBound):
            if(Filter):
                pltFile.write(("plot \""+str(i)+str(elementName)+wantedSpins+"_Fil.dat\" using ("+str(i+1-lowerBound)+"):2:3 with labels point font \"Verdana,5\" offset character " + str(fileParsingFactor) + ",character 0\n").replace('/', '_'))
                pltFile.write(("replot \""+str(i)+str(elementName)+wantedSpins+"_Fil.dat\" using ("+str(i+1-lowerBound)+"):2:("+str(fileParsingFactor*0.5)+") with xerrorbars\n").replace('/', '_'))
            else:
                pltFile.write("plot \""+str(i)+str(elementName)+".dat\" using ("+str(i+1-lowerBound)+"):2:3 with labels point font \"Verdana,5\" offset character " + str(fileParsingFactor) + ",character 0\n")
                pltFile.write("replot \""+str(i)+str(elementName)+".dat\" using ("+str(i+1-lowerBound)+"):2:("+str(fileParsingFactor*0.5)+") with xerrorbars\n")
        else:
            if(Filter):
                pltFile.write(("replot \""+str(i)+str(elementName)+wantedSpins+"_Fil.dat\" using ("+str(i+1-lowerBound)+"):2:3 with labels point font \"Verdana,5\" offset character " + str(fileParsingFactor) + ",character 0\n").replace('/', '_'))
                pltFile.write(("replot \""+str(i)+str(elementName)+wantedSpins+"_Fil.dat\" using ("+str(i+1-lowerBound)+"):2:("+str(fileParsingFactor*0.5)+") with xerrorbars\n").replace('/', '_'))
            else:
                pltFile.write("replot \""+str(i)+str(elementName)+".dat\" using ("+str(i+1-lowerBound)+"):2:3 with labels point font \"Verdana,5\" offset character " + str(fileParsingFactor) + ",character 0\n")
                pltFile.write("replot \""+str(i)+str(elementName)+".dat\" using ("+str(i+1-lowerBound)+"):2:("+str(fileParsingFactor*0.5)+") with xerrorbars\n")
    if UI:
        print ("Program is finished plotting")
        exit
