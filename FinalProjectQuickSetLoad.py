import tkinter as tk 
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import os


root = tk.Tk()
#total size of the gui when first opened
root.geometry('600x600')
root.title('QuickLoad Hub')

#defines opening tic tac toe program
def openTTT():
    os.system('python TicTacToe.py')
    
def openValidation():
    os.system('start ValidationtestQuickSetLoad.docx')

#defines opening survey program
def openEnterData():
    os.system('python EnterData.py')
    
#defines opening the about word doc
def open_doc():
    os.system('start UnderstandingQuickSetLoad.docx')
    
#defines the doc that is opened when you click the button in the help section
def help_doc():
    os.system('start QuickSetLoadHelp.docx')

#defines opening a program of your choice from your pc
def open_program():
    my_program = filedialog.askopenfilename()
    # Opens the program chosen by the user
    os.system('"%s"' % my_program)

#home page of the gui
def home_page():
    home_frame = tk.Frame(main_frame)
    #this is the home tab that is a welcome to the code
    lb = tk.Label(home_frame, text='Home Page ', font = ('Bold', 30))
    lb.pack()
    lb1 = tk.Label(home_frame, text='Welcome to QuickSetLoad, the program opening GUI \n\n that has quick loading programs, \n\n and is already quick set from the start!',
                   font  = ('Times New Roman', 14))
    lb1.pack()
    
    
    home_frame.pack(pady = 20)
#second page of the gui called menu which hosts all avaliable programs you can open
#like tic tac toe, the survey, and any program you wish

def menu_page():
    menu_frame = tk.Frame(main_frame)
    #the text when you open the Programs tab labeled menu in the code since it is a programs menu
    lb = tk.Label(menu_frame, text='Programs Page \n\nPage: 2', font = ('Bold', 30))
    lb.pack()

    menu_frame.pack(pady = 20)
    #this button allows you to open any program from your file explorer 
    my_button = tk.Button(menu_frame, text="Open your program", command=open_program)
    my_button.pack(pady = 40)   
     #this will open the tic tac toe game program
    TTTbutton = tk.Button(menu_frame, text="Open Tic Tac Toe", command=openTTT)
    TTTbutton.pack(pady = 40)
    #this will open the survey program that you take
    Surveybutton = tk.Button(menu_frame, text="Open survey", command=openEnterData)
    Surveybutton.pack(pady = 40)
#the about page is where the doc about the gui and my thoughts are
#this will also host a validation testing doc as well

def About_page():
    About_frame = tk.Frame(main_frame)
    #the text you'll see when you open the About tab
    lb = tk.Label(About_frame, text='About Page \n\nPage: 3', font = ('Bold', 30))
    lb.pack()
    
    About_frame.pack(pady = 20)
    #The doc opened in the About section that will teach you about 
    #this gui and my overall intentions with what I wanted to do
    About_button = tk.Button(About_frame, text = 'About this gui', command = open_doc)
    About_button.pack(pady = 20)
    #this button in the about section of the gui will open the Validation test doc
    Validation_button = tk.Button(About_frame, text = 'Validation test doc', command = openValidation)
    Validation_button.pack(pady =20)
    
#this will be the help doc page where you open the help word doc and learn how 
#to fully navigate and use this GUI
def Help_page():
    Help_frame = tk.Frame(main_frame)
    #the label you will see when you click the tab labeled help
    lb = tk.Label(Help_frame, text='Do you need any help \n\n with understanding the gui?', font = ('Bold', 15))
    lb.pack()
    #this will open the help word doc when clicked, goes more indepth on how the sections work
    #for each part of the gui
    Help_button = tk.Button(Help_frame, text = 'Help understanding this gui/UserManual', command = help_doc)
    Help_button.pack(pady = 20)
    
    Help_frame.pack(pady = 20)
    
#hides the side indicators
def indicator_hidden():
    home_indicate.config(bg="#c3c3c3")
    menu_indicate.config(bg="#c3c3c3")
    About_indicate.config(bg="#c3c3c3")
    Help_indicate.config(bg="#c3c3c3")
    
#deletes the previously open page so you don't have multiple
#opened pages from each frame like the home frame and menu frame on the about page
def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

#defines if and when to hide the indicator for a certain frame/tabm and deletes the previously
#opened frame so no frames stack on top of each other
def indicate(lb, page):
    
    indicator_hidden()
    lb.config(bg="black")
    delete_pages()
    page()


options_frame = tk.Frame(root, bg = '#c3c3c3')

#side button to go to the home page
home_button = tk.Button(options_frame, text = 'Home', font = ('Bold', 15), 
                        fg= '#158aff', bd = 0, bg = '#c3c3c3',
                        command = lambda: indicate(home_indicate, home_page))

#the location on the side bar of the home button
home_button.place(x=18, y = 50)

#the indicator that you are on the home page
home_indicate = tk.Label(options_frame, text='', bg = '#c3c3c3')
home_indicate.place(x=3, y = 50, width = 5, height = 40)

#the side button that is meant for the programs page defined as menu 
menu_button = tk.Button(options_frame, text = 'Programs', font = ('Bold', 15), 
                        fg= '#158aff', bd = 0, bg = '#c3c3c3',
                        command = lambda: indicate(menu_indicate, menu_page))

#location of the menu page on the side bar
menu_button.place(x=8, y = 100)

#indicator so you know you are on the programs page
menu_indicate = tk.Label(options_frame, text='', bg = '#c3c3c3')
menu_indicate.place(x=3, y = 100, width = 5, height = 40)

#The side button labeled as About that when clicked takes you to the about page
About_button = tk.Button(options_frame, text = 'About', font = ('Bold', 15), 
                         fg= '#158aff', bd = 0, bg = '#c3c3c3',
                         command = lambda: indicate(About_indicate, About_page))

#The about page's button location
About_button.place(x=18, y = 150)

#The about page's indicator
About_indicate = tk.Label(options_frame, text='', bg = '#c3c3c3')
About_indicate.place(x=3, y = 150, width = 5, height = 40)

#The help button the is labeled on the sidebar as helped and takes you to the help page
Help_button = tk.Button(options_frame, text = 'Help', font = ('Bold', 15), 
                         fg= '#158aff', bd = 0, bg = '#c3c3c3',
                         command = lambda: indicate(Help_indicate, Help_page))

#Defines the location of the help button
Help_button.place(x=18, y = 400)

#Defines the indicator for the help button
Help_indicate = tk.Label(options_frame, text='', bg = '#c3c3c3')
Help_indicate.place(x=3, y = 400, width = 5, height = 40)

#the side bar that holds all the buttons to each tab
options_frame.pack(side = tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width= 100, height = 600)

#This is the area that isn't taken up by the options side bar
main_frame = tk.Frame(root, highlightbackground='#c3c3c3',
                      highlightthickness=2)

main_frame.pack(side = tk.LEFT)

main_frame.pack_propagate(False)
#total size of the gui frame that is adjustable 
main_frame.configure(width = 600, height = 600)



root.mainloop()
