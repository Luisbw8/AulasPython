import tkinter as tk
from tkinter import simpledialog

def calcular_media():
    n1 = simpledialog.askfloat("primeiro numero","Insira o primeiro numero")
    n2 = simpledialog.askfloat("Segundo numero","Insira o segundo numero")

    media = (n1+n2)/2

    label_resultado.config(text=f"A média de {n1} e {n2} é igual á {media}")

janela = tk.Tk()
janela.title("Calcular Média")

button = tk.Button(janela, text="Calcular Média dos dois Números ", command=calcular_media)
button.pack(pady=20)

label_resultado = tk.Label(janela, text="")
label_resultado.pack(padx=20, pady=20)

janela.mainloop()