#importação da biblioteca tkinter
import tkinter as tk

#Função para executar quando o botão for clicado
def mudar_pagina():
    mensagem_label.config(text="Seja Bem-Vindo(A)")


#Criação da Janela 
janela = tk.Tk()
janela.title("Interface de Entrada") #Adiciona um titulo a Interface 

#Cria um rotulo para criar uma mensagem
mensagem_label = tk.Label(janela, text="Introdução a Interface")
mensagem_label.pack(padx=20, pady=20) #Adiciona o Rotulo na interface

#Criação do Botão
buttom = tk.Button(janela, text="Clique aqui", command=mudar_pagina)
buttom.pack(padx=20, pady=20) #Adiciona o botão na interface



#Loop para a Janela
janela.mainloop()