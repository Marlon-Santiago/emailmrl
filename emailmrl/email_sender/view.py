import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED
from emailmrl.utils import inner_element_space

listas = ['Administradores', 'Alunos']

def get_layouts():
    inner_element_space(500),
    
    frame_campaing = [
        
        [
            sg.Text('Selecione o seu codigo'),
            sg.In(key = '-Code-', size = (30, 1)),
            sg.FilesBrowse('Selecione', file_types = (('Codigo Python', '*.py'),), size = (15, 1)),
        ],
        [
            sg.Text('Seleciona a lista de destinatario'),
            sg.Combo(listas, default_value = listas[1], key = '-Lists-',),
        ]
    ]

    frame_email = [
        inner_element_space(500),
        [
            sg.Text('Insira o Titulo', font = ('Helvetica 15')),
        ],
        [
            sg.In(key = '-Title-', size = (62, 1)),
        ],
        [
            sg.Text('Insira o conteudo', font = ('Helvetica 15')),
        ],
        [
            sg.MLine(key = '-Content-', size = (60, 10)),
        ],
        inner_element_space(500)
    ]
    



    layout = [
        [
            sg.Frame('Configuração da campanha', frame_campaing, element_justification = 'c'),
        ],
        [
            sg.Frame('Configuração de E-mail', frame_email, element_justification = 'c'),
        ],
        [
            sg.Button('Enviar e-mail', key = '-Send-', size = (15, 1), pad = (10, (10, 0))),
            sg.Button('Gerenciar listas', key = '-ListEditor-', size = (15, 1), pad = (10, (10, 0)))
        ],
        inner_element_space(500),
        
    ]
        
        
    return layout

def get_windows():
    sg.theme('DarkBlue')
    return sg.Window('Enviador de E-mail', get_layouts())
