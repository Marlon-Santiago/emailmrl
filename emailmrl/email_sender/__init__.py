import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED
from emailmrl.email_sender import view
from emailmrl.list_editor.menager import initialize as init_editor

class Email_Sender():
    def __init__(self):
        self.window = None
        
    def instantiate(self):
        if self.window == None:
            self.window = view.get_windows()
        
    def enable_window(self):
        self.instantiate()
    
        while True:
            event, values = self.window.read()
        
            if event == WIN_CLOSED:
                self.close_window()
                break
        
            if event == '-Send-':
                title = values['-Title-']
                content = values['-Content-']
            
                sg.popup(f'O titulo é: {title} o  conteudo é: {content}', title = 'E-mail')
            
            if event == '-ListEditor-':
                self.hide_window()
                init_editor()
            
    def close_window(self):
        if self.window is not None:
            self.window.close()
            
    def hide_window(self):
        if self.window is not None:
            self.window.close()
            
    def unhide_window(self):
        if self.window is not None:
            self.window.UnHide()
        

