import random
import tkinter as tk
from tkinter import messagebox


class JogoAdivinhacao:

    def __init__(self, master):
        self.master = master
        self.master.title("🎯 Jogo da Adivinhação")
        self.master.geometry("420x520")
        self.master.resizable(False, False)

        self.COR_FUNDO = "#2C3E50"
        self.COR_CARD = "#34495E"
        self.COR_TEXTO = "#ECF0F1"
        self.COR_DESTAQUE = "#F1C40F"
        self.COR_BOTAO = "#2ECC71"
        self.COR_HISTORICO = "#1A252F"

        self.master.configure(bg=self.COR_FUNDO)

        self.limite_inferior = 1
        self.limite_superior = 24
        self.max_tentativas = 6
        self.tentativas = 0
        self.numero_secreto = random.randint(
            self.limite_inferior, self.limite_superior
        )

        self.criar_widgets()

    def criar_widgets(self):
        label_titulo = tk.Label(
            self.master,
            text="🎯 ADIVINHE O NÚMERO",
            font=("Segoe UI", 16, "bold"),
            bg=self.COR_FUNDO,
            fg=self.COR_DESTAQUE,
        )
        label_titulo.pack(pady=(15, 5))

        label_instrucao = tk.Label(
            self.master,
            text=f"Escolha um número entre {self.limite_inferior} e {self.limite_superior}\nVocê tem {self.max_tentativas} tentativas!",
            font=("Segoe UI", 10),
            bg=self.COR_FUNDO,
            fg=self.COR_TEXTO,
        )
        label_instrucao.pack(pady=5)

        card = tk.Frame(self.master, bg=self.COR_CARD, bd=0, relief="flat")
        card.pack(pady=10, fill="x", padx=20)

        self.label_status = tk.Label(
            card,
            text=f"Tentativa {self.tentativas + 1} de {self.max_tentativas}",
            font=("Segoe UI", 10, "bold"),
            bg=self.COR_CARD,
            fg=self.COR_DESTAQUE,
        )
        self.label_status.pack(pady=(10, 5))

        self.entry_palpite = tk.Entry(
            card,
            font=("Segoe UI", 16, "bold"),
            justify="center",
            width=8,
            bd=0,
            highlightthickness=2,
            highlightbackground=self.COR_DESTAQUE,
        )
        self.entry_palpite.pack(pady=5)
        self.entry_palpite.bind(
            "<Return>", lambda event: self.verificar_palpite()
        )

        self.btn_chutar = tk.Button(
            card,
            text="🚀 Enviar Chute",
            font=("Segoe UI", 11, "bold"),
            bg=self.COR_BOTAO,
            fg="white",
            activebackground="#27AE60",
            activeforeground="white",
            bd=0,
            padx=15,
            pady=5,
            cursor="hand2",
            command=self.verificar_palpite,
        )
        self.btn_chutar.pack(pady=(5, 10))

        self.label_dica = tk.Label(
            self.master,
            text="Boa sorte!",
            font=("Segoe UI", 11, "bold"),
            bg=self.COR_FUNDO,
            fg=self.COR_TEXTO,
        )
        self.label_dica.pack(pady=5)

        label_hist_titulo = tk.Label(
            self.master,
            text="📋 Histórico de Palpites:",
            font=("Segoe UI", 10, "bold"),
            bg=self.COR_FUNDO,
            fg=self.COR_TEXTO,
        )
        label_hist_titulo.pack(pady=(10, 2))

        self.listbox_historico = tk.Listbox(
            self.master,
            font=("Segoe UI", 10),
            bg=self.COR_HISTORICO,
            fg=self.COR_TEXTO,
            bd=0,
            height=5,
            width=35,
            selectbackground=self.COR_HISTORICO,
            highlightthickness=1,
            highlightbackground=self.COR_CARD,
        )
        self.listbox_historico.pack(pady=5)

        self.btn_reiniciar = tk.Button(
            self.master,
            text="🔄 Jogar Novamente",
            font=("Segoe UI", 10, "bold"),
            bg="#E74C3C",
            fg="white",
            activebackground="#C0392B",
            activeforeground="white",
            bd=0,
            padx=10,
            pady=4,
            cursor="hand2",
            command=self.reiniciar_jogo,
        )
        self.btn_reiniciar.pack(pady=10)

    def verificar_palpite(self):
        palpite_texto = self.entry_palpite.get()

        if not palpite_texto.isdigit():
            messagebox.showwarning(
                "Atenção", "Por favor, digite apenas números inteiros!"
            )
            self.entry_palpite.delete(0, tk.END)
            return

        palpite = int(palpite_texto)
        self.tentativas += 1
        self.entry_palpite.delete(0, tk.END)

        if palpite == self.numero_secreto:
            self.label_dica.config(
                text="🎉 PARABÉNS! Você acertou!", fg="#2ECC71"
            )
            self.listbox_historico.insert(
                0, f"Tentativa {self.tentativas}: {palpite} 🎯 (CORRETO!)"
            )
            messagebox.showinfo(
                "Vitória!",
                f"🏆 Você acertou o número {self.numero_secreto} em {self.tentativas} tentativa(s)!",
            )
            self.finalizar_jogo()
            return

        elif palpite < self.numero_secreto:
            dica_texto = f"O número secreto é MAIOR que {palpite} ⬆️"
            hist_texto = f"Tentativa {self.tentativas}: {palpite} ⬆️ (Muito baixo)"
            cor_dica = "#3498DB"
        else:
            dica_texto = f"O número secreto é MENOR que {palpite} ⬇️"
            hist_texto = f"Tentativa {self.tentativas}: {palpite} ⬇️ (Muito alto)"
            cor_dica = "#E67E22"

        self.label_dica.config(text=dica_texto, fg=cor_dica)
        self.listbox_historico.insert(0, hist_texto)

        if self.tentativas < self.max_tentativas:
            self.label_status.config(
                text=f"Tentativa {self.tentativas + 1} de {self.max_tentativas}"
            )
        else:
            self.label_dica.config(
                text=f"💥 Fim de jogo! Era o número {self.numero_secreto}.",
                fg="#E74C3C",
            )
            messagebox.showinfo(
                "Fim de Jogo",
                f"Sua chances acabaram!\nO número secreto era {self.numero_secreto}.",
            )
            self.finalizar_jogo()

    def finalizar_jogo(self):
        self.entry_palpite.config(state="disabled")
        self.btn_chutar.config(state="disabled")

    def reiniciar_jogo(self):
        self.numero_secreto = random.randint(
            self.limite_inferior, self.limite_superior
        )
        self.tentativas = 0
        self.label_status.config(
            text=f"Tentativa {self.tentativas + 1} de {self.max_tentativas}"
        )
        self.label_dica.config(text="Boa sorte!", fg=self.COR_TEXTO)
        self.listbox_historico.delete(0, tk.END)
        self.entry_palpite.config(state="normal")
        self.btn_chutar.config(state="normal")
        self.entry_palpite.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = JogoAdivinhacao(root)
    root.mainloop()