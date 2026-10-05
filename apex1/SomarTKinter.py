import tkinter as tk
from tkinter import simpledialog

def calcular_soma():
    n1 = simpledialog.askinteger("primeiro numero","Insira o primeiro numero")
    n2 = simpledialog.askinteger("Segundo numero","Insira o segundo numero")

    soma = n1 + n2
    label_resultado.config(text=f"A soma de {n1} e {n2} é igual á {soma}")

janela = tk.Tk()
janela.title("Calcular Soma")

button = tk.Button(janela, text="Somar Dois Números ", command=calcular_soma)
button.pack(pady=20)

label_resultado = tk.Label(janela, text="")
label_resultado.pack(padx=20, pady=20)

janela.mainloop()