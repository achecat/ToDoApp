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


        #cria card pra cada tarefa
        for t in tarefas:
            self._criar_card_tarefa(self.scroll_a_fazer, t)


    def _criar_card_tarefa(self, parent, tarefa):
        '''Cria a linha da tarefa/card da tarefa, começa com _ pra ser privada'''
        card_frame = ctk.CTkFrame(parent)
        card_frame.pack(fill="x", pady=5, padx=5)


        #caixinha pra marcar que foi concluida
        chk_var = ctk.BooleanVar(value=tarefa.concluida)
        chk = ctk.CTkCheckBox(
            card_frame,
            text=f"[{tarefa.categoria}] {tarefa.titulo}",
            variable=chk_var,
            command=lambda: self._toggle_status(tarefa.id),
        )
        chk.pack(side="left", padx=10, pady=10)


        #btn = (botão) excluir
        btn_deletar = ctk.CTkButton(
            card_frame,
            text="❌",
            width=30,
            fg_color="transparent",
            hover_color="#8B0000",
            command=lambda: self._deletar(tarefa.id),
        )
        btn_deletar.pack(side="right", padx=10)


    def _toggle_status(self, tarefa_id):
        ServiceTarefas.alternar_status(tarefa_id)


    def _deletar(self, tarefa_id):
        ServiceTarefas.deletar_tarefa(tarefa_id)

        #recarrega a tela após deletar
        self.carregar_tarefas()