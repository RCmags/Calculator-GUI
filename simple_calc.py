#Program description:
# Creates a GUI for a calculator that performs basic math operations.

#--- Libraries:
import tkinter as tk


#--- Constants:
SIGNS = ( '+', '-', '*', '/', '.' )
ERROR_MESSAGE = 'Syntax Error'
FONT_NUMBER_SIZE = 9
NUM_BUTTON = 10
BUTTON_RANGE = NUM_BUTTON//3


#--- Frames:
base = tk.Tk()
box_keys = tk.Frame(base)
box_pad = tk.Frame(box_keys)
box_bottom = tk.Frame(box_pad)
box_side = tk.Frame(box_keys)


#--- Global variables:

#Output text
sum_val = ''
string_val = tk.StringVar()

#Lists for button widgets
buttons = []
button_signs = []
funcs = []
funcs_signs = []

#List for button frames
box_num = []
accum_index = 0


#--- Functions:

def FrameSize():
    return base.winfo_width()//FONT_NUMBER_SIZE

	
    #- Function to update output text
def Convert():
    string_val.set( sum_val )

	
    #- Function to delete last entry of output text
def funcDelete():
    global sum_val
    sum_val = sum_val[0:-1]
    Convert()

	
    #- Function for reset output text
def funcReset():
    global sum_val
    sum_val = ''
    Convert()

	
    #- Function for equal sign: solves expression
def funcEqual():
    global sum_val

    #Attempting to calculate expression
    try:
        sum_val = str( eval(sum_val) )
        
        if len(sum_val) > FrameSize():
            sum_val = sum_val[0:FrameSize()]
        
    #Throws error if there is a syntax error
    except:
        if sum_val != '':
            sum_val = ERROR_MESSAGE
    Convert()

	
#--- Classes:
class buttonClass:

        #- Character to repeatedly print is defined:
    def __init__(self, val):
        self.__input = str(val)

        #- Function to add character when button is pressed
    def ButtonFunc(self):
        global sum_val

        #Reset string if it is an error
        if sum_val == ERROR_MESSAGE:
            sum_val = ''

        #Force string to fit inside widget
        if len(sum_val) < FrameSize():
            sum_val += self.__input

            #Preevent first entry from being sign
            if sum_val[0] in SIGNS:
                sum_val = sum_val[1:]    

            #Prevent two signs from being next to each other
            if len(sum_val) > 1 and self.__input in SIGNS and sum_val[-2] in SIGNS:
                sum_val = sum_val[0:-1]
        Convert()


#--- Executing Program:

    #-- Creating widgets:

        #Adding titles
base.title( 'Calculator' )
name = tk.Label( base, text = "Calculator", font = ('verdana', 12, 'bold') )
text = tk.Label( base, textvariable = string_val, relief = 'sunken', bg = 'white', anchor = 'ne', font = ('verdana', FONT_NUMBER_SIZE ) )

        #Adding special operations
button_del = tk.Button( box_side, text = 'DEL', command = funcDelete, bg = 'red' )
button_reset = tk.Button( box_side, text = 'CE', command = funcReset, bg = 'orange' )
button_equal = tk.Button( box_side, text = '=', command = funcEqual, bg = 'yellow' )

        #Creating frames to that store number buttons
for index in range( BUTTON_RANGE ):
    box_num.append( tk.Frame(box_pad) )

	
        #Creating number buttons:
for index in range( NUM_BUTTON ):
    
    funcs.append( buttonClass(index) )

    #Storing buttons within box_num frames
    if index == 0:
        base_box = box_pad
    elif index <= BUTTON_RANGE:
        base_box = box_num[0]
    elif index <= 2*BUTTON_RANGE:
        base_box = box_num[1]
    else:
        base_box = box_num[2]
       
    buttons.append( tk.Button( base_box, text = str(index), command = funcs[index].ButtonFunc ) )

	
        #Creating operation buttons:
for index in range( len(SIGNS) ):

    funcs_signs.append( buttonClass( SIGNS[index] ) )

    #Storing buttons in different frames
    if index < BUTTON_RANGE:
        button_signs.append( tk.Button( box_bottom, text = SIGNS[index], command = funcs_signs[index].ButtonFunc , bg = 'cyan' ) )
    else:
        button_signs.append( tk.Button( box_side, text = SIGNS[index], command = funcs_signs[index].ButtonFunc , bg = 'cyan' ) )


    #-- Packing widgets:

        #Widgets inside base:
name.pack( side = 'top', fill = 'x', expand = 'no' )
text.pack( side = 'top', fill  = 'x', expand = 'no' )
box_keys.pack( side = 'top', fill = 'both', expand = 'yes' )

        #Widgets inside box_keys:
box_side.pack( side = 'right', fill = 'both', expand = 'yes' )
box_pad.pack( side = 'left', fill = 'both', expand = 'yes' )

        #Widgets inside box_side:
button_equal.pack( side = 'bottom', fill = 'both', expand = 'yes' )
button_reset.pack( side = 'bottom', fill = 'both', expand = 'yes' )
button_del.pack( side = 'bottom', fill = 'both', expand = 'yes' )

        #Widgets inside box_pad:
box_bottom.pack( side = 'bottom', fill = 'both', expand = 'yes' )
buttons[0].pack( side = 'bottom', fill = 'both', expand = 'yes' )


        #Buttons inside each box_num frame inside box_pad:
for index_1 in range( BUTTON_RANGE ):

    for index_2 in range( BUTTON_RANGE ):    
        buttons[1 + index_2 + accum_index].pack( side = 'left', fill = 'both', expand = 'yes' )
    #End of loop
    
    accum_index += BUTTON_RANGE
    box_num[-1 - index_1].pack( side = 'top', fill = 'both', expand = 'yes' )

	
        #Widgets inside box_pad and box_keys:
for index in range( len(SIGNS) ):

    if index < BUTTON_RANGE:
        button_signs[index].pack( side = 'left' , fill = 'both', expand = 'yes')
    else:
        button_signs[index].pack( side = 'top', fill = 'both', expand = 'yes' )
