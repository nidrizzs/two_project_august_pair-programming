import tkinter as tk
from tkinter import messagebox

class BancoVisual:
    def __init__(self, root):
        self.root = root
        self.root.title("Banco Visual - Nycollas")
        self.root.geometry("380x520")
        
        # 🎨 Definindo as cores da paleta (Bege e Vermelho)
        self.cor_fundo = "#5A7A8A"      # Bege claro
        self.cor_titulo = "#780000"     # Vermelho vinho
        self.cor_destaque = "#64090F"   # Vermelho carmim
        self.cor_botao_dep = "#803A25" # Bege escuro / Dourado
        self.cor_texto = "#2B2D42"      # Escuro para contraste

        self.root.configure(bg=self.cor_fundo)
        self.saldo = 1000.0  # Saldo inicial

        # 🏦 Título
        self.lbl_titulo = tk.Label(
            root, 
            text="Banco Digital", 
            font=("Arial", 18, "bold"), 
            bg=self.cor_fundo, 
            fg=self.cor_titulo
        )
        self.lbl_titulo.pack(pady=10)

        # 🖼️ Imagem do Caixa Eletrônico
        # Certifique-se de ter um arquivo 'caixa_eletronico.png' na mesma pasta do código
        try:
            self.img_atm = tk.PhotoImage(file="caixa_eletronico.png")
            self.lbl_imagem = tk.Label(root, image=self.img_atm, bg=self.cor_fundo)
            self.lbl_imagem.pack(pady=5)
        except tk.TclError:
            # Caso a imagem não esteja na pasta, exibe um aviso simples sem fechar o programa
            self.lbl_imagem = tk.Label(
                root, 
                text="[ 🏦 Caixa Eletrônico ]", 
                font=("Arial", 10, "italic"), 
                bg=self.cor_fundo, 
                fg=self.cor_titulo
            )
            self.lbl_imagem.pack(pady=5)

        # 💵 Exibição do Saldo
        self.lbl_saldo = tk.Label(
            root, 
            text=f"Saldo: R$ {self.saldo:.2f}", 
            font=("Arial", 14, "bold"), 
            bg=self.cor_fundo, 
            fg=self.cor_destaque
        )
        self.lbl_saldo.pack(pady=10)

        # ✏️ Campo de Entrada
        self.lbl_instrucao = tk.Label(
            root, 
            text="Digite o valor:", 
            font=("Arial", 10), 
            bg=self.cor_fundo, 
            fg=self.cor_texto
        )
        self.lbl_instrucao.pack(pady=5)
        
        self.txt_valor = tk.Entry(root, font=("Arial", 12), justify="center")
        self.txt_valor.pack(pady=5)

        # 🔘 Botões
        self.btn_depositar = tk.Button(
            root, 
            text="Depositar", 
            font=("Arial", 10, "bold"), 
            bg=self.cor_botao_dep, 
            fg="white", 
            width=15, 
            command=self.depositar
        )
        self.btn_depositar.pack(pady=5)

        self.btn_sacar = tk.Button(
            root, 
            text="Sacar", 
            font=("Arial", 10, "bold"), 
            bg=self.cor_destaque, 
            fg="white", 
            width=15, 
            command=self.sacar
        )
        self.btn_sacar.pack(pady=5)

    def atualizar_saldo(self):
        self.lbl_saldo.config(text=f"Saldo: R$ {self.saldo:.2f}")

    def obter_valor(self):
        try:
            valor = float(self.txt_valor.get().replace(",", "."))
            if valor <= 0:
                messagebox.showwarning("Atenção", "Digite um valor maior que zero.")
                return None
            return valor
        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite um número válido.")
            return None

    def depositar(self):
        valor = self.obter_valor()
        if valor:
            self.saldo += valor
            self.atualizar_saldo()
            messagebox.showinfo("Sucesso", f"Depósito de R$ {valor:.2f} realizado!")
            self.txt_valor.delete(0, tk.END)

    def sacar(self):
        valor = self.obter_valor()
        if valor:
            if valor > self.saldo:
                messagebox.showerror("Erro", "Saldo insuficiente!")
            else:
                self.saldo -= valor
                self.atualizar_saldo()
                messagebox.showinfo("Sucesso", f"Saque de R$ {valor:.2f} realizado!")
                self.txt_valor.delete(0, tk.END)

# Execução do aplicativo
if __name__ == "__main__":
    app_root = tk.Tk()
    app = BancoVisual(app_root)
    app_root.mainloop()