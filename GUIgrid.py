from Tkinter import *
import searching_function as sf
root = Tk()
root.title("Data Extraction Tool")


class Application(Frame):
#Setting up the variables so everything works properly        
    def __init__(self, master):
        """ Initialize the Frame """
        Frame.__init__(self,master)
        self.Zinput=StringVar()
        self.isoLowinput=StringVar()
        self.Jinput=StringVar()
        self.isoUpinput=StringVar()
        self.Einput=StringVar()
        self.Qlowinput=StringVar()
        self.Qhighinput=StringVar()
        self.Alowinput=StringVar()
        self.Ahighinput=StringVar()
        self.contentZ=self.Zinput 
        self.contentisoLow=self.isoLowinput
        self.contentJ=self.Jinput
        self.contentisoUp=self.isoUpinput
        self.contentE=self.Einput
        self.contentQlow=self.Qlowinput
        self.contentQhigh=self.Qhighinput
        self.contentAlow=self.Alowinput
        self.contentAhigh=self.Ahighinput

        self.create_widgets()
        self.grid()
        
    def create_widgets(self):
        """Creates Title in GUI"""
        self.instruction = Label(root, text = "Evaluated Nuclear Structure Extraction",bd=5)
        self.instruction.grid(row = 0, column =2, columnspan = 2)
        
        self.instruction = Label(root, text = "Decay Info",bd=5)
        self.instruction.grid(row = 0, column =6, columnspan = 1)

#Implements user input for Z (Chemical Symbol)        
        self.instructionZ = Label(root, text = "Chemical Symbol (ex. ZN)")#Command to make a title/text label 'A'
        self.instructionZ.grid(row = 1, column =0, columnspan = 1, sticky = W)#This tells us where the label "Z" goes
        self.Zinput = Entry(textvariable= self.Zinput,bd=5)#Command to make a user input box
        self.Zinput.grid(row = 2, column = 0, sticky = W)#This tells us where the user input box for "Z" goes
        
#Implements user input Lower bound isotope
        self.instructionisoLow = Label(root, text = "Lower bound isotope")#Command to make a title/text label 'isoLow'
        self.instructionisoLow.grid(row = 1, column =1, columnspan = 1, sticky = W) #This tells us where the label "Z" goes
        self.isoLowinput = Entry(textvariable= self.isoLowinput,bd=5)#Command to make a user input box
        self.isoLowinput.grid(row = 2, column = 1, sticky = W)#This tells us where the user input box for "Z" goes
        
#Implements user input for Upper bound isotope
        self.instructionisoUp = Label(root, text = "Upper bound isotope")#Command to make a title 'Energy Range'
        self.instructionisoUp.grid(row = 1, column =2, columnspan = 1, sticky = W) #This tells us where the label "Energy Range" goes
        self.isoUpinput = Entry(textvariable= self.isoUpinput,bd=5)#Command to make a user input box
        self.isoUpinput.grid(row = 2, column = 2, sticky = W)#This tells us where the user input box for "Energy Range" goes
        
#Implements user input for Spins
        self.instructionJ = Label(root, text = "J (ex. 0+,3/2-,etc...)")#Command to make a title 'Spin Range'
        self.instructionJ.grid(row = 3, column =0, columnspan = 1, sticky = W) #This tells us where the label "Spin Range" goes
        self.Jinput = Entry(textvariable= self.Jinput,bd=5)#Command to make a user input box
        self.Jinput.grid(row = 4, column =0, columnspan = 1, sticky = W) #This tells us where the label "Spin Range" goes

#Implements user input for Bound on Energy
        self.instructionE = Label(root, text = "Upper energy bound (keV)")#Command to make a title 'Spin Range'
        self.instructionE.grid(row = 3, column =1, columnspan = 1, sticky = W) #This tells us where the label "Spin Range" goes        
        self.Einput = Entry(textvariable= self.Einput,bd=5)#Command to make a user input box
        self.Einput.grid(row = 4, column =1, columnspan = 1, sticky = W) #This tells us where the label "Spin Range" goes


#Implements user input for Qlow
        self.instructionQlow = Label(root, text = "Qlow")#Command to make a title 'Spin Range'
        self.instructionQlow.grid(row = 1, column =5, columnspan = 1, sticky = W) #This tells us where the label "Spin Range" goes        
        self.Qlowinput = Entry(textvariable= self.Qlowinput,bd=5)#Command to make a user input box
        self.Qlowinput.grid(row = 2, column =5, columnspan = 1, sticky = W) #This tells us where the label "Spin Range" goes

#Implements user input for Qhigh
        self.instructionQhigh = Label(root, text = "Qhigh")#Command to make a title 'Spin Range'
        self.instructionQhigh.grid(row = 1, column =6, columnspan = 1, sticky = W) #This tells us where the label "Spin Range" goes        
        self.Qhighinput = Entry(textvariable= self.Qhighinput,bd=5)#Command to make a user input box
        self.Qhighinput.grid(row = 2, column =6, columnspan = 1, sticky = W) #This tells us where the label "Spin Range" goes

#Implements user input for Alow
        self.instructionAlow = Label(root, text = "Alow")#Command to make a title 'Spin Range'
        self.instructionAlow.grid(row = 3, column =5, columnspan = 1, sticky = W) #This tells us where the label "Spin Range" goes        
        self.Alowinput = Entry(textvariable= self.Alowinput,bd=5)#Command to make a user input box
        self.Alowinput.grid(row = 4, column =5, columnspan = 1, sticky = W) #This tells us where the label "Spin Range" goes

#Implements user input for Ahigh
        self.instructionAhigh = Label(root, text = "Ahigh")#Command to make a title 'Spin Range'
        self.instructionAhigh.grid(row = 3, column =6, columnspan = 1, sticky = W) #This tells us where the label "Spin Range" goes        
        self.Ahighinput = Entry(textvariable= self.Ahighinput,bd=5)#Command to make a user input box
        self.Ahighinput.grid(row = 4, column =6, columnspan = 1, sticky = W) #This tells us where the label "Spin Range" goes


#Implements submit button
        self.submit_button = Button(self, text ="Submit", command = self.readinput)#Makes a Submit button, ***problem here is the command (reveal) reads all user input boxes. So (see below) the only way to get it to output 'info pulled from website...' is to input 64Zn to all the boxes...need to figure out how to make it only read box by box and have 1 submit button for all those different commands
        self.submit_button.grid(row=5, column=0, columnspan= 5, sticky =W)#Tells us where to put the button in the GUI

#Implements submit button2 (for Hayden's part)
        self.submit_button2 = Button(self, text ="Submit2", command = self.interpret)#Makes a Submit button, ***problem here is the command (reveal) reads all user input boxes. So (see below) the only way to get it to output 'info pulled from website...' is to input 64Zn to all the boxes...need to figure out how to make it only read box by box and have 1 submit button for all those different commands
        self.submit_button2.grid_columnconfigure(0, weight=1)
        self.submit_button2.grid(row=5, column=5, columnspan= 5, sticky =E)#Tells us where to put the button in the GUI

#Implements text box
        self.text = Text(self, width= 12, height= 10, wrap = WORD)#Makes the output text box
        self.text.grid_columnconfigure(0, weight=1)
        self.text.grid(row=6, column=1, columnspan=1, sticky= E+W+N+S)

#Implements text box2
        #self.text2 = Text(self, width= 15, height= 5, wrap = WORD)#Makes the output text box
        #self.text2.grid_columnconfigure(5, weight=1)
        #self.text2.grid(row=6, column=5, columnspan=1, sticky= E+W+N+S)


        
#All the above is python trickery and organization for the window, the readinput function below stores the userinput as contentA, contentZ, etc...
    def readinput(self):
        """Stores user input as local variables"""
        self.contentZ= self.Zinput.get()
        self.contentisoLow= self.isoLowinput.get()
        self.contentJ= self.Jinput.get()
        self.contentisoUp= self.isoUpinput.get()
        self.contentE=self.Einput.get()
        root.destroy()#closes the GUI window

#The interpret function reads the user input for Hayden's part and feeds those values into the acquire function
    def interpret(self):
        self.contentQhigh=self.Qhighinput.get()
        self.contentAlow=self.Alowinput.get()
        self.contentAhigh=self.Ahighinput.get()
        self.contentQlow=self.Qlowinput.get()

        if(self.contentQlow==True, self.contentQhigh== True, self.contentAlow== True, self.contentAhigh==True): #current condition is there must be a value in each user input box...
            message= '{}'.format(sf.acquire(Theory=False, Q_low=int(self.contentQlow), Q_high=int(self.contentQhigh), A_low=int(self.contentAlow), A_high=int(self.contentAhigh), Sym=False))
#This if statement puts the output of the searching function in the text box**** Current problem is it returns an empty pdat, isn't appending the list

        self.text.delete(0.0, END) #This deletes and the words in the box if the button is clicked a second time
        self.text.insert(0.0, message)#And this writes the new words in the box if it's clicked a second time
        
           
       
app = Application(root)
root.geometry("1500x900")
root.mainloop()


class guioutputs: #This class contains the outputs (stored user input values) and is what we feed into the main script
    Z=app.contentZ
    isoLow=app.contentisoLow
    J=app.contentJ
    isoUp=app.contentisoUp
    E=app.contentE
    Qlow= app.contentQlow
    Qhigh= app.contentQhigh
    Alow= app.contentAlow
    Ahigh= app.contentAhigh

