import tkinter as tk
from tkinter import messagebox, ttk

# --- MODELO DE DADOS (Substituindo as variáveis soltas por uma lista estruturada) ---
servicos = [
    {
        "nome": "Corte",
        "barbeiros": "Gustavo, Nicolas, Felipe, Victor",
        "preco": 30.00,
        "validade": "7 dias",
        "descricao": "O melhor corte da região.",
        "estoque": 10,
    },
    {
        "nome": "Barba",
        "barbeiros": "Gustavo, Nicolas, Felipe, Victor",
        "preco": 20.00,
        "validade": "7 dias",
        "descricao": "Melhor barbearia da região.",
        "estoque": 10,
    },
    {
        "nome": "Sobrancelha",
        "barbeiros": "Gustavo, Nicolas, Felipe, Victor",
        "preco": 7.00,
        "validade": "7 dias",
        "descricao": "O melhor estilo.",
        "estoque": 10,
    },
    {
        "nome": "Luzes",
        "barbeiros": "Gustavo, Nicolas, Felipe, Victor",
        "preco": 50.00,
        "validade": "1 mês",
        "descricao": "O melhor estilo.",
        "estoque": 10,
    },
    {
        "nome": "Alisamento",
        "barbeiros": "Gustavo, Nicolas, Felipe, Victor",
        "preco": 50.00,
        "validade": "1 mês",
        "descricao": "O melhor estilo.",
        "estoque": 10,
    },
]

# --- CORES DA PALETA BARBER SHOP ---
COR_BG = "#1A1A1A"  # Grafite escuro / Quase preto
COR_CARD = "#262626"  # Cinza escuro para os painéis
COR_TEXTO = "#FFFFFF"  # Branco para leitura limpa
COR_DETALHE = "#D4AF37"  # Dourado Barbearia (Gold)
COR_ACCENT_AZUL = "#1E3A8A"  # Azul tradicional de Barber Pole
COR_ACCENT_VERMELHO = "#991B1B"  # Vermelho tradicional de Barber Pole


class BarbeariaApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Barbearia - Sistema de Agendamento")
        self.root.geometry("850x650")
        self.root.configure(bg=COR_BG)

        # Cabeçalho Principal Estilizado
        self.header_frame = tk.Frame(
            root, bg=COR_BG, highlightbackground=COR_DETALHE, highlightthickness=1
        )
        self.header_frame.pack(fill="x", padx=15, pady=15)

        self.lbl_titulo = tk.Label(
            self.header_frame,
            text="💈 BARBER SHOP SYSTEM 💈",
            font=("Impact", 28),
            fg=COR_DETALHE,
            bg=COR_BG,
        )
        self.lbl_titulo.pack(pady=5)

        self.lbl_subtitulo = tk.Label(
            self.header_frame,
            text="Tradição, Estilo e Modernidade",
            font=("Helvetica", 11, "italic"),
            fg="#AAAAAA",
            bg=COR_BG,
        )
        self.lbl_subtitulo.pack(pady=2)

        # Layout Principal: Esquerda (Menu) | Direita (Área Dinâmica de Conteúdo)
        self.main_container = tk.Frame(root, bg=COR_BG)
        self.main_container.pack(fill="both", expand=True, padx=15, pady=5)

        self.menu_frame = tk.Frame(self.main_container, bg=COR_CARD, width=220)
        self.menu_frame.pack(side="left", fill="y", padx=(0, 10), pady=5)
        self.menu_frame.pack_propagate(False)

        self.content_frame = tk.Frame(self.main_container, bg=COR_CARD)
        self.content_frame.pack(side="right", fill="both", expand=True, pady=5)

        self.criar_menu()
        self.mostrar_home()  # Tela inicial padrão

    def criar_menu(self):
        """Gera os botões laterais do menu"""
        opcoes = [
            ("Agendar Serviço", self.mostrar_agendamento),
            ("Gerenciar Serviços", self.mostrar_gerenciamento),
            ("Status do Estoque", self.mostrar_estoque),
            ("Localização e Contato", self.mostrar_info),
            ("Sobre / Funcionamento", self.mostrar_sobre),
        ]

        tk.Label(
            self.menu_frame,
            text="NAVEGAÇÃO",
            font=("Helvetica", 10, "bold"),
            fg=COR_DETALHE,
            bg=COR_CARD,
        ).pack(pady=15)

        for texto, comando in opcoes:
            btn = tk.Button(
                self.menu_frame,
                text=texto,
                font=("Helvetica", 11, "bold"),
                fg=COR_TEXTO,
                bg=COR_BG,
                activebackground=COR_DETALHE,
                activeforeground=COR_BG,
                bd=0,
                cursor="hand2",
                relief="flat",
                pady=10,
                command=comando,
            )
            btn.pack(fill="x", padx=10, pady=5)

        # Botão de Sair destacado
        btn_sair = tk.Button(
            self.menu_frame,
            text="Sair do Sistema",
            font=("Helvetica", 10, "bold"),
            fg=COR_TEXTO,
            bg=COR_ACCENT_VERMELHO,
            activebackground="#EF4444",
            activeforeground=COR_TEXTO,
            bd=0,
            cursor="hand2",
            command=self.root.quit,
        )
        btn_sair.pack(side="bottom", fill="x", padx=10, pady=15)

    def limpar_tela_conteudo(self):
        """Limpa o frame da direita para renderizar a nova opção do menu"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def criar_titulo_secao(self, texto):
        lbl = tk.Label(
            self.content_frame,
            text=texto,
            font=("Helvetica", 16, "bold"),
            fg=COR_DETALHE,
            bg=COR_CARD,
        )
        lbl.pack(pady=15)
        return lbl

    def mostrar_home(self):
        self.limpar_tela_conteudo()
        self.criar_titulo_secao("Bem-vindo ao nosso Sistema")
        lbl_boas_vindas = tk.Label(
            self.content_frame,
            text="Selecione uma opção no menu lateral para começar.\n\nPraticidade para agendar seus cortes e gerenciar o negócio!",
            font=("Helvetica", 12),
            fg=COR_TEXTO,
            bg=COR_CARD,
            justify="center",
        )
        lbl_boas_vindas.pack(expand=True)

    # --- OPÇÃO 2: AGENDAR SERVIÇO ---
    def mostrar_agendamento(self):
        self.limpar_tela_conteudo()
        self.criar_titulo_secao("📝 AGENDAR UM HORÁRIO")

        # Frame interno para os cartões de serviço
        scroll_frame = tk.Frame(self.content_frame, bg=COR_CARD)
        scroll_frame.pack(fill="both", expand=True, padx=15)

        for idx, serv in enumerate(servicos):
            card = tk.LabelFrame(
                scroll_frame,
                text=f" {serv['nome']} ",
                font=("Helvetica", 11, "bold"),
                fg=COR_DETALHE,
                bg=COR_BG,
                bd=1,
                labelanchor="nw",
                padx=10,
                pady=5,
            )
            card.pack(fill="x", pady=5)

            info_text = f"Preço: R$ {serv['preco']:.2f}  |  Vagas Restantes: {serv['estoque']}  |  Duração: {serv['validade']}"
            tk.Label(
                card,
                text=info_text,
                font=("Helvetica", 10),
                fg=COR_TEXTO,
                bg=COR_BG,
            ).pack(side="left", anchor="w")

            # Botão de agendamento aciona popup de escolha de barbeiro
            btn_agendar = tk.Button(
                card,
                text="Agendar",
                font=("Helvetica", 9, "bold"),
                bg=COR_ACCENT_AZUL,
                fg=COR_TEXTO,
                bd=0,
                padx=15,
                cursor="hand2",
                command=lambda s=serv: self.popup_escolher_barbeiro(s),
            )
            btn_agendar.pack(side="right", anchor="e")

            if serv["estoque"] <= 0:
                btn_agendar.configure(
                    state="disabled", text="Esgotado", bg="#444444"
                )

    def popup_escolher_barbeiro(self, servico):
        """Abre uma janela para selecionar o profissional disponível"""
        popup = tk.Toplevel(self.root)
        popup.title("Escolha o Profissional")
        popup.geometry("350x200")
        popup.configure(bg=COR_BG)
        popup.transient(self.root)
        popup.grab_set()

        tk.Label(
            popup,
            text=f"Selecione o Barbeiro para:\n{servico['nome']}",
            font=("Helvetica", 11, "bold"),
            fg=COR_DETALHE,
            bg=COR_BG,
        ).pack(pady=10)

        lista_barbeiros = [b.strip() for b in servico["barbeiros"].split(",")]
        combo = ttk.Combobox(popup, values=lista_barbeiros, state="readonly")
        combo.pack(pady=10)
        combo.current(0)

        def confirmar():
            barbeiro = combo.get()
            servico["estoque"] -= 1
            messagebox.showinfo(
                "Sucesso!",
                f"✅ Agendamento de {servico['nome']} feito com sucesso com o profissional {barbeiro}!",
            )
            popup.destroy()
            self.mostrar_agendamento()  # Atualiza a tela anterior

        tk.Button(
            popup,
            text="Confirmar Agendamento",
            bg=COR_DETALHE,
            fg=COR_BG,
            font=("Helvetica", 10, "bold"),
            bd=0,
            command=confirmar,
        ).pack(pady=15)

    # --- OPÇÃO 1: CADASTRAR/ALTERAR SERVIÇO ---
    def mostrar_gerenciamento(self):
        self.limpar_tela_conteudo()
        self.criar_titulo_secao("🛠️ CONFIGURAR / ALTERAR SERVIÇOS")

        # Dropdown para escolher qual vaga atualizar
        frame_selecao = tk.Frame(self.content_frame, bg=COR_CARD)
        frame_selecao.pack(pady=5)

        tk.Label(
            frame_selecao,
            text="Selecione o serviço para editar: ",
            font=("Helvetica", 10),
            fg=COR_TEXTO,
            bg=COR_CARD,
        ).pack(side="left")

        nomes_servicos = [f"{i+1} - {s['nome']}" for i, s in enumerate(servicos)]
        combo_edicao = ttk.Combobox(
            frame_selecao, values=nomes_servicos, state="readonly", width=25
        )
        combo_edicao.pack(side="left", padx=5)
        combo_edicao.current(0)

        # Campos do Formulário
        form_frame = tk.Frame(self.content_frame, bg=COR_CARD)
        form_frame.pack(pady=15, padx=50, fill="x")

        campos = ["Nome:", "Barbeiros:", "Preço (R$):", "Duração:", "Descrição:", "Vagas/Estoque:"]
        entries = {}

        for i, campo in enumerate(campos):
            lbl = tk.Label(
                form_frame,
                text=campo,
                font=("Helvetica", 10),
                fg=COR_TEXTO,
                bg=COR_CARD,
                anchor="w",
            )
            lbl.grid(row=i, column=0, sticky="w", pady=4)
            ent = tk.Entry(
                form_frame,
                bg=COR_BG,
                fg=COR_TEXTO,
                insertbackground=COR_TEXTO,
                bd=1,
                relief="solid",
            )
            ent.grid(row=i, column=1, sticky="ew", pady=4, padx=(10, 0))
            entries[campo] = ent

        form_frame.columnconfigure(1, weight=1)

        def carregar_dados_no_form(event):
            idx = combo_edicao.current()
            s = servicos[idx]
            entries["Nome:"].delete(0, tk.END)
            entries["Nome:"].insert(0, s["nome"])
            entries["Barbeiros:"].delete(0, tk.END)
            entries["Barbeiros:"].insert(0, s["barbeiros"])
            entries["Preço (R$):"].delete(0, tk.END)
            entries["Preço (R$):"].insert(0, str(s["preco"]))
            entries["Duração:"].delete(0, tk.END)
            entries["Duração:"].insert(0, s["validade"])
            entries["Descrição:"].delete(0, tk.END)
            entries["Descrição:"].insert(0, s["descricao"])
            entries["Vagas/Estoque:"].delete(0, tk.END)
            entries["Vagas/Estoque:"].insert(0, str(s["estoque"]))

        combo_edicao.bind("<<ComboboxSelected>>", carregar_dados_no_form)
        carregar_dados_no_form(None)  # Inicializa o primeiro

        def salvar_alteracoes():
            idx = combo_edicao.current()
            try:
                servicos[idx]["nome"] = entries["Nome:"].get()
                servicos[idx]["barbeiros"] = entries["Barbeiros:"].get()
                servicos[idx]["preco"] = float(entries["Preço (R$):"].get())
                servicos[idx]["validade"] = entries["Duração:"].get()
                servicos[idx]["descricao"] = entries["Descrição:"].get()
                servicos[idx]["estoque"] = int(entries["Vagas/Estoque:"].get())

                messagebox.showinfo(
                    "Sucesso",
                    f"📦 Serviço '{servicos[idx]['nome']}' atualizado com sucesso!",
                )
                # Recarrega a listagem do combobox
                combo_edicao["values"] = [
                    f"{i+1} - {s['nome']}" for i, s in enumerate(servicos)
                ]
            except ValueError:
                messagebox.showerror(
                    "Erro",
                    "Por favor, verifique os campos de Preço e Vagas (devem ser numéricos).",
                )

        btn_salvar = tk.Button(
            self.content_frame,
            text="Salvar Alterações",
            font=("Helvetica", 11, "bold"),
            bg=COR_DETALHE,
            fg=COR_BG,
            bd=0,
            pady=8,
            padx=20,
            cursor="hand2",
            command=salvar_alteracoes,
        )
        btn_salvar.pack(pady=10)

    # --- OPÇÃO 3: VER SERVIÇOS / VENDAS / STATUS ESTOQUE ---
    def mostrar_estoque(self):
        self.limpar_tela_conteudo()
        self.criar_titulo_secao("📊 STATUS DO ESTOQUE E VAGAS")

        for serv in servicos:
            frame_item = tk.Frame(
                self.content_frame,
                bg=COR_BG,
                highlightbackground="#333333",
                highlightthickness=1,
            )
            frame_item.pack(fill="x", padx=20, pady=5)

            txt_info = f"✂️ {serv['nome'].upper()} \nDescrição: {serv['descricao']}\nPreço: R$ {serv['preco']:.2f}"
            lbl_info = tk.Label(
                frame_item,
                text=txt_info,
                font=("Helvetica", 10),
                fg=COR_TEXTO,
                bg=COR_BG,
                justify="left",
                anchor="w",
            )
            lbl_info.pack(side="left", padx=15, pady=10)

            lbl_vagas = tk.Label(
                frame_item,
                text=f"{serv['estoque']}\nvagas",
                font=("Impact", 14),
                fg=COR_DETALHE if serv["estoque"] > 0 else COR_ACCENT_VERMELHO,
                bg=COR_BG,
            )
            lbl_vagas.pack(side="right", padx=25)

    # --- OPÇÃO 4 e 5: LOCALIZAÇÃO E CONTATO ---
    def mostrar_info(self):
        self.limpar_tela_conteudo()
        self.criar_titulo_secao("📍 LOCALIZAÇÃO E CONTATO")

        info_txt = (
            "📌 ENDEREÇO:\n"
            "Rua dos Barbeiros, nº 100 - Centro - Cidade Grande\n"
            "Ponto de referência: Ao lado do grande shopping.\n\n"
            "--------------------------------------------------\n\n"
            "📞 CONTATOS:\n"
            "Telefone/WhatsApp: (11) 99999-9999\n"
            "E-mail: contato@barbeariaexemplo.com"
        )

        lbl = tk.Label(
            self.content_frame,
            text=info_txt,
            font=("Helvetica", 11),
            fg=COR_TEXTO,
            bg=COR_CARD,
            justify="center",
            pady=20,
        )
        lbl.pack()

    # --- OPÇÃO 6, 7 e 8: SOBRE NÓS, FUNCIONAMENTO E CRÉDITOS ---
    def mostrar_sobre(self):
        self.limpar_tela_conteudo()
        self.criar_titulo_secao("💈 SOBRE A BARBEARIA")

        texto_sobre = (
            "A melhor barbearia da região, unindo tradição, estilo e modernidade.\n"
            "Cuidamos do seu visual com os melhores profissionais do mercado.\n\n"
            "📅 HORÁRIO DE FUNCIONAMENTO:\n"
            "• Segunda a Sexta: 09:00 às 20:00\n"
            "• Sábados: 08:00 às 18:00\n"
            "• Domingos e Feriados: Fechado\n\n"
            "👨‍💻 CRÉDITOS:\n"
            "Desenvolvido por: Equipe de Programação da Barbearia\n"
            "Projeto idealizado para facilitar a vida dos nossos clientes e barbeiros."
        )

        lbl = tk.Label(
            self.content_frame,
            text=texto_sobre,
            font=("Helvetica", 11),
            fg=COR_TEXTO,
            bg=COR_CARD,
            justify="center",
            pady=10,
        )
        lbl.pack()


# --- INICIALIZAÇÃO DO APP ---
if __name__ == "__main__":
    root = tk.Tk()
    app = BarbeariaApp(root)
    root.mainloop()