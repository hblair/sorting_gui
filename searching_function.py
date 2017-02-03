# -*- coding: utf-8 -*-
"""
Hayden Blair
Electro Weak Interactions Group

Searching Function
"""

from data_array import final

def acquire(Theory=False,Q_low=False,Q_high=False,A_low=False,A_high=False,Sym=False):
    '''
    This is going to be the complete searching function that will take
    in user inputs from the GUI, and return the desired values from the 
    data array.
    '''
    pdat = []
    if Theory == False:
        for i in final:
            if len(i) == 14:
                pdat.append(i)
    elif Theory == True:
        for i in final:
            if len(i) == 15:
                del(i[14])
                pdat.append(i)
            else:
                pdat.append(i)
    '''
    Creates a psuedo array that can contain the theoretical values if the user wants them
    The rest of the function then removes all of the different nucleons that do not
    satisfy the user's specifications
    '''

    '''
    This next section uses each one of the user specifications to search through the'
    database, and flags each one of the rows that does not match the desired parameters.
    Once the proper entries have all been flagged, they will be removed before the pseudo
    array is returned to the user.
    '''


#Q value range
    if Q_high == False and Q_low == False:
        pass
    elif Q_high == False and Q_low != False:
        for i in range(0,len(pdat)):
            if float(pdat[i][5]) < Q_low:
                pdat[i].append('r')
    elif Q_high!= False and Q_low == False:
        for i in range(0,len(pdat)):
            if float(pdat[i][5]) > Q_high:
                pdat[i].append('r')
    elif Q_high != False and Q_low != False:
        for i in range(0,len(pdat)):
            if float(pdat[i][5]) < Q_low or float(pdat[i][5]) > Q_high:
                pdat[i].append('r')

#Nucleon range                
    if A_high == False and A_low == False:
        pass
    elif A_high == False and A_low != False:
        for i in range(0,len(pdat)):
            if eval(pdat[i][3]) < A_low:
                pdat[i].append('r')
    elif A_high!= False and A_low == False:
        for i in range(0,len(pdat)):
            if eval(pdat[i][3]) > A_high:
                pdat[i].append('r')
    elif A_high != False and A_low != False:
        for i in range(0,len(pdat)):
            if eval(pdat[i][3]) < A_low or eval(pdat[i][3]) > A_high:
                pdat[i].append('r')

#Chemical Symbol
    if Sym == False:
        pass
    elif Sym != False:
        for i in range(0,len(pdat)):
            if pdat[i][4] != Sym:
                pdat[i].append('r')

    '''
    Now the program runs back through the entire pseudo data array and looks at the
    last column in every row. If the last column is the flag 'r', that row is removed.
    The removal starts at the back of the array and moves forward, so that the array's
    entries do not get their placeholders mixed up as the flagged entries are removed.
    '''

#Removal of flagged entries
    for i in reversed(range(0,len(pdat))):
        if pdat[i][len(pdat[i])-1] == 'r':
            del(pdat[i])

    return pdat
           
            

    
    
#print acquire(Theory=False, Q_low= 7000, Q_high= 8000, A_low= 1, A_high= 20, Sym=False)
    
        
            

