import PySimpleGUI as sg
import utils.button as ui

class Janelas():

    ########################################## LAYOUTS INTERFACE #################################################
    def janela_inicio(self):  # Janela de Menu
        sg.theme_background_color('#505A9A')
        sg.theme_text_element_background_color ('#505A9A')
      
        layout = [
                [sg.T(" ", )],
                [sg.Text("LabdeIA-PTI", size=(15, 1), justification="center",
                        font=('Poppins', 40, 'bold'), key='', text_color='white')],
                [sg.Image(filename='utils/images/team.png', size=(200, 200), background_color="#505A9A")],
                [sg.T(" ")],
                [sg.Button('som', key='som', button_color='#44ffff')],
                [sg.Button('', image_data=ui.button_jogar, key = 'Jogar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
                 [sg.Button('', image_data=ui.button_aluno, key = 'Aluno', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
                [sg.Button('', image_data=ui.button_instrucoes, key = 'Instruções', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
                [sg.Button('', image_data=ui.button_sair, key = 'Sair', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
                        
                [sg.Image(filename='utils/images/ptilogo.png', size=(80, 80), background_color="#505A9A")],
        ]
        return sg.Window("LabdeIA-PTI", layout=layout, size=(800, 700), element_justification='center', location=(100, 50))

    def janela_definicao(self, list_nome): # Janela de entrada de dados(nome, número de fases)
        layout = [
            [sg.Text("Selecione o nome do Aluno(a):", font=(
                'Poppins', 15), justification="center")],
            [sg.InputOptionMenu((list_nome), key="nome", size=(10, 1))],
            [sg.Text("Digite o n° de Fases:", font=(
                'Poppins', 15), justification="center")],
            [sg.InputOptionMenu(('1','2', '3', '5', '10'), key="nfases")],
            [sg.Text("Tempo:", font=(
                'Poppins', 15), justification="center")],
            [sg.InputOptionMenu(('5', '10', '15', '30', '45'), key="tempo")],
            [sg.Button('', image_data=ui.button_jogar_small, key = 'Jogar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
            sg.Button('', image_data=ui.button_voltar_small, key = 'Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],

        ]
        return sg.Window("LabdeIA-PTI", layout=layout, size=(400, 300), element_justification='center', location=(600, 300))
        
    def janela_instruction(self):  # Janela informanto o conjunto de instruções do jogo
        sg.theme('Reddit')

        layout = [
            [sg.Image('utils/images/rules.png', size=(700, 370))],
            [sg.Button('', image_data=ui.button_voltar, key = 'Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
        ]
        return sg.Window("LabdeIA-PTI", layout=layout, size=(800, 600), element_justification='center', location=(500, 150))

    def janela_jogo(self):  # Janela do jogo na perspectiva do Aluno
        sg.theme('Reddit')

        col1 = [[sg.Text("Mestre", size=(12, 1), font=('Poppins', 30, 'bold'), justification="center", key='mestre')],
                [sg.Image(filename='utils/images/teacher.png', background_color='white',
                        size=(412, 412),  key='camMestre')],
                [sg.Text("", size=(18, 1), font=('Poppins', 15),
                        justification="center", key='OutMestre')]
                ]

        col2 = [[sg.Text("Jogador(a)", size=(12, 1), font=('Poppins', 30, "bold"), justification="center", key='aluno')],
                [sg.Image(filename='utils/images/user.png', background_color='white',
                        size=(412, 412), key='camAluno')],
                [sg.Text("", size=(18, 1), font=('Poppins', 15),
                        justification="center", key='OutAluno')]
                ]

        layout = [
            [sg.T('')],
            # [sg.Text("Fase: ", size=(5, 1), justification="center", font=("Poppins", 25)), sg.Text('', size=(6, 1), font=("Poppins", 25, 'bold'), text_color='#c71017', key='fase'),
            # sg.T('                                                                                                                                                                                                   '),
            [sg.Text('', size=(5, 1), text_color='#c71017', font=('Poppins', 25, 'bold'), key='contador', justification="center"), sg.T('              '),sg.Image(filename='utils/images/cronometro.gif', size=(5,5), key='stopwatch')],


            [sg.Column(col1, element_justification='c'), sg.Column(col2, element_justification='c')],
            [sg.T('')],
            [sg.Text('', size=(32, 1), text_color='#505A9A', font=(
                'Poppins', 25), justification="center", key='expressao')],
            [sg.Text("Expressões Corretas:", size=(20, 1), justification="center", font=(
                "Poppins", 20, 'bold')), sg.Text('0', font=("Poppins", 20, 'bold'), key='scorenum')],
        ]
        return sg.Window("LabdeIA-PTI", layout=layout, element_justification='c', size=(
            1370, 800), location=(100, 50))

    def janela_final(self):
        layout = [
            [sg.Text("LabdeIA-PTI", size=(15, 1), justification="center",
                    font=('Poppins', 40, 'bold'), text_color='white')],
            [sg.Image(filename='utils/images/team.png', size=(100, 100), key='acertos')],
            [sg.Text("",size=(32,1), justification="center",font=('Helvetica', 25, 'bold'), key='mensagem')],
            [sg.Text("N° de Expressões Corretas: ", size=(23,1), font=("Helvetica", 18)), sg.Text('0', font=("Helvetica", 18), key='scorefinal')],
            [sg.Button('', image_data=ui.button_voltar, key = 'Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
            [sg.Image(filename='utils/images/ptilogo.png', size=(80, 80))],
        ]
        return sg.Window("LabdeIA-PTI", layout=layout, size=(600, 400), element_justification='center', location=(500, 300))

    def janela_final_saida(self):  # Janela de confirmação de saida
        sg.theme('Reddit')
        layout = [
            [sg.Text("Você tem certeza que deseja sair?", font=(
                'Poppins', 15), justification="center")],
            [sg.Button('', image_data=ui.button_sim, key = 'Sim', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
            sg.Button('', image_data=ui.button_nao, key = 'Não', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
        ]
        return sg.Window("LabdeIA-PTI", layout=layout, size=(400, 200), element_justification='center', location=(600,300))

########################################## LAYOUTS CADASTROALUNO #################################################

    def janela_aluno(self,data):        
        layout = [
            [sg.Text("Area dos Alunos")],
            [sg.T("")],
            [sg.Table(values=data, headings=['Nome','Idade','Sexo','Grau'],max_col_width=50, col_widths=[20,5,10,15], auto_size_columns=False, justification="center",num_rows=10, key='table')],
            [sg.Button('Cadastrar', key='cadastrar', button_color='#44ff45'),sg.Button('Editar', key='editar', button_color='#44ff45'),sg.Button('Remover', key='remover', button_color='#44ff45'),sg.Button('Relatório', key='pdf', button_color='#44ff45'),],
            [sg.Button('Voltar', key='voltar', button_color='#44ff45')],

                ]
        return sg.Window("LabdeIA-PTI", layout=layout, size=(600, 450), element_justification='center', location=(600,300))
    
    def janela_editar(self, nome, idade, sexo, grau):
        layout = [
            [sg.Text("Editar Aluno")],
            [sg.T("")],
            [sg.Text("Nome")],
            [sg.Input(nome,key="nome")],
            [sg.Text("Idade")],
            [sg.Input(idade,key="idade")],
            [sg.Text("Sexo")],
            [sg.InputOptionMenu(default_value=sexo,values=('Masculino','Feminino'),key="sexo")],
            [sg.Text("Grau")],
            [sg.Input(grau,key="grau")],
            [sg.Button('Editar', key='editar', button_color='#44ff45')],
            [sg.Button('Voltar', key='voltar', button_color='#44ff45')],
            [sg.Text("", size=(25, 1), font=('Poppins', 10),text_color='red', key='erro')]
                ]
        return sg.Window("LabdeIA-PTI", layout=layout, element_justification='center', size=(500, 400), location=(600,300))

    def janela_cadastrar(self):
        layout = [
            [sg.Text("Cadastrar Aluno")],
            [sg.T("")],
            [sg.Text("Nome")],
            [sg.Input(key="nome")],
            [sg.Text("Idade")],
            [sg.Input(key="idade")],
            [sg.Text("Sexo")],
            [sg.InputOptionMenu(values=('Masculino','Feminino'),key="sexo")],
            [sg.Text("Grau")],
            [sg.Input(key="grau")],
            [sg.Button('Cadastrar', key='salvar', button_color='#44ff45')],
            [sg.Button('Voltar', key='voltar', button_color='#44ff45')],
            [sg.Text("", size=(25, 1), font=('Poppins', 10),text_color='red', key='erro')]
                ]
        return sg.Window("LabdeIA-PTI", layout=layout, element_justification='center', size=(500, 400), location=(600,300))