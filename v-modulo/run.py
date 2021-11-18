import cv2
import time
import glob
import sys
import numpy as np
import PySimpleGUI as sg
from rmn import RMN
from wintest import Windows
from gamemode import SinglePlayer, MultiPlayer

janela = Windows()
singleP = SinglePlayer()
singleP.storeExpressions()

def time_as_int():
    return int(round(time.time() * 100))

current_time = 0 #Tempo
aux = False # Auxiliar while
aux_confirm = 0 # Auxiliar do segundo while
score = 0 # Pontuação

while aux == False:

    # Chama as janelas
    aux_confirm = 0

    janela1 = janela.janela_inicio()
    janela5 = janela.janela_final_saida()
    
    # janelaT.close()
    event, values = janela1.read() # Mostra a janela do Menu

    if event == "Sair":
        event5, values5 = janela5.read() # Mostra a janela de confirmação de saida
        if event5 == "Sim":
            aux = True
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
        janela3 = janela.janela_instruction() 
        event, values = janela3.read() # Mostra a janela com as Instruções
        if event == "Voltar":
            janela3.close()
    elif event == "Individual":
        start_time = time_as_int()
        
        janela1.close()

        janela2 = janela.janela_jogoSP()
        janela7 = janela.janela_definicaoSP()

        while aux_confirm == 0:

            event7, values7 = janela7.read(timeout=1) # Mostra a janela de definição do nome e número de fases 
            if event7 == sg.WIN_CLOSED:
                janela7.close()
                aux_confirm = 1
            if event7 == 'Jogar':
                # Impede do usuário iniciar o programa com um nome e um número de fases inválido

                nome = values7['nome']

                if(len(nome) > 0 and len(nome) <= 9):
                    janela7.close()

                    janela7.close()
                    
                    # Chama o jogo 
                    singleP = SinglePlayer()
                    score = singleP.jogo(janela1, janela2, nome)
                    print(score)
                    list = singleP.retornaList()
                    # Retorna pro Menu
                    if score == -1:
                        break
                    else:
                        
                        janela4 = janela.janela_final()

                        while True:
                            event, values = janela4.read(timeout=1) # Mostra a janela final com os pontos

                            if score == 0:
                                janela4['mensagem'].update(
                                    "Mais sorte na próxima!")
                            elif score <= int(len(list))/2:
                                janela4['mensagem'].update("Quase lá, tente novamente!")
                            elif score == int(len(list)):
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
    elif event == 'Multijogador':
        
            start_time = time_as_int()
            
            janela1.close()

            janela2 = janela.janela_jogoMP()
            janela6 = janela.janela_mestre()
            janela7 = janela.janela_definicaoMP()

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
                            multiP = MultiPlayer()
                            score = multiP.alunoRec(janela1, janela2, janela6, n, nome)
                            
                            # Retorna pro Menu
                            if score == -1:
                                break
                            else:

                                janela4 = janela.janela_final()

                                while True:
                                    event, values = janela4.read(timeout=1) # Mostra a janela final com os pontos

                                    if score == 0:
                                        janela4['acertos'].update(filename="images.utils/gameover.png")
                                        janela4['mensagem'].update(
                                            "Mais sorte na próxima!")
                                    elif score <= int(n)/2:
                                        janela4['acertos'].update(filename="images.utils/palmas.png")
                                        janela4['mensagem'].update("Quase lá, tente novamente!")
                                    elif score == int(n):
                                        janela4['acertos'].update(filename="images.utils/crown.png")
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
#     janelaT.close()
cv2.destroyAllWindows()