import PySimpleGUI as sg

lista = ['Administrador','Aluno']

def get_layout():
    
    frame_list = [
        [
            sg.Text('Selecione a lista'),
            sg.Combo(lista, default_value = lista[1], key ='-List-'),
        ],
        [
            sg.Text('Criar uma lista'),
            sg.In(key = '-ListName-'),
            sg.Button('Criar a lista', key = '-Create-', size = (10, 1)),
        ],
        [
            sg.Button('Deletar uma lista', key = '-Delete-', size = (15, 1)),
            sg.Button('Mostrar contatos', key = '-Delete-', size = (15, 1)),
        ],
    ]
    
    layouts = [
        [
            sg.Frame('Configuirações da lista', frame_list)
        ]
    ]
    
    return layouts

def get_window():
    return sg.Window('Editor de lista', get_layout())