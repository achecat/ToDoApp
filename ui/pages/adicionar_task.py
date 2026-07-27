import customtkinter as ctk
from services.task_service import ServiceTarefas

class AdicionarTaskPage(ctk.CTkFrame):

    def __init__(self, master, on_success_callback=None, **kwargs):
        super().__init__(master, **kwargs)

        #callback opcional para avisar o App que salvou com sucesso
        self.on_success_callback = on_success_callback


        #título
        self.titulo = ctk.CTkLabel(
            self, text="Adicionar Nova Tarefa", font=("Arial", 20, "bold")
        )
        self.titulo.pack(anchor="w", padx=20, pady=15)


        #campo: título
        self.entry_titulo = ctk.CTkEntry(
            self, placeholder_text="Título da tarefa..."
        )
        self.entry_titulo.pack(fill="x", padx=20, pady=8)


        #campo: categoria
        self.entry_categoria = ctk.CTkEntry(
            self, placeholder_text="Categoria (ex: Trabalho, Estudo)..."
        )
        self.entry_categoria.pack(fill="x", padx=20, pady=8)


        #campo: descrição
        self.entry_descricao = ctk.CTkEntry(
            self, placeholder_text="Descrição (opcional)..."
        )
        self.entry_descricao.pack(fill="x", padx=20, pady=8)

        #botão salvar
        self.btn_salvar = ctk.CTkButton(
            self, text="Salvar Tarefa", command=self._salvar
        )
        self.btn_salvar.pack(padx=20, pady=20)

        #mensagem de feedback
        self.label_msg = ctk.CTkLabel(self, text="")
        self.label_msg.pack(pady=5)

    def _salvar(self):
        titulo = self.entry_titulo.get().strip()
        categoria = self.entry_categoria.get().strip() or "Geral"
        descricao = self.entry_descricao.get().strip() or None

        if not titulo:
            self.label_msg.configure(
                text="Informe pelo menos o título!", text_color="orange"
            )
            return

        #chama o service
        ServiceTarefas.adicionar(
            titulo=titulo, descricao=descricao, categoria=categoria
        )

        #limpa os campos
        self.entry_titulo.delete(0, "end")
        self.entry_categoria.delete(0, "end")
        self.entry_descricao.delete(0, "end")

        self.label_msg.configure(
            text="Tarefa salva com sucesso!", text_color="green"
        )

        #executa função de callback
        if self.on_success_callback:
            self.on_success_callback()        