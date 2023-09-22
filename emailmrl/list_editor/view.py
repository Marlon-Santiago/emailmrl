import PySimpleGUI as sg
from emailmrl.utils import inner_element_space

lista = ['Administrador','Aluno']

def get_layout():
    
    frame_list = [
        inner_element_space(600),
        [
            sg.Text('Selecione a lista'),
            sg.Combo(lista, default_value = lista[1], key ='-List-'),
        ],
        [
            sg.Text('Criar uma lista'),
            sg.In(key = '-ListName-'),
            sg.Button('Criar a lista', key = '-Create-', size = (15, 1), pad = (0, (7, 7))),
        ],
        [
            sg.Button('Deletar uma lista', key = '-Delete-', size = (15, 1), pad = (5, (7, 7))),
            sg.Button('Mostrar contatos', key = '-Delete-', size = (15, 1), pad = (5, (7, 7))),
        ],
    ]
    
    frame_import = [
        inner_element_space(600),
        [
            sg.Text('Selecione um arquivo (CSV):', tooltip = 'Cabeçalhos: name e email'),
            sg.In(key = '-CSV-'),
            sg.FileBrowse('Selecionar', file_types = (('CSV', '*.csv'),), tooltip = 'cabeçalhoe: name e email',),
        ],
        [
            sg.Button('Importar contatos', key = '-Import-', size = (15, 1), pad = (0, (7, 7)))
        ]
    ]
    
    frame_add = [
        inner_element_space(600),
        [
            sg.Text('Insira o nome:'),
            sg.In(key = '-Name-'),
        ],
        [
            sg.Text('insira o email:'),
            sg.In(key = '-Email-'),
        ],
        [
            sg.Button('Adicionar contato', key = '-Add-', size = (15, 1), pad = (5, (7, 7)))
        ],
    ]
    
    layouts = [
        [
            sg.Frame('Configurações da lista', frame_list, element_justification = 'c')
        ],
        [
            sg.Frame('Importa contatos', frame_import, element_justification = 'c')
        ],
        [
            sg.Frame('Adiçionar contato', frame_add, element_justification = 'c')
        ],
        [
            sg.Button('Voltar', key = '-Back-', size = (15, 1), pad = (5, (7, 7)))
        ]
    ]
    
    return layouts

def get_window():
    sg.theme('DarkBlue')
    return sg.Window('Editor de lista', get_layout(), element_justification = 'c')