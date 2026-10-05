import tkinter as tk
from tkinter import simpledialog

def calcular_aprovacao():
    n1 = simpledialog.askfloat("primeira nota","Insira a primeira nota")
    n2 = simpledialog.askfloat("Segunda nota","Insira a segunda nota")

    media = (n1+n2)/2
    if (media <6):
        label_resultado.config(text=f"Aluno Reprovado! \n Média: {media}")
    else:
        label_resultado.config(text=f"Aluno Aprovado!! \n Média: {media}")    

janela = tk.Tk()
janela.title("Verificar Aprovação")

button = tk.Button(janela, text="Verificar", command=calcular_aprovacao)
button.pack(pady=20)

label_resultado = tk.Label(janela, text="")
label_resultado.pack(padx=20, pady=20)

janela.mainloop()