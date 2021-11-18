import numpy as np
import PySimpleGUI as sg
import button

class Windows():
    
    def janela_inicio(self):

        sg.theme('Reddit')
        sg.theme_background_color('#505A9A')
        sg.theme_text_element_background_color ('#505A9A')

        layout = [
            [sg.T(" ", )],
            [sg.Text("LabdeIA-PTI", size=(15, 1), justification="center",
                    font=('Poppins', 40, 'bold'), key='', text_color='white')],
            [sg.Image(filename='images.utils/team.png', size=(200, 200), background_color="#505A9A")],
            [sg.T(" ")],
            [sg.Button('', image_data=button.button_individual, key = 'Individual', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
            [sg.Button('', image_data=button.button_multijogador, key = 'Multijogador', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
            [sg.Button('', image_data=button.button_instrucoes, key = 'Instruções', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
            [sg.Button('', image_data=button.button_sair, key = 'Sair', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
            
            [sg.Image(filename='images.utils/ptilogo.png', size=(80, 80), background_color="#505A9A")],
        ]
        return sg.Window("LabdeIA-PTI", layout=layout, size=(800, 700), element_justification='center', location=(2000, 150))

    def janela_definicaoSP(self):
        sg.theme('Reddit')

        layout = [
            [sg.Text("Digite o seu nome:", font=(
                'Poppins', 15), justification="center")],
            [sg.Input(key="nome", size=(10, 1), font=('Poppins', 15))],
            [sg.Button('', image_data=button.button_jogar_small, key = 'Jogar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
            sg.Button('', image_data=button.button_voltar_small, key = 'Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
        ]
        return sg.Window("LabdeIA-PTI - Individual", layout=layout, size=(400, 200), element_justification='center', location=(2200, 300))

    def janela_definicaoMP(self): # Janela de entrada de dados(nome, número de fases)
        sg.theme('Reddit')

        layout = [
            [sg.Text("Digite o nome do Jogador(a):", font=(
                'Poppins', 15), justification="center")],
            [sg.Input(key="nome", size=(10, 1), font=('Poppins', 15))],
            [sg.Text("Digite o n° de Fases:", font=(
                'Poppins', 15), justification="center")],
            [sg.Input(key="nfases", size=(5, 1), font=('Poppins', 15))],
            [sg.Button('', image_data=button.button_jogar_small, key = 'Jogar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
            sg.Button('', image_data=button.button_voltar_small, key = 'Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
        ]
        return sg.Window("LabdeIA-PTI - Multijogador", layout=layout, size=(400, 200), element_justification='center', location=(2200, 300))


    def janela_final(self):
        layout = [
            [sg.Text("LabdeIA-PTI", size=(15, 1), justification="center",
                    font=('Poppins', 40, 'bold'), text_color='white')],
            [sg.Image(filename='images.utils/crown.png', size=(100, 100), key='acertos')],
            [sg.Text("",size=(32,1), justification="center",font=('Helvetica', 25, 'bold'), key='mensagem')],
            [sg.Text("N° de Expressões Corretas: ", size=(23,1), font=("Helvetica", 18)), sg.Text('0', font=("Helvetica", 18), key='scorefinal')],
            [sg.Button('', image_data=button.button_voltar, key = 'Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
            [sg.Image(filename='images.utils/ptilogo.png', size=(80, 80))],
        ]
        return sg.Window("LabdeIA-PTI", layout=layout, size=(600, 400), element_justification='center', location=(2100, 300))

    def janela_instruction(self):
        sg.theme('Reddit')
        layout = [
            [sg.Image('images.utils/rules.png',size=(700,600))],
            [sg.Button('', image_data=button.button_voltar, key = 'Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
        ]
        return sg.Window("LabdeIA-PTI",layout=layout, size=(800, 700), element_justification='center', location=(2000, 150))


    def janela_mestre(self):  # Janela do jogo na pespectiva do Mestre
        sg.theme('Reddit')

        layout = [
            [sg.T('')],
            [sg.Text("Fase: ", size=(5, 1), justification="center", font=("Poppins", 25)), sg.Text('', size=(6, 1), font=("Poppins", 25, 'bold'), text_color='#c71017', key='fase'),
            sg.T('                                                                                                                                                                                                  '),
            sg.Text("Tempo:", size=(7, 1), justification="center", font=("Poppins", 25)), sg.Text('', size=(12, 1), text_color='#c71017', font=('Poppins', 25, 'bold'), key='contador')],

            [
                [sg.Text("Mestre", size=(12, 1), font=('Poppins', 30,
                        'bold'), justification="center", key='mestre')],
                [sg.Image(filename='images.utils/teacher.png', background_color='white',
                        size=(412, 412),  key='camMestre')],
                [sg.Text("", size=(18, 1), font=('Poppins', 15),
                        justification="center", key='OutMestre')]
            ],

            [sg.T('')],
            [sg.Text('', size=(28, 1), text_color='#114E0E', font=(
                'Poppins', 25), justification="center", key='expressao')],
        ]
        return sg.Window("LabdeIA-PTI - Multijogador", layout=layout, element_justification='c', size=(
            1370, 800), location=(1750, 50))

    def janela_jogoMP(self):    # multiplayer
        sg.theme('Reddit')

        col1 = [[sg.Text("Mestre", size=(12, 1), font=('Poppins', 30, 'bold'), justification="center", key='mestre')],
                [sg.Image(filename='images.utils/teacher.png', background_color='white',
                        size=(412, 412),  key='camMestre')],
                [sg.Text("", size=(18, 1), font=('Poppins', 15),
                        justification="center", key='OutMestre')]
                ]

        col2 = [[sg.Text("Jogador(a)", size=(12, 1), font=('Poppins', 30, "bold"), justification="center", key='aluno')],
                [sg.Image(filename='images.utils/user.png', background_color='white',
                        size=(412, 412), key='camAluno')],
                [sg.Text("", size=(18, 1), font=('Poppins', 15),
                        justification="center", key='OutAluno')]
                ]

        layout = [
            [sg.T('')],
            [sg.Text("Fase: ", size=(5, 1), justification="center", font=("Poppins", 25)), sg.Text('', size=(6, 1), font=("Poppins", 25, 'bold'), text_color='#c71017', key='fase'),
            sg.T('                                                                                                                                                                                                   '),
            sg.Text("Tempo:", size=(7, 1), justification="center", font=("Poppins", 25)), sg.Text('', size=(12, 1), text_color='#c71017', font=('Poppins', 25, 'bold'), key='contador')],


            [sg.Column(col1, element_justification='c'), sg.Column(col2, element_justification='c')],
            [sg.T('')],
            [sg.Text('', size=(32, 1), text_color='#505A9A', font=(
                'Poppins', 25), justification="center", key='expressao')],
            [sg.Text("Expressões Corretas:", size=(20, 1), justification="center", font=(
                "Poppins", 20, 'bold')), sg.Text('0', font=("Poppins", 20, 'bold'), key='scorenum')],
        ]
        return sg.Window("LabdeIA-PTI - Multijogador", layout=layout, element_justification='c', size=(
            1370, 800), location=(35, 50))

    def janela_jogoSP(self):        # singleplayer
        sg.theme('Reddit')

        col1 = [[sg.Image(filename='images.utils/teacher.png', background_color='white',
                        size=(412, 412),  key='Imagem')],
                [sg.Text("", size=(18, 1), font=('Poppins', 15),
                        justification="center", key='OutImage')]
                ]

        col2 = [[sg.Text("Jogador(a)", size=(12, 1), font=('Poppins', 30, "bold"), justification="center", key='Jogador')],
                [sg.Image(filename='images.utils/user.png', background_color='white',
                        size=(412, 412), key='camJogador')],
                [sg.Text("", size=(18, 1), font=('Poppins', 15),
                        justification="center", key='OutJogador')]
                ]

        layout = [
            [sg.T('')],
            [sg.Text("Fase: ", size=(5, 1), justification="center", font=("Poppins", 25)), sg.Text('', size=(6, 1), font=("Poppins", 25, 'bold'), text_color='#c71017', key='fase'),
            sg.T('                                                                                                                                                                                                   '),
            sg.Text("Tempo:", size=(7, 1), justification="center", font=("Poppins", 25)), sg.Text('', size=(12, 1), text_color='#c71017', font=('Poppins', 25, 'bold'), key='contador')],


            [sg.Column(col1, element_justification='c'), sg.VSeparator(
                'white'), sg.Column(col2, element_justification='c')],
            [sg.T('')],
            [sg.Text('', size=(30, 1), text_color='#114E0E', font=(
                'Poppins', 25), justification="center", key='expressao')],
            [sg.Text("Expressões Corretas:", size=(20, 1), justification="center", font=(
                "Poppins", 20, 'bold')), sg.Text('0', font=("Poppins", 20, 'bold'), key='scorenum')],
        ]
        return sg.Window("LabdeIA-PTI - Individual", layout=layout, element_justification='c', size=(
            1370, 800), location=(1750, 50))

    def janela_final_saida(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text("Você tem certeza que deseja sair?", font=('Helvetica', 15 ,"bold"), justification="center")],
            [sg.Button('', image_data=button.button_sim, key = 'Sim', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
            sg.Button('', image_data=button.button_nao, key = 'Não', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
            ]
        return sg.Window("LabdeIA-PTI",layout=layout, size=(400, 200), element_justification='center', location=(2200, 300))