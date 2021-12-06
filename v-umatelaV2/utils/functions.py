import time
import PySimpleGUI as sg
import utils.layouts as ui

from utils.sounds import Sounds
from Dao import Aluno

janelas = ui.Janelas()
sons = Sounds()
alunos = Aluno()
som=True

#######################################################FUNÇÕES DE CADASTRO DO ALUNO#############################################

class Functions():
    def cadastrar(self, janela1):
        janela_cad = janelas.janela_cadastrar()
        janela1.close()
        
        while True:
            event, values = janela_cad.read()
            if event == sg.WIN_CLOSED:
                janela_cad.close()
                break
            if event == "salvar":
                sons.menu(som)
                if values['nome'] == "":
                    janela_cad['erro'].update("Informe um nome")
                elif values['idade'] == "":
                    janela_cad['erro'].update("Informe uma idade")
                elif any(chr.isdigit() for chr in values['idade']) == False:
                    janela_cad['erro'].update("A idade deve ser um número")
                elif values['sexo'] == "":
                    janela_cad['erro'].update("Informe o sexo do Aluno")
                elif values['grau'] == "":
                    janela_cad['erro'].update("Informe um grau de dificuldade do Aluno")
                else:
                    aluno = Aluno(values['nome'], values['idade'], values['sexo'], values['grau'])
                    
                    if aluno.aluno_exists(values['nome']) == False:
                        janela_cad['erro'].update("Esse aluno já está Cadastrado")
                    else:
                        aluno = Aluno(values['nome'], values['idade'], values['sexo'], values['grau'])
                        
                        aluno.insert_table()
                        aluno.create_archive()
                    
                        janela_cad.close()
                        break
            if event == "voltar":
                sons.menu(som)
                janela_cad.close()
                break

    def editar(self, janela1, aluno):
    
        janela_edit = janelas.janela_editar(aluno.nome,aluno.idade,aluno.sexo,aluno.grau)
        janela1.close()
        
        while True:
            event, values = janela_edit.read()
            if event == sg.WIN_CLOSED:
                janela_edit.close()
                break
            if event == "editar":
                if values['nome'] == "":
                    janela_edit['erro'].update("Informe um nome")
                elif values['idade'] == "":
                    janela_edit['erro'].update("Informe uma idade")
                elif any(chr.isdigit() for chr in values['idade']) == False:
                    janela_edit['erro'].update("A idade tem que ser um número")
                elif values['sexo'] == "":
                    janela_edit['erro'].update("Informe o sexo do Aluno")
                elif values['grau'] == "":
                    janela_edit['erro'].update("Informe o grau de dificuldade do Aluno")
                else:
                    alunoedit = Aluno(values['nome'], values['idade'], values['sexo'], values['grau'], aluno.id)
                    if alunoedit.aluno_exists(values['nome']) == False:
                        janela_edit['erro'].update("Esse aluno já está Cadastrado")
                    else:
                        alunoedit.update_aluno()
                        aluno.del_archive()
                        alunoedit.create_archive()
                        
                        janela_edit.close()
                        break
            if event == "voltar":
                janela_edit.close()
                break

    def mostrar(self, list_alunos):  
        data = []
        list_alunos = alunos.list_alunos()
        
        for aluno in list_alunos:
            data.append([aluno.nome,aluno.idade,aluno.sexo,aluno.grau])
        return data, list_alunos

    ############################################################################################################################################
    
    def translateEmo(self, emolabel):  # Traduz o emolabel para o 'OutMestre' da JANELA2
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

    def time_as_int(self): #Funcao do tempo do Jogo
        return int(round(time.time() * 100))