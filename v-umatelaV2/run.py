import cv2
import sys
import numpy as np
import PySimpleGUI as sg
import utils.layouts as ui
import utils.functions as fc

from utils.captures import Mestre, AlunoTEA 
from utils.sounds import Sounds
from rmn import RMN
from utils.Dao import Aluno

func_alun = AlunoTEA()
janelas = ui.Janelas()
functions = fc.Functions()
rmn = RMN()
sound = Sounds()

def main():
    aux = False # Auxiliar while
    som = True
    score = 0 # Pontuação
    current_time = 0 #Tempo
    aux_confirm = 0 # Auxiliar do segundo while       

    while aux == False:

        # Chama as janelas
        aux_confirm = 0

        janela1 = janelas.janela_inicio()
        janela5 = janelas.janela_final_saida()

        event, values = janela1.read() # Mostra a janela do Menu
        if event == sg.WIN_CLOSED:
            aux = True
            sys.exit()
        
        if event == "som":
            som = not som
            janela1.close()

        if event == "Sair":
            sound.menu(som)
            event5, values5 = janela5.read() # Mostra a janela de confirmação de saida
            if event5 == "Sim":
                sound.menu(som)
                sys.exit()
            if event5 == "Não":
                sound.voltar(som)
                janela5.close()
                janela1.close()
            if event5 == sg.WIN_CLOSED:
                janela5.close()
                janela1.close()


        if event == "Instruções":
            sound.menu(som)
            janela1.close()
            janela3 = janelas.janela_instruction() 
            event, values = janela3.read() # Mostra a janela com as Instruções
            if event == sg.WIN_CLOSED:
                janela3.close()
            if event == "Voltar":
                sound.voltar(som)
                janela3.close()
        elif event == "Aluno":
            sound.menu(som)
        
            janela1.close()
            
            alunos = Aluno()
            data, list_alunos = functions.mostrar(alunos)
            if len(data) > 0:
                janela_area_aluno = janelas.janela_aluno(data)

                while True:
                    event, values = janela_area_aluno.read()
            
                    if event == sg.WIN_CLOSED:
                        janela_area_aluno.close()
                        break
                    elif event == "voltar":
                        sound.voltar(som)
                        janela_area_aluno.close()
                        break
                    elif event == "cadastrar":
                        sound.menu(som)  
                        functions.cadastrar(janela_area_aluno)
                    
                    elif event == "editar":
                        sound.menu(som)
                        select = values['table']
                        if len(select) > 0:
                            functions.editar(janela_area_aluno, list_alunos[int(select[0])])
                    
                    elif event == "remover":
                        sound.menu(som)
                        select = values['table']
                        if len(select) > 0:
                            alunoArq = alunos.select_aluno(list_alunos[int(select[0])].id)
                            alunoArq.del_alunos()
                            alunoArq.del_archive()

                        data, list_alunos = functions.mostrar(alunos)
                        janela_area_aluno['table'].update(values=data)
                    
                    elif event == "pdf":
                        sound.menu(som)
                        select = values['table']
                        if len(select) > 0:
                            alunoPDF = alunos.select_aluno(list_alunos[int(select[0])].id)
                            alunoPDF.text_to_pdf()

            else:
                functions.cadastrar(janela1)
                    
        elif event == "Jogar":
            sound.menu(som)

            start_time = functions.time_as_int()
            
            janela1.close()
            alunos = Aluno()
            list_nome = alunos.list_nome_alunos()
        
            if not list_nome:
                functions.cadastrar(janela1)
            else: 
                
                janela2 = janelas.janela_jogo()
                janela7 = janelas.janela_definicao(list_nome)
                # janela8 = janela_carregamento()
        
                while aux_confirm == 0:
                    
                    event7, values7 = janela7.read(timeout=1) # Mostra a janela de definição do nome e número de fases 
                    
                    if event7 == sg.WIN_CLOSED:
                        janela7.close()
                        aux_confirm = 1
                    if event7 == 'Jogar':
                        sound.menu(som)
                            
                        nome = values7['nome']
                        n = values7['nfases']
                        tempo = values7['tempo']
                        # Impede do usuário iniciar o programa com um nome e um número de fases inválido

                        if(n != ''):
                            if(int(n) > 0 and int(n) <= 10 and len(nome) > 0 and len(tempo) > 0): 
                                janela7.close()
                                tempo = int(tempo)*100
                                # Chama o jogo 
                                score, tempoAcertos, listEmo = func_alun.alunoCaptura(janela1, janela2, n, nome, tempo)
                                
                                # Retorna pro Menu
                                if score == -1:
                                    break
                                else:

                                    janela4 = janelas.janela_final()

                                    while True:
                                        event, values = janela4.read(timeout=10) # Mostra a janela final com os pontos

                                        if score == 0:
                                            janela4['acertos'].update(filename="utils/images/gameover.png")
                                            janela4['mensagem'].update(
                                                "Mais sorte na próxima!")
                                        elif score <= int(n)/2:
                                            janela4['acertos'].update(filename="utils/images/palmas.png")
                                            janela4['mensagem'].update("Quase lá, tente novamente!")
                                        elif score == int(n):
                                            janela4['acertos'].update(filename="utils/images/crown.png")
                                            janela4['mensagem'].update("Parabéns "+ nome +"!")

                                        janela4['scorefinal'].update(score)

                                        if event == sg.WIN_CLOSED:
                                            alunoArq = alunos.select_aluno_by_name(nome)
                                            alunoArq.save_aluno_relatory(int(n),score,tempoAcertos,listEmo)
                                            sys.exit()

                                        if event == "Voltar":
                                            sound.menu(som)

                                            janela4.close()
                                            alunoArq = alunos.select_aluno_by_name(nome)
                                            alunoArq.save_aluno_relatory(int(n),score,tempoAcertos,listEmo)
                                            aux_confirm = 1
                                            break

                            else:
                                continue

                    elif event7 == 'Voltar':
                        sound.voltar(som)
                        janela7.close()
                        break
                        # continue
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()