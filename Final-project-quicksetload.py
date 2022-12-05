from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title('QuickSetLoad')
root.geometry("600x600")

def open_program():
    my_program = filedialog.askopenfilename()
    my_label.config(text=my_program)
    # Opens the program chosen by the user
    os.system('"%s"' % my_program)


my_button = Button(root, text="Open your program", command=open_program)
my_button.pack(pady = 20)

my_label = Label(root, text="")
my_label.pack(pady =20)

root.mainloop()
