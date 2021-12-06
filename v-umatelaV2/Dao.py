import sqlite3
import os
from datetime import datetime
import textwrap
from fpdf import FPDF

class Aluno:
    def __init__(self, nome="", idade="", sexo="", grau="",id=0):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.grau = grau
        self.create_table()
    
    def create_table(self):
        conn = sqlite3.connect('somare')
        c = conn.cursor()
        
        c.execute(""" CREATE TABLE IF NOT EXISTS aluno ( 
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome TEXT NOT NULL,
                  idade INTEGER NOT NULL,
                  sexo TEXT NOT NULL,
                  grau TEXT NOT NULL
            )""")
        
        conn.commit()
        conn.close()
        
    def insert_table(self):
        conn = sqlite3.connect('somare')
        c = conn.cursor()
        
        c.execute("""INSERT INTO aluno
                  (nome, idade, sexo, grau)
                  VALUES (?,?,?,?)
                  """, (self.nome, self.idade, self.sexo, self.grau))
        
        conn.commit()
        conn.close()
        
    def create_archive(self):
        arq = open("./logs/"+self.nome+".txt", 'w')
        
        arq.write("----------------------------------------------------- \n")
        arq.write("|                     Relatório                     | \n")
        arq.write("----------------------------------------------------- \n")
        arq.write("     Aluno: "+self.nome+"  -  Idade: "+str(self.idade)+"\n")
        arq.write("     Sexo: "+self.sexo+"  -  Grau: "+self.grau+     "\n")
        arq.write("-----------------------------------------------------\n")     
        
        arq.close()
        
        
    def list_nome_alunos(self):
        conn = sqlite3.connect('somare')
        c = conn.cursor()
        
        c.execute("""SELECT nome FROM aluno""")
        results = c.fetchall()

        list_alunos = []
        
        for result in results:
            list_alunos.append(result[0])
            
        conn.commit()
        conn.close()
        
        return list_alunos
    
    def list_alunos(self):
        conn = sqlite3.connect('somare')
        c = conn.cursor()
        
        c.execute("""SELECT * FROM aluno""")
        results = c.fetchall()

        list_alunos = []
        
        for result in results:
            aluno = Aluno(result[1],result[2],result[3],result[4],result[0])
            list_alunos.append(aluno)
            
        conn.commit()
        conn.close()
        
        return list_alunos
    
    def update_aluno(self):
        
        conn = sqlite3.connect('somare')
        c = conn.cursor()
        
        c.execute("""UPDATE aluno SET nome=?, idade=?, sexo=?, grau=? WHERE id=?""",(self.nome,self.idade,self.sexo,self.grau,self.id))
        
        conn.commit()
        conn.close()
    
    def del_alunos(self):
        conn = sqlite3.connect('somare')
        c = conn.cursor()
        
        c.execute("DELETE FROM aluno WHERE id = "+str(self.id))
        
        conn.commit()
        conn.close()
            
    def select_aluno(self, id):
        conn = sqlite3.connect('somare')
        c = conn.cursor()
        
        c.execute("SELECT * FROM aluno WHERE id = "+str(id))
        results = c.fetchall()
        
        aluno = Aluno(results[0][1],results[0][2],results[0][3],results[0][4],results[0][0])

        conn.commit()
        conn.close()
        
        return aluno
    
    def select_aluno_by_name(self, nome):
        conn = sqlite3.connect('somare')
        c = conn.cursor()
        
        c.execute("SELECT * FROM aluno WHERE nome = '"+nome+"'")
        results = c.fetchall()
        
        aluno = Aluno(results[0][1],results[0][2],results[0][3],results[0][4],results[0][0])

        conn.commit()
        conn.close()
    
        return aluno
    
    def aluno_exists(self, nome):
        conn = sqlite3.connect('somare')
        c = conn.cursor()
        
        c.execute("SELECT * FROM aluno WHERE nome = '"+nome+"'")
        results = c.fetchall()
        
        if len(results) > 0 and results[0][0] != self.id:
            return False
        else:
            return True

    def del_archive(self):
        if os.path.exists("./logs/"+self.nome+".txt"):
            os.remove("./logs/"+self.nome+".txt")
            
    def save_aluno_relatory(self,rodadas,acertos,tempo,emocoes):
            
        date = datetime.now()
        dateStr = date.strftime("%d/%m/%Y")
        hoursStr = date.strftime("%H:%M")
        arq = open("./logs/"+self.nome+".txt", 'a')
        
        arq.write("\n")
        arq.write("----------------------------------------------------- \n")
        arq.write("                  "+self.nome+" Jogou                 \n")
        arq.write("----------------------------------------------------- \n")
        arq.write("     Data: "+dateStr+"  -  Horário: "+hoursStr+      "\n")
        arq.write("\n")
        arq.write("     Rodadas: "+str(rodadas)+"  -  Total Acertos: "+str(acertos)+"\n")
        arq.write("\n") 
        arq.write("\n")
        for i in range(rodadas):
            arq.write("     Rodada "+str(i+1)+":  Tempo: "+str(tempo[i])+" \n")
            arq.write("                Emoção: "+emocoes[i]+" \n")

        arq.write("----------------------------------------------------- \n")     
        
        arq.close()

    def text_to_pdf(self):
        file = open("./logs/"+self.nome+'.txt')
        text = file.read()
        file.close()
        a4_width_mm = 210
        pt_to_mm = 0.35
        fontsize_pt = 15
        fontsize_mm = fontsize_pt * pt_to_mm
        margin_bottom_mm = 10
        character_width_mm = 7 * pt_to_mm
        width_text = a4_width_mm / character_width_mm

        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.set_auto_page_break(True, margin=margin_bottom_mm)
        pdf.add_page()
        pdf.set_font(family='Courier', size=fontsize_pt)
        splitted = text.split('\n')

        for line in splitted:
            lines = textwrap.wrap(line, width_text)

            if len(lines) == 0:
                pdf.ln()

            for wrap in lines:
                pdf.cell(0, fontsize_mm, wrap, ln=1)

        pdf.output("./Relatórios/"+self.nome+'.pdf', 'F')