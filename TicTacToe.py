import tkinter as tk 
from tkinter import *
from tkinter import messagebox as mbox 

root = tk.Tk()
root.title('QuickLoad Hub')

#X starts so True
clicked = True
count=0
#Check to see if someone has won tictactoe



def wincheck():
    global winner
    winner=False
    #checks for 'X' win 
    if bu1["text"] == "X" and bu2["text"] == "X" and bu3["text"] == "X":
        bu1.config(bg="red")
        bu2.config(bg="red")
        bu3.config(bg="red")
        winner = True
        mbox.showinfo("Tic Tac Toe", "Player 1 wins!")
        disableAllButtons()
    elif bu4["text"] == "X" and bu5["text"] == "X" and bu6["text"] == "X":
        bu4.config(bg="red")
        bu5.config(bg="red")
        bu6.config(bg="red")
        winner = True
        mbox.showinfo("Tic Tac Toe", "Player 1 wins!")
        disableAllButtons()
    elif bu7["text"] == "X" and bu8["text"] == "X" and bu9["text"] == "X":
        bu7.config(bg="red")
        bu8.config(bg="red")
        bu9.config(bg="red")
        winner = True
        mbox.showinfo("Tic Tac Toe", "Player 1 wins!")
        disableAllButtons()
    elif bu1["text"] == "X" and bu4["text"] == "X" and bu7["text"] == "X":
        bu1.config(bg="red")
        bu4.config(bg="red")
        bu7.config(bg="red")
        winner = True
        mbox.showinfo("Tic Tac Toe", "Player 1 wins!")
        disableAllButtons()
    elif bu2["text"] == "X" and bu5["text"] == "X" and bu8["text"] == "X":
        bu2.config(bg="red")
        bu5.config(bg="red")
        bu8.config(bg="red")
        winner = True
        mbox.showinfo("Tic Tac Toe", "Player 1 wins!")
        disableAllButtons()
    elif bu3["text"] == "X" and bu6["text"] == "X" and bu9["text"] == "X":
        bu3.config(bg="red")
        bu6.config(bg="red")
        bu9.config(bg="red")
        winner = True
        mbox.showinfo("Tic Tac Toe", "Player 1 wins!")
        disableAllButtons()
    elif bu1["text"] == "X" and bu5["text"] == "X" and bu9["text"] == "X":
        bu1.config(bg="red")
        bu5.config(bg="red")
        bu9.config(bg="red")
        winner = True
        mbox.showinfo("Tic Tac Toe", "Player 1 wins!")
        disableAllButtons()
    elif bu3["text"] == "X" and bu5["text"] == "X" and bu7["text"] == "X":
        bu3.config(bg="red")
        bu5.config(bg="red")
        bu7.config(bg="red")
        winner = True
        mbox.showinfo("Tic Tac Toe", "Player 1 wins!")  
        disableAllButtons()
#check for 'O' win       
    if bu1["text"] == "O" and bu2["text"] == "O" and bu3["text"] == "O":
        bu1.config(bg="red")
        bu2.config(bg="red")
        bu3.config(bg="red")
        winner = True
        mbox.showinfo("Tic Tac Toe", "Player 2 wins!")
        disableAllButtons()
    elif bu4["text"] == "O" and bu5["text"] == "O" and bu6["text"] == "O":
        bu4.config(bg="red")
        bu5.config(bg="red")
        bu6.config(bg="red")
        winner = True
        mbox.showinfo("Tic Tac Toe", "Player 2 wins!")
        disableAllButtons()
    elif bu7["text"] == "O" and bu8["text"] == "O" and bu9["text"] == "O":
        bu7.config(bg="red")
        bu8.config(bg="red")
        bu9.config(bg="red")
        winner = True
        mbox.showinfo("Tic Tac Toe", "Player 2 wins!")
        disableAllButtons()
    elif bu1["text"] == "O" and bu4["text"] == "O" and bu7["text"] == "O":
        bu1.config(bg="red")
        bu4.config(bg="red")
        bu7.config(bg="red")
        winner = True
        mbox.showinfo("Tic Tac Toe", "Player 2 wins!")
        disableAllButtons()
    elif bu2["text"] == "O" and bu5["text"] == "O" and bu8["text"] == "O":
        bu2.config(bg="red")
        bu5.config(bg="red")
        bu8.config(bg="red")
        winner = True
        mbox.showinfo("Tic Tac Toe", "Player 2 wins!")
        disableAllButtons()
    elif bu3["text"] == "O" and bu6["text"] == "O" and bu9["text"] == "O":
        bu3.config(bg="red")
        bu6.config(bg="red")
        bu9.config(bg="red")
        winner = True
        mbox.showinfo("Tic Tac Toe", "Player 2 wins!")
        disableAllButtons()
    elif bu1["text"] == "O" and bu5["text"] == "O" and bu9["text"] == "O":
        bu1.config(bg="red")
        bu5.config(bg="red")
        bu9.config(bg="red")
        winner = True
        mbox.showinfo("Tic Tac Toe", "Player 2 wins!")
        disableAllButtons()
    elif bu3["text"] == "O" and bu5["text"] == "O" and bu7["text"] == "O":
        bu3.config(bg="red")
        bu5.config(bg="red")
        bu7.config(bg="red")
        winner = True
        mbox.showinfo("Tic Tac Toe", "Player 2 wins!")   
        disableAllButtons()
    if count == 9 and winner == False:
        mbox.showinfo("Tic Tac Toe", "No one has won it is a tie\n no one wins")
        disableAllButtons(); 
#the fuction that stops all buttons from being clicked after someone wins or a tie occurs       
def disableAllButtons():
    bu1.config(state=DISABLED)
    bu2.config(state=DISABLED)
    bu3.config(state=DISABLED)
    bu4.config(state=DISABLED)
    bu5.config(state=DISABLED)
    bu6.config(state=DISABLED)
    bu7.config(state=DISABLED)
    bu8.config(state=DISABLED)
    bu9.config(state=DISABLED)
    
#button clicked function
def b_click(bu):
    global clicked, count
    
    if bu["text"] == " " and clicked == True:
        bu["text"]= "X"
        clicked = False
        count += 1
        wincheck()
    elif bu["text"] == " " and clicked == False:
        bu["text"]= "O"
        clicked = True
        count += 1
        wincheck()
        
        
    else: 
        mbox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick another box ")
def reset():
    #allows for each button to be useable everywhere in the code
    global bu1, bu2, bu3, bu4, bu5, bu6, bu7, bu8, bu9
    #allows for our defined clicked and count function to be used here
    global clicked, count
    #sets the turn to True which is 'X'(player1) turn
    clicked = True
    #Starts at 0 for how many turns has been played so far
    count = 0
    #Each button to the tic tac toe board from top left to bottom right
    bu1 = Button(root, text=' ', font=("Helvetica",20), height = 3, width = 6, bg ="SystemButtonFace",
                command = lambda: b_click(bu1))
    bu2 = Button(root, text=' ', font=("Helvetica",20), height = 3, width = 6, bg ="SystemButtonFace",
                command = lambda: b_click(bu2))
    bu3 = Button(root, text=' ', font=("Helvetica", 20), height = 3, width = 6, bg ="SystemButtonFace",
                command = lambda: b_click(bu3))

    bu4 = Button(root, text=' ', font=("Helvetica", 20), height = 3, width = 6, bg ="SystemButtonFace",
                command = lambda: b_click(bu4))
    bu5 = Button(root, text=' ', font=("Helvetica", 20), height = 3, width = 6, bg ="SystemButtonFace",
                command = lambda: b_click(bu5))
    bu6 = Button(root, text=' ', font=("Helvetica", 20), height = 3, width = 6, bg ="SystemButtonFace",
                command = lambda: b_click(bu6))

    bu7 = Button(root, text=' ', font=("Helvetica", 20), height = 3, width = 6, bg ="SystemButtonFace",
                command = lambda: b_click(bu7))
    bu8 = Button(root, text=' ', font=("Helvetica", 20), height = 3, width = 6, bg ="SystemButtonFace",
                command = lambda: b_click(bu8))
    bu9 = Button(root, text=' ', font=("Helvetica", 20), height = 3, width = 6, bg ="SystemButtonFace",
                command = lambda: b_click(bu9))
    #defines the location of each button from button 1 to 9
    bu1.grid(row=0, column=0)
    bu2.grid(row=0, column=1)
    bu3.grid(row=0, column=2)

    bu4.grid(row=1, column=0)
    bu5.grid(row=1, column=1)
    bu6.grid(row=1, column=2)

    bu7.grid(row=2, column=0)
    bu8.grid(row=2, column=1)
    bu9.grid(row=2, column=2)



#create menu

my_menu = Menu(root)
root.config(menu=my_menu)

options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command = reset)

reset()

root.mainloop()