import customtkinter as ctk
from services.task_service import ServiceTarefas

class HomePage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)


        #config do grid (2 colunas com larguras iguais)
        self.grid_columnconfigure((0, 1), weight=1, uniform="group1")
        self.grid_rowconfigure(1, weight=1)


        #cabeçalhos das colunas
        lbl_a_fazer = ctk.CTkLabel(
            self, text="📌 A Fazer", font=("Arial", 18, "bold"), text_color="#74B9FF"
        )
        lbl_a_fazer.grid(row=0, column=0, pady=(10, 5), sticky="w", padx=15)

        lbl_concluidos = ctk.CTkLabel(
            self, text="✅ Concluídos", font=("Arial", 18, "bold"), text_color="#55E6C1"
        )
        lbl_concluidos.grid(row=0, column=1, pady=(10, 5), sticky="w", padx=15)


        #area rolavel (la ele)
        self.scroll_a_fazer = ctk.CTkScrollableFrame(
            self, fg_color="#2A2A3D", corner_radius=12
        )
        self.scroll_a_fazer.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.scroll_concluidos = ctk.CTkScrollableFrame(
            self, fg_color="#2A2A3D", corner_radius=12
        )
        self.scroll_concluidos.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)


        #renderiza os dados do banco
        self.carregar_tarefas()


    def carregar_tarefas(self):
        '''Limpa a lista atual e busca as tarefas do banco'''

        #limpa elementos antigos da tela
        for w in self.scroll_a_fazer.winfo_children():
            w.destroy()
        for w in self.scroll_concluidos.winfo_children():
            w.destroy()


        #busca os dados no banco
        tarefas= ServiceTarefas.listar_todas()

        a_fazer = [t for t in tarefas if not t.concluida]
        concluidas = [t for t in tarefas if t.concluida]


        # Preenche a coluna "A Fazer"
        if not a_fazer:
            ctk.CTkLabel(
                self.scroll_a_fazer, text="Nenhuma tarefa pendente!", text_color="#A0A0A0"
            ).pack(pady=20)
        else:
            for t in a_fazer:
                self._criar_card_tarefa(self.scroll_a_fazer, t)


        # Preenche a coluna "Concluídos"
        if not concluidas:
            ctk.CTkLabel(
                self.scroll_concluidos, text="Nenhuma tarefa concluída.", text_color="#A0A0A0"
            ).pack(pady=20)
        else:
            for t in concluidas:
                self._criar_card_tarefa(self.scroll_concluidos, t)


    def _criar_card_tarefa(self, parent, tarefa):
        '''Cria a linha da tarefa/card da tarefa, começa com _ pra ser privada'''
        card = ctk.CTkFrame(parent, fg_color="#1E1E2E", corner_radius=8)
        card.pack(fill="x", pady=5, padx=5)


        #caixinha pra marcar que foi concluida
        chk = ctk.CTkCheckBox(
            card,
            text=f"[{tarefa.categoria}] {tarefa.titulo}",
            font=("Arial", 13),
            checkbox_width=20,
            checkbox_height=20,
            command=lambda t_id=tarefa.id: self._toggle_status(t_id),
        )
        if tarefa.concluida:
            chk.select()
        else:
            chk.deselect()

        chk.pack(side="left", padx=10, pady=12, fill="x", expand=True)


        #btn = (botão) excluir
        btn_deletar = ctk.CTkButton(
            card,
            text="🗑️",
            width=30,
            height=30,
            fg_color="transparent",
            hover_color="#FF4D4D",
            command=lambda t_id=tarefa.id: self._deletar(t_id),
        )
        btn_deletar.pack(side="right", padx=8)

    def _toggle_status(self, tarefa_id):
        ServiceTarefas.alternar_status(tarefa_id)


    def _deletar(self, tarefa_id):
        ServiceTarefas.deletar_tarefa(tarefa_id)

        #recarrega a tela após deletar
        self.carregar_tarefas()