import tkinter as tk
from tkinter import simpledialog

def pedir_nome():
    nome_usuario = simpledialog.askstring("Entrada", "Digite o seu nome:")
    
    # 2. Verifica se o usuário não cancelou e mostra na tela
    if nome_usuario:
        label_resultado.config(text=f"Bem-vindo, {nome_usuario}!")
    else:
        label_resultado.config(text="Nenhum nome foi digitado.")

# Configuração da janela principal
root = tk.Tk()
root.title("Exemplo Tkinter")

# Botão para abrir a caixa de diálogo
botao = tk.Button(root, text="Digitar Nome", command=pedir_nome)
botao.pack(pady=20)

# Componente Label que começará vazio e depois mostrará a variável
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)

root.mainloop()
