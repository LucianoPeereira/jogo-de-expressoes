import cv2
import time
import sys
import numpy as np
import button
from rmn import RMN
import PySimpleGUI as sg

rmn = RMN()
current_time = 0 #Tempo
aux = False # Auxiliar while
aux_confirm = 0 # Auxiliar do segundo while
score = 0 # Pontuação

def time_as_int(): #Funcao do tempo do Jogo
    return int(round(time.time() * 100))

########################################## LAYOUTS INTERFACE #################################################333

def janela_inicio():  # Janela de Menu
    sg.theme('Reddit')
    sg.theme_background_color('#505A9A')
    sg.theme_text_element_background_color ('#505A9A')
    
    layout = [
            [sg.T(" ", )],
            [sg.Text("LabdeIA-PTI", size=(15, 1), justification="center",
                    font=('Poppins', 40, 'bold'), key='', text_color='white')],
            [sg.Image(filename='images/team.png', size=(200, 200), background_color="#505A9A")],
            [sg.T(" ")],
            [sg.Button('', image_data=button.button_jogar, key = 'Jogar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
            [sg.Button('', image_data=button.button_instrucoes, key = 'Instruções', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
            [sg.Button('', image_data=button.button_sair, key = 'Sair', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
                    
            [sg.Image(filename='images/ptilogo.png', size=(80, 80), background_color="#505A9A")],
    ]
    return sg.Window("LabdeIA-PTI", layout=layout, size=(800, 600), element_justification='center', location=(2000, 150))

def janela_definicao(): # Janela de entrada de dados(nome, número de fases)
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
    return sg.Window("LabdeIA-PTI", layout=layout, size=(400, 200), element_justification='center', location=(2200, 300))


def janela_final():
    layout = [
        [sg.Text("LabdeIA-PTI", size=(15, 1), justification="center",
                font=('Poppins', 40, 'bold'), text_color='white')],
        [sg.Image(filename='images/team.png', size=(100, 100), key='acertos')],
        [sg.Text("",size=(32,1), justification="center",font=('Helvetica', 25, 'bold'), key='mensagem')],
        [sg.Text("N° de Expressões Corretas: ", size=(23,1), font=("Helvetica", 18)), sg.Text('0', font=("Helvetica", 18), key='scorefinal')],
        [sg.Button('', image_data=button.button_voltar, key = 'Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
        [sg.Image(filename='images/ptilogo.png', size=(80, 80))],
    ]
    return sg.Window("LabdeIA-PTI", layout=layout, size=(600, 400), element_justification='center', location=(2100, 300))

def janela_jogo():  # Janela do jogo na perspectiva do Aluno
    sg.theme('Reddit')

    col1 = [[sg.Text("Mestre", size=(12, 1), font=('Poppins', 30, 'bold'), justification="center", key='mestre')],
            [sg.Image(filename='images/teacher.png', background_color='white',
                      size=(412, 412),  key='camMestre')],
            [sg.Text("", size=(18, 1), font=('Poppins', 15),
                     justification="center", key='OutMestre')]
            ]

    col2 = [[sg.Text("Jogador(a)", size=(12, 1), font=('Poppins', 30, "bold"), justification="center", key='aluno')],
            [sg.Image(filename='images/user.png', background_color='white',
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
    return sg.Window("LabdeIA-PTI", layout=layout, element_justification='c', size=(
        1370, 800), location=(35, 50))

def janela_mestre():  # Janela do jogo na pespectiva do mestre
    sg.theme('Reddit')

    layout = [
        [sg.T('')],
        [sg.Text("Fase: ", size=(5, 1), justification="center", font=("Poppins", 25)), sg.Text('', size=(6, 1), font=("Poppins", 25, 'bold'), text_color='#c71017', key='fase'),
         sg.T('                                                                                                                                                                                                  '),
         sg.Text("Tempo:", size=(7, 1), justification="center", font=("Poppins", 25)), sg.Text('', size=(12, 1), text_color='#c71017', font=('Poppins', 25, 'bold'), key='contador')],

        [
            [sg.Text("Mestre", size=(12, 1), font=('Poppins', 30,
                     'bold'), justification="center", key='mestre')],
            [sg.Image(filename='images/teacher.png', background_color='white',
                      size=(412, 412),  key='camMestre')],
            [sg.Text("", size=(18, 1), font=('Poppins', 15),
                     justification="center", key='OutMestre')]
        ],

        [sg.T('')],
        [sg.Text('', size=(28, 1), text_color='#114E0E', font=(
            'Poppins', 25), justification="center", key='expressao')],
    ]
    return sg.Window("LabdeIA-PTI", layout=layout, element_justification='c', size=(
        1370, 800), location=(1750, 50))

def janela_instruction():  # Janela informanto o conjunto de instruções do jogo
    sg.theme('Reddit')

    layout = [
        [sg.Image('images/rules.png', size=(700, 370))],
        [sg.Button('', image_data=button.button_voltar, key = 'Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
    ]
    return sg.Window("LabdeIA-PTI", layout=layout, size=(800, 600), element_justification='center', location=(2000, 150))

def janela_final_saida():  # Janela de confirmação de saida
    sg.theme('Reddit')

    layout = [
        [sg.Text("Você tem certeza que deseja sair?", font=(
            'Poppins', 15), justification="center")],
        [sg.Button('', image_data=button.button_sim, key = 'Sim', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
        sg.Button('', image_data=button.button_nao, key = 'Não', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
    ]
    return sg.Window("LabdeIA-PTI", layout=layout, size=(400, 200), element_justification='center', location=(2200, 300))

############################################ FUNCIONALIDADES ###################################################3

def translateEmo(emolabel):  # Traduz o emolabel para o 'OutMestre' da JANELA6 e JANELA2
    emocao = ""

    if(emolabel == 'happy'):
        emocao = "Feliz"
    elif(emolabel == 'sad'):
        emocao = "Triste"
    elif(emolabel == 'neutral'):
        emocao = "Neutro"
    elif(emolabel == 'disgust'):
        emocao = "Nojo"
    elif(emolabel == 'fear'):
        emocao = "Medo"
    elif(emolabel == 'angry'):
        emocao = "Bravo"
    elif(emolabel == 'surprise'):
        emocao = "Surpreso"

    return emocao

# Faz a contagem para o usuário (mestre ou aluno) ser capturado
def nextTurn(user, janela2, janela6, i, n, nome="aluno"):
    current_time = 0
    start_time = time_as_int()

    if(user == "aluno"):
        janela6['camMestre'].update(
            filename="images/teacher.png") #Atualiza a imagem na aba mestre - (Janela mestre)                                   
        
        janela6['expressao'].update(" ") # Limpa o campo de 'Faca uma expressão'
        janela6['mestre'].update(text_color="black", font=(
            'Poppins', 30, "bold"))                       

        while current_time <= 500: # Timer de contagem (5 segundos)
          
            event, values = janela2.read(timeout=1)
            
            if event == sg.WIN_CLOSED:
                janela2.close()
                sys.exit()
                
            janela2['contador'].update('{:02d}'.format( #Atualiza o tempo da Janela do Aluno
                (current_time // 100) % 60))                       
            janela2['OutAluno'].update(" ", text_color="black", font=(
                'Poppins', 20, "bold")) #
            janela2['expressao'].update(
                "Atenção "+nome+", agora é a sua vez!", font=('Poppins', 28, "bold"))  

            current_time = time_as_int() - start_time

        janela2['expressao'].update("Faça uma Expressão!", font=('Poppins', 28, "bold"))                    
        janela2['mestre'].update(text_color="black", font=('Poppins', 20, "bold"))                       

    elif(user == "mestre"):
        while current_time <= 500: # Timer de contagem (5 segundos)                                                                    # feito
            
            event2, values2 = janela2.read(timeout=1)
            event, values = janela6.read(timeout=1)
            
            if event == sg.WIN_CLOSED or event2 == sg.WIN_CLOSED:
                janela6.close()
                janela2.close()
                sys.exit()

            janela2['aluno'].update(nome)
            janela2['contador'].update("")
            janela2['mestre'].update(text_color="black", font=('Poppins', 30, "bold"))                   
            janela2['aluno'].update(text_color="black", font=('Poppins', 30, "bold"))                       

            janela2['expressao'].update(" ")
        
            janela2['OutMestre'].update(" ")
            janela2['OutAluno'].update("Aguarde", text_color="#D4181A", font=(
                "Poppins", 25, "bold"))                                                               

            fase_str = str(i+1) + " / " + str(n)
            janela2['fase'].update(str(fase_str))
            janela6['fase'].update(str(fase_str))
          
            janela6['OutMestre'].update(" ")
            janela6['contador'].update('{:02d}'.format(
                (current_time // 100) % 60))                         
            janela6['expressao'].update(
                "Atenção Mestre, é a sua vez!", font=('Poppins', 28, "bold"))  
            janela6['camMestre'].update(filename="images/teacher.png")

            current_time = time_as_int() - start_time
        
        janela6['expressao'].update("Mestre, faça uma Expressão!")
        janela6['mestre'].update(text_color="black", font=('Poppins', 20, "bold"))                      

def mestreCaptura(janela2, janela6, i, n, nome, neutral=0):  # Captura da tela do mestre
    vid = cv2.VideoCapture(2)
    maior = 0
    frame_dic = {}
    emotion = ""
    frame = ""
    img_frame = ""
    emotions = []
    emocao = ""

    # "Atenção Mestre, é a sua vez!",
    nextTurn("mestre", janela2, janela6, i, n, nome)

    current_time = 0
    start_time = time_as_int()

    while current_time <= 500:  # Timer 5 segundos de Captura das expressões do mestre
        event2, values2 = janela2.read(timeout=1)
        event, values = janela6.read(timeout=1)
        janela6['contador'].update('{:02d}.{:02d}'.format(
            (current_time // 100) % 60, current_time % 100))

        ret, frame_cap = vid.read()
        

        if frame_cap is None or ret is not True:
            continue

        try:

            if event == sg.WIN_CLOSED or event2 == sg.WIN_CLOSED:
                vid.release()
                janela2.close()
                janela6.close()
                sys.exit()

            emoproba = 0
            emolabelProf = ""

            current_time = time_as_int() - start_time

            frame_cap = np.fliplr(frame_cap).astype(np.uint8)
            resultsProf = rmn.detect_emotion_for_single_frame(frame_cap)
            # frame_cap = cv2.resize(frame_cap(200,200))

            # Captura de emoções

            for resultProf in resultsProf:
                emolabelProf = resultProf['emo_label']
                emoproba = resultProf['emo_proba']

                emocao = translateEmo(emolabelProf) # Traduz o emolabel

                janela6['OutMestre'].update(
                    emocao,  text_color="black", font=("Poppins", 25, "bold"))

            # Capta as expressões diferentes de neutro e com 70% do emoproba
            if(emoproba > 0.7 and emolabelProf != "neutral"):
                emotions.append(emolabelProf)

                # Se o emolabel for diferente de todas as keys, incrementa no frame_dic
                if(emolabelProf != key for key in frame_dic):
                    frame_dic[emolabelProf] = frame_cap

            imgbytes = cv2.imencode('.png', frame_cap)[1].tobytes()
            janela6['camMestre'].update(data=imgbytes)

        except Exception as err:
            print(err)
            continue

    for e in emotions: # Captura a emoção com maior frequência
        if(emotions.count(e) > maior):
            maior = emotions.count(e)
            emotion = e         # emolabel final

    # Condicional caso não tenha sido gerado emoção ou só tenha gerado neutro
    if len(emotions) <= 0 and emotion == "":
        neutral += 1

        if(neutral >= 5): # Retorna ao menu
            return -1

        current_time = 0
        start_time = time_as_int()

        while current_time <= 500: # Timer de delay e update
            event, values = janela6.read(timeout=1)
            
            if event == sg.WIN_CLOSED:
                janela6.close()
                sys.exit()
            
            janela6['camMestre'].update(filename="images/teacher.png")
            janela6['OutMestre'].update(
                "Tente Novamente", text_color="#D4181A", font=("Poppins", 25, "bold"))
            current_time = time_as_int() - start_time

        start_time = time_as_int()
        vid.release() # Interrompe a captura do RMN
        emotion = mestreCaptura(janela2, janela6, i, n, nome, neutral)

    emocao = translateEmo(emotion)

    janela2['OutMestre'].update(
        emocao, text_color="black", font=("Poppins", 25, "bold"))
    janela6['OutMestre'].update(
        emocao, text_color="black", font=("Poppins", 25, "bold"))

    # Função que capta o frame de acordo com expressão de maior frequência
    for key in frame_dic:   # Guarda a imagem do mestre
        if key == emotion:
            img_frame = cv2.imencode('.png', frame_dic[key])[1].tobytes()
            janela2['camMestre'].update(data=img_frame)
            janela6['camMestre'].update(data=img_frame)

    vid.release()
    return emotion

def alunoRec(janela1, janela2, janela6, n, nome):  # Captura das expressôes do Aluno
    janela1.close()
    score = 0

    for i in range(int(n)): # Fases do jogo
        results = []
        result = {}

        emo_p = mestreCaptura(janela2, janela6, i, n, nome) # Chama a captura do mestre 

        # Caso só tenha sido gerado neutro ele retorna -1 para retornar ao menu
        if(emo_p == -1):
            janela2.close()
            janela6.close()
            return -1

        vid1 = cv2.VideoCapture(0)
        

        # "Atenção Aluno, é a sua vez!"
        nextTurn("aluno", janela2, janela6, i, n, nome)

        current_time = 0
        start_time = time_as_int()

        # Captura e comparação de expressôes do Aluno com o mestre
        while True:
            ret, frame = vid1.read()
            if frame is None or ret is not True:
                continue

            event, values = janela2.read(timeout=1)
            event6, values6 = janela6.read(timeout=1)

            janela2['aluno'].update(
                text_color="black", font=('Poppins', 20, "bold"))

            if event == sg.WIN_CLOSED or event6 == sg.WIN_CLOSED:
                vid1.release()
                janela6.close()
                janela2.close()
                sys.exit()

            try:
                emoproba = 0
                emolabel = ""

                # Update na tela dos frames da Webcam
                frame = np.fliplr(frame).astype(np.uint8)
                imgbytes = cv2.imencode('.png', frame)[1].tobytes()
                janela2['camAluno'].update(data=imgbytes)
                janela2['contador'].update('{:02d}.{:02d}'.format(
                    (current_time // 100) % 60, current_time % 100))

                # Começa a captura das expressões depois de 2 segundos
                current_time = time_as_int() - start_time
                if(current_time >= 200):
                    results = rmn.detect_emotion_for_single_frame(frame)

                for result in results:
                    emolabel = result['emo_label']
                    emoproba = result['emo_proba']

                # Compara se as emoções são iguais
                if (emoproba > 0.7 and emolabel == emo_p and current_time < 1000): # Se as expressões forem iguais e não tiver chegado em 10 segundos de captura

                    current_time = 0
                    start_time = time_as_int()

                    score += 1 # Aumenta 1 ponto
                    while current_time <= 500: # Timer de delay e update
                        event, values = janela2.read(timeout=1)
                        
                        if event == sg.WIN_CLOSED:
                            janela2.close()
                            sys.exit()
                        
                        current_time = time_as_int() - start_time

                        janela2['OutMestre'].update(
                            "Expressão Correta", text_color="white", font=("Poppins", 25, "bold"))
                        janela2['OutAluno'].update(
                            "Expressão Correta", text_color="#19D342", font=("Poppins", 25, "bold"))
                        janela2['scorenum'].update(value=score)

                    start_time = time_as_int()
                    break

                elif (current_time > 1000): # Caso o tempo passe de 10 segundos

                    current_time = 0
                    start_time = time_as_int()

                    while current_time <= 500: # Timer de delay e update
                        event, values = janela2.read(timeout=1)
                        
                        if event == sg.WIN_CLOSED:
                            janela2.close()
                            sys.exit()
                                    
                        current_time = time_as_int() - start_time

                        janela2['OutMestre'].update(
                            "Tempo Esgotado", text_color="white", font=("Poppins", 25, "bold"))
                        janela2['OutAluno'].update(
                            "Tempo Esgotado", text_color="#D4181A", font=("Poppins", 25, "bold"))

                    start_time = time_as_int()
                    break

            except Exception as err:
                print(err)
                continue
        vid1.release()
        janela2['camAluno'].update(filename="images/user.png")
        janela2['camMestre'].update(filename="images/teacher.png")
    janela2.close()
    janela6.close()
    return score

############################################# MENU #################################################33

# janela = janela_termos()
# event, values = janela.read() # Mostra a janela com os termos
# if event == sg.WIN_CLOSED:
#     janela.close()

# if event == "Sim":

while aux == False:

    # Chama as janelas
    aux_confirm = 0

    janela1 = janela_inicio()
    janela5 = janela_final_saida()

    # janela.close()
    event, values = janela1.read() # Mostra a janela do Menu

    if event == "Sair":
        event5, values5 = janela5.read() # Mostra a janela de confirmação de saida
        if event5 == "Sim":
            sys.exit()
        if event5 == "Não":
            janela5.close()
            janela1.close()
        if event5 == sg.WIN_CLOSED:
            janela5.close()
            janela1.close()

    if event == sg.WIN_CLOSED:
        aux = True
        sys.exit()

    if event == "Instruções":
        janela1.close()
        janela3 = janela_instruction() 
        event, values = janela3.read() # Nostra a janela com as Instruções
        if event == sg.WIN_CLOSED:
            janela3.close()
        if event == "Voltar":
            janela3.close()
    elif event == "Jogar":
        start_time = time_as_int()
        
        janela1.close()

        janela2 = janela_jogo()
        janela6 = janela_mestre()
        janela7 = janela_definicao()
        # janela8 = janela_carregamento()

        while aux_confirm == 0:

            event7, values7 = janela7.read(timeout=1) # Mostra a janela de definição do nome e número de fases 
            if event7 == sg.WIN_CLOSED:
                janela7.close()
                aux_confirm = 1
            if event7 == 'Jogar':
                nome = values7['nome']
                n = values7['nfases']

                # Impede do usuário iniciar o programa com um nome e um número de fases inválido

                if(n != ''):
                    if(int(n) > 0 and int(n) <= 10 and len(nome) > 0 and len(nome) <= 10): 
                        janela7.close()
                        
                        # Chama o jogo 
                        score = alunoRec(janela1, janela2, janela6, n, nome)
                        
                        # Retorna pro Menu
                        if score == -1:
                            break
                        else:

                            janela4 = janela_final()

                            while True:
                                event, values = janela4.read(timeout=10) # Mostra a janela final com os pontos

                                if score == 0:
                                    janela4['acertos'].update(filename="images/gameover.png")
                                    janela4['mensagem'].update(
                                        "Mais sorte na próxima!")
                                elif score <= int(n)/2:
                                    janela4['acertos'].update(filename="images/palmas.png")
                                    janela4['mensagem'].update("Quase lá, tente novamente!")
                                elif score == int(n):
                                    janela4['acertos'].update(filename="images/crown.png")
                                    janela4['mensagem'].update("Parabéns "+ nome +"!")

                                janela4['scorefinal'].update(score)

                                if event == sg.WIN_CLOSED:
                                    sys.exit()

                                if event == "Voltar":
                                    janela4.close()
                                    aux_confirm = 1
                                    break

                    else:
                        continue

            elif event7 == 'Voltar':
                janela7.close()
                break
                # continue

# elif event == 'Não':
#     janela.close()
cv2.destroyAllWindows()

