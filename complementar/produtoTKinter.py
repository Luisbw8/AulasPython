import tkinter as tk
from tkinter import simpledialog

def calcular_media():
    nome_product = simpledialog.askstring("Nome do Produto","Insira o nome do produto")
    price_product = simpledialog.askfloat("preço do Produto","Insira o preço do produto")

    

    label_resultado.config(text=f"A média de {n1} e {n2} é igual á {media}")

janela = tk.Tk()
janela.title("Calcular Produto")

button = tk.Button(janela, text="Calcular", command=calcular_media)
button.pack(pady=20)

label_resultado = tk.Label(janela, text="")
label_resultado.pack(padx=20, pady=20)

janela.mainloop()