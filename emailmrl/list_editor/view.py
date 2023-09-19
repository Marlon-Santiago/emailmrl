import PySimpleGUI as sg

def get_layout():
    return [
        [
            sg.Text('HI'),
        ] 
    ]

def get_window():
    return sg.Window('Editor de lista', get_layout())