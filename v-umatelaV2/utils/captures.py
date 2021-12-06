import cv2
import sys
import PySimpleGUI as sg
import numpy as np
import sys

from utils.functions import Functions
from rmn import RMN
from utils.sounds import Sounds
from utils.functions import Functions

fc = Functions()
rmn = RMN()
sons = Sounds()
som=True

class Mestre():

    def nextTurn(self, user, janela2, i, n, nome="aluno"):
        current_time = 0
        start_time = fc.time_as_int()

        if(user == "aluno"):                                 
            
            janela2['expressao'].update(" ") # Limpa o campo de 'Faca uma expressão'
            janela2['mestre'].update(text_color="black", font=(
                'Poppins', 30, "bold"))                       

            while current_time <= 500: # Timer de contagem (5 segundos)
            
                event, values = janela2.read(timeout=1)
                
                if event == sg.WIN_CLOSED:
                    janela2.close()
                    sys.exit()
                    
                janela2['contador'].update('{:02d}'.format( #Atualiza o tempo da Janela do Aluno
                    (current_time // 100) % 60))    
                janela2.find_element("stopwatch").UpdateAnimation("utils/images/cronometro.gif", time_between_frames=24)
                janela2['OutAluno'].update(" ", text_color="black", font=(
                    'Poppins', 20, "bold")) #
                janela2['expressao'].update(
                    "Atenção "+nome+", agora é a sua vez!", font=('Poppins', 28, "bold"))  

                current_time = fc.time_as_int() - start_time

            janela2['expressao'].update("Faça uma Expressão!", font=('Poppins', 28, "bold"))                    
            janela2['mestre'].update(text_color="black", font=('Poppins', 20, "bold"))                       

        elif(user == "mestre"):
            while current_time <= 500: # Timer de contagem (5 segundos)                                                                    # feito
                
                event2, values2 = janela2.read(timeout=1)
                # event, values = janela6.read(timeout=1)
                
                if event2 == sg.WIN_CLOSED:
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
                # janela2['fase'].update(str(fase_str))
                # janela2['fase'].update(str(fase_str))
            
                janela2['OutMestre'].update(" ")
                janela2['contador'].update('{:02d}'.format(
                    (current_time // 100) % 60)) 
                janela2.find_element("stopwatch").UpdateAnimation("utils/images/cronometro.gif", time_between_frames=24)
                janela2['expressao'].update(
                    "Atenção Mestre, é a sua vez!", font=('Poppins', 28, "bold"))  
                janela2['camMestre'].update(filename="utils/images/teacher.png")

                current_time = fc.time_as_int() - start_time
            
            janela2['expressao'].update("Mestre, faça uma Expressão!")
            janela2['mestre'].update(text_color="black", font=('Poppins', 20, "bold")) 

    def mestreCaptura(self, janela2, i, n, nome, neutral=0):  # Captura de tela do mestre
        vid = cv2.VideoCapture(0)
        maior = 0
        frame_dic = {}
        emotion = ""
        img_frame = ""
        emotions = []
        emocao = ""

        # "Atenção Mestre, é a sua vez!",
        self.nextTurn("mestre", janela2, i, n, nome)

        current_time = 0
        start_time = fc.time_as_int()

        while current_time <= 500:  # Timer 5 segundos de Captura das expressões do mestre
            event2, values2 = janela2.read(timeout=1)
            janela2['contador'].update('{:02d}.{:02d}'.format(
                (current_time // 100) % 60, current_time % 100))
            janela2.find_element("stopwatch").UpdateAnimation("utils/images/cronometro.gif", time_between_frames=24)

            ret, frame_cap = vid.read()

            if frame_cap is None or ret is not True:
                continue

            try:
                # sound.clock(som)
                if event2 == sg.WIN_CLOSED:
                    vid.release()
                    janela2.close()
                    sys.exit()

                emoproba = 0
                emolabelProf = ""

                current_time = fc.time_as_int() - start_time

                frame_cap = np.fliplr(frame_cap).astype(np.uint8)
                resultsProf = rmn.detect_emotion_for_single_frame(frame_cap)

                # Captura de emoções

                for resultProf in resultsProf:
                    emolabelProf = resultProf['emo_label']
                    emoproba = resultProf['emo_proba']

                    emocao = fc.translateEmo(emolabelProf) # Traduz o emolabel

                    janela2['OutMestre'].update(
                        emocao,  text_color="black", font=("Poppins", 25, "bold"))

                # Capta as expressões diferentes de neutro e com 70% do emoproba
                if(emoproba > 0.7 and emolabelProf != "neutral"):
                    emotions.append(emolabelProf)

                    # Se o emolabel for diferente de todas as keys, incrementa no frame_dic
                    if(emolabelProf != key for key in frame_dic):
                        frame_dic[emolabelProf] = frame_cap

                imgbytes = cv2.imencode('.png', frame_cap)[1].tobytes()
                janela2['camMestre'].update(data=imgbytes)

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
            start_time = fc.time_as_int()

            while current_time <= 300: # Timer de delay e update
                event, values = janela2.read(timeout=1)
                
                if event == sg.WIN_CLOSED:
                    janela2.close()
                    sys.exit()
                
                janela2['camMestre'].update(filename="utils/images/teacher.png")
                janela2['OutMestre'].update(
                    "Tente Novamente", text_color="#D4181A", font=("Poppins", 25, "bold"))
                current_time = fc.time_as_int() - start_time

            start_time = fc.time_as_int()
            vid.release() # Interrompe a captura do RMN
            emotion = fc.mestreCaptura(janela2, i, n, nome, neutral)

        emocao = fc.translateEmo(emotion)

        janela2['OutMestre'].update(
            emocao, text_color="black", font=("Poppins", 25, "bold"))

        # Função que capta o frame de acordo com expressão de maior frequência
        for key in frame_dic:   # Guarda a imagem do mestre
            if key == emotion:
                img_frame = cv2.imencode('.png', frame_dic[key])[1].tobytes()
                janela2['camMestre'].update(data=img_frame)

        vid.release()
        return emotion
    
     

class AlunoTEA(Mestre):
    
    def alunoCaptura(self, janela1, janela2, n, nome, tempo):  # Captura as expressôes do Aluno
        janela1.close()
        score = 0
        tempoAcertos = []
        listEmo = []

        for i in range(int(n)): # Fases do jogo
            results = []
            result = {}

            emo_p = self.mestreCaptura(janela2, i, n, nome) # Chama a captura do mestre 
            listEmo.append(fc.translateEmo(emo_p))
            # Caso só tenha sido gerado neutro ele retorna -1 para retornar ao menu
            if(emo_p == -1):
                janela2.close()
                return -1

            vid1 = cv2.VideoCapture(0)

            # "Atenção Aluno, é a sua vez!"
            self.nextTurn("aluno", janela2, i, n, nome)

            current_time = 0
            start_time = fc.time_as_int()
            sons.clock(som)
            # Captura e comparação de expressôes do Aluno com o mestre
            while True:
                ret, frame = vid1.read()
                if frame is None or ret is not True:
                    continue

                event, values = janela2.read(timeout=1)
                if event == sg.WIN_CLOSED:
                    vid1.release()
                    janela2.close()
                    sys.exit()
                    
                janela2['aluno'].update(
                    text_color="black", font=('Poppins', 20, "bold"))

                try:
                    emoproba = 0
                    emolabel = ""

                    # Update na tela dos frames da Webcam
                    frame = np.fliplr(frame).astype(np.uint8)
                    imgbytes = cv2.imencode('.png', frame)[1].tobytes()
                    janela2['camAluno'].update(data=imgbytes)
                    janela2['contador'].update('{:02d}.{:02d}'.format(
                        (current_time // 100) % 60, current_time % 100))
                    janela2.find_element("stopwatch").UpdateAnimation("./utils/images/cronometro.gif", time_between_frames=24)
                    

                    # Começa a captura das expressões depois de 2 segundos
                    current_time = fc.time_as_int() - start_time
                    if(current_time >= 200):
                        results = rmn.detect_emotion_for_single_frame(frame)

                    for result in results:
                        emolabel = result['emo_label']
                        emoproba = result['emo_proba']

                    # Compara se as emoções são iguais
                    if (emoproba > 0.7 and emolabel == emo_p and current_time < tempo):
                        sons.clocknot()
                        sons.expcorreta(som)
                        # Se as expressões forem iguais e não tiver chegado em 10 segundos de captura
                        tempoAcertos.append(str(current_time/100)+"s")
                        current_time = 0
                        start_time = fc.time_as_int()

                        score += 1 # Aumenta 1 ponto
                        while current_time <= 500: # Timer de delay e update
                            event, values = janela2.read(timeout=1)
                            
                            if event == sg.WIN_CLOSED:
                                janela2.close()
                                sys.exit()
                            
                            current_time = fc.time_as_int() - start_time
                            
                            # janela2.find_element("camAluno").UpdateAnimation("./images/win.gif", time_between_frames=100)
                            janela2['OutMestre'].update(
                                "Expressão Correta", text_color="white", font=("Poppins", 25, "bold"))
                            janela2['OutAluno'].update(
                                "Expressão Correta", text_color="#19D342", font=("Poppins", 25, "bold"))
                            janela2['scorenum'].update(value=score)

                        start_time = fc.time_as_int()
                        break

                    elif (current_time > tempo): # Caso o tempo passe de 10 segundos
                        sons.clocknot()
                        sons.gameOver(som)
                        tempoAcertos.append("NÃO ACERTOU")

                        current_time = 0
                        start_time = fc.time_as_int()

                        while current_time <= 500: # Timer de delay e update
                            event, values = janela2.read(timeout=1)
                            
                            if event == sg.WIN_CLOSED:
                                janela2.close()
                                sys.exit()
                                        
                            current_time = fc.time_as_int() - start_time

                            janela2['OutMestre'].update(
                                "Tempo Esgotado", text_color="white", font=("Poppins", 25, "bold"))
                            janela2['OutAluno'].update(
                                "Tempo Esgotado", text_color="#D4181A", font=("Poppins", 25, "bold"))

                        start_time = fc.time_as_int()
                        break

                except Exception as err:
                    print(err)
                    continue
            vid1.release()
            janela2['camAluno'].update(filename="utils/images/user.png")
            janela2['camMestre'].update(filename="utils/images/teacher.png")
        janela2.close()
        
        return score, tempoAcertos, listEmo
        
    