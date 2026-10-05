import tkinter as tk
from tkinter import simpledialog

def inserir_nome():
    nome_user = simpledialog.askstring("Inserir", "Digite o seu nome?")
    if nome_user:
        label_resultado.config(text=f"Bem-vindo, {nome_user}")
    else:
        label_resultado.config(text=f"Nenhum nome Inserido.")

janela = tk.Tk()
janela.title("Saudar")

button = tk.Button(janela, text="Inserir nome", command=inserir_nome)
button.pack(pady=20, padx=20)

label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=10)

janela.mainloop()

