import customtkinter as ctk
from services.task_service import ServiceTarefas

class HomePage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #titulo
        self.titulo = ctk.CTkLabel(
            self, text="Sua Lista de Tarefas", font=("Arial", 20, "bold")
        )
        self.titulo.pack(anchor="w", padx=20, pady=(15,5))


        #area rolavel (la ele)
        self.scroll_tarefas = ctk.CTkScrollableFrame(self)
        self.scroll_tarefas.pack(fill="both", expand=True, padx=15, pady=10)


        #renderiza os dados do banco
        self.carregar_tarefas()


    def carregar_tarefas(self):
        '''Limpa a lista atual e busca as tarefas do banco'''

        #limpa elementos antigos da tela
        for widget in self.scroll_tarefas.winfo_children():
            widget.destroy()


        #busca os dados no banco
        tarefas= ServiceTarefas.listar_todas()

        if not tarefas:
            msg_vazio = ctk.CTkLabel(
                self.scroll_tarefas,
                text="Nenhuma tarefa encontrada.",
                font=("Arial", 14, "italic")
            )
            msg_vazio.pack(pady=20)
            return


        #cria card pra cada tarefa
        for t in tarefas:
            self._criar_card_tarefa(t)


    def _criar_card_tarefa(self, tarefa):
        '''Cria a linha da tarefa/card da tarefa, começa com _ pra ser privada'''
        card_frame = ctk.CTkFrame(self.scroll_tarefas)
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


        #botão excluir
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