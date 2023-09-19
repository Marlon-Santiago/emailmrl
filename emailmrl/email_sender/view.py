import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED

listas = ['Administradores', 'Alunos']

def get_layouts():
    layout = [
        [
            sg.Text('Selecione o seu codigo'),
            sg.In(),
            sg.FilesBrowse('Selecione', file_types = (('Codigo Python', '*.py'),)),
        ],
        [
            sg.Text('Seleciona a lista de destinatario'),
            sg.Combo(listas, default_value = listas[1]),
        ],
        [
            sg.Text('Insira o Titulo: '),
            sg.In(key = '-Title-'),
        ],
        [
            sg.Text('Insira o conteudo do email'),
            sg.MLine(key = '-Content-'),
        ],
        [
            sg.Button('Enviar', key = '-Send-'),
            sg.Button('Gerenciar listas', key = '-ListEditor-')
        ]
    ]
        
        
    return layout

def get_windows():
    return sg.Window('Teste de Janela', get_layouts())
