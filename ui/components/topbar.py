import customtkinter as ctk

class TopBar(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.app = master

        #botao de listar as tarefas
        self.botao_listar = ctk.CTkButton(
            self,
            text="Tarefas",
            command=lambda: self.app.trocar_pagina("listar")
        )
        self.botao_listar.pack(side="left", padx=10, pady=10)

        #botao de adicionar tarefa
        self.botao_adicionar = ctk.CTkButton(
            self,
            text="Nova Tarefa",
            command=lambda: self.app.trocar_pagina("adicionar")
        )
        self.botao_adicionar.pack(side="left", padx=5, pady=10)