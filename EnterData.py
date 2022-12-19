import PySimpleGUI as sg
import pandas as pd
#color of the gui
sg.theme('DarkTeal9')
#how it reads the excel file 
EXCEL_FILE ='Enterdata.xlsx'
df = pd.read_excel(EXCEL_FILE)

#The ways to fill out the information and what is avaliable as options to click
layout = [
    [sg.Text('Please fill out the following fields: ')],
    [sg.Text('Name', size = (15,1)), sg.InputText(key = 'Name')],
    [sg.Text('Favorite color', size = (15,1)), sg.Combo(['Green', 'Red', 'Yellow', 'Blue', 'Purple', 'Orange'], key = 'Favorite Color')],
    [sg.Text('The language I speak is', size = (15,1)),
                        sg.Checkbox('English', key = 'English'),
                        sg.Checkbox('Spanish', key = 'Spanish'),
                        sg.Checkbox('Korean', key = 'Korean'),
                        sg.Checkbox('German', key = 'German'),
                        sg.Checkbox('Russian', key = 'Russian')],
    [sg.Text('Favorite coding language', size = (18,1)), sg.InputText(key='Favorite coding Language')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window = sg.Window('Data Entry form', layout)
#clears all inputs in each field
def clear_input():
    for key in values:
        window[key]('')
    
    return None

#Defines if you sumbitted your inputs with a window after hitting the submit button
#defines if you cleared your inputs by clearing all inputs after hitting the clear button
#Closes program if you click the exit button
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        #Saves your inputs to the excel file
        df = df.append(values, ignore_index = True)
        df.to_excel(EXCEL_FILE, index = False)
        sg.popup('Your answers has been saved!')
        clear_input()
window.close()