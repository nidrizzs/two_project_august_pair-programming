'''
abala ascii,
A Tabela ASCII (American Standard Code for Information Interchange) é 
como um "dicionário" que os computadores usam para entender letras, números e símbolos.
Como os computadores só entendem números (código binário: 0s e 1s), a Tabela ASCII atribui 
um número específico para cada caractere.

Tabela hexadecimal
Tabela Hexadecimal (ou tabela de base 16) é um sistema de
numeração muito usado na computação para representar números binários 
(0s e 1s) de uma forma muito mais curta e fácil de ler para nós, humanos.
'''

import random
import string

def gerar_senhas(tamanho):
    senha_caracteres = string.ascii_letters + string.digits + string.punctuation

    senha_gerada = ''.join(
         random.choice(senha_caracteres)for _ in range
         (tamanho)
    )
    return senha_gerada
senha_usuario = gerar_senhas(12)
print(f'sua senha gerada, será:{senha_usuario}')

if __name__ == "__main__":

    import random
import string
import tkinter as tk
from tkinter import messagebox

# ==========================================
# CONSTANTES DE CORES (Sua Paleta)
# ==========================================
COLOR_AZUL_ESC = "#004d6e"  # Fundo da tela
COLOR_AZUL_MED = "#0081ab"  # Bordas e detalhes
COLOR_AZUL_CLA = "#00b1cd"  # Destaque da senha
COLOR_VERDE    = "#a6c844"  # Botão Gerar
COLOR_ROSA     = "#b83764"  # Alertas de erro
COLOR_AMARELO  = "#edce01"  # Botão Copiar
COLOR_ACO      = "#4a3336"  # Fundo dos cards/campos

# ==========================================
# LÓGICA DO PROGRAMA
# ==========================================
def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho <= 0:
            raise ValueError
        
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        
        # Atualiza o campo de texto da senha
        var_senha.set(senha)
    except ValueError:
        messagebox.showerror(
            "Erro de Entrada", 
            "Por favor, insira um número inteiro válido maior que 0!"
        )

def copiar_senha():
    senha = var_senha.get()
    if senha and senha != "Clique em Gerar":
        # Limpa o clipboard e adiciona a nova senha
        janela.clipboard_clear()
        janela.clipboard_append(senha)
        messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência!")
    else:
        messagebox.showwarning("Atenção", "Nenhuma senha foi gerada para copiar.")

# ==========================================
# INTERFACE GRÁFICA (Tkinter)
# ==========================================
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("400x320")
janela.config(bg=COLOR_AZUL_ESC)
janela.resizable(False, False)

# Título
label_titulo = tk.Label(
    janela, 
    text="🍕Gerador de Senhas🍕", 
    font=("Helvetica", 16, "bold"), 
    bg=COLOR_AZUL_ESC, 
    fg="white"
)
label_titulo.pack(pady=15)

# Container Principal (Card)
card = tk.Frame(janela, bg=COLOR_ACO, bd=2, relief="solid")
card.pack(padx=20, pady=10, fill="both", expand=True)

# Campo: Tamanho da Senha
frame_input = tk.Frame(card, bg=COLOR_ACO)
frame_input.pack(pady=10)

label_tamanho = tk.Label(
    frame_input, 
    text="Tamanho da senha:", 
    font=("Helvetica", 10, "bold"), 
    bg=COLOR_ACO, 
    fg="white"
)
label_tamanho.pack(side="left", padx=5)

entry_tamanho = tk.Entry(
    frame_input, 
    width=5, 
    font=("Helvetica", 10), 
    justify="center",
    bd=2
)
entry_tamanho.insert(0, "12")  # Valor padrão
entry_tamanho.pack(side="left", padx=5)

# Campo: Exibição da Senha Gerada
var_senha = tk.StringVar(value="Clique em Gerar")
label_senha = tk.Label(
    card, 
    textvariable=var_senha, 
    font=("Consolas", 12, "bold"), 
    bg=COLOR_AZUL_ESC, 
    fg=COLOR_AZUL_CLA, 
    width=28, 
    pady=8,
    relief="sunken"
)
label_senha.pack(pady=10)

# Botão: Gerar Senha
btn_gerar = tk.Button(
    card, 
    text="GERAR SENHA", 
    command=gerar_senha, 
    bg=COLOR_VERDE, 
    fg="black", 
    font=("Helvetica", 10, "bold"),
    cursor="hand2",
    activebackground=COLOR_AZUL_MED
)
btn_gerar.pack(fill="x", padx=20, pady=5)

# Botão: Copiar Senha
btn_copiar = tk.Button(
    card, 
    text="COPIAR", 
    command=copiar_senha, 
    bg=COLOR_AMARELO, 
    fg="black", 
    font=("Helvetica", 9, "bold"),
    cursor="hand2"
)
btn_copiar.pack(fill="x", padx=20, pady=5)

# Execução do App
if __name__ == "__main__":
    janela.mainloop()