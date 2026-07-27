import customtkinter as ctk

from ui.components.topbar import TopBar

from ui.pages.home import HomePage
from ui.pages.adicionar_task import AdicionarTaskPage

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        #config da janela
        self.title("To-Do List App")
        self.geometry("800x600")
        self.minsize(600, 400)

        #tema
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        #navbar
        self.topbar = TopBar(master=self)
        self.topbar.pack(side="top", fill="x", padx=10, pady=(10,0))

        self.container_conteudo = ctk.CTkFrame(master=self, fg_color="transparent")
        self.container_conteudo.pack(
            side="bottom", fill="both", expand=True, padx=10, pady=10
        )

        #instancia as janelas pra n ter q recriar toda vez que clicar em um botão
        self.paginas = {}
        self._inicializar_paginas()
        self.trocar_pagina("listar")


    def _inicializar_paginas(self):
        self.paginas["listar"] = HomePage(master=self.container_conteudo)
        self.paginas["adicionar"] = AdicionarTaskPage(
            master=self.container_conteudo,
            on_success_callback=lambda: self.trocar_pagina("listar"),
        )


    def trocar_pagina(self, nome_pagina: str):
        #sistema de nav
        for pagina in self.paginas.values():
            pagina.pack_forget()

        if nome_pagina in self.paginas:
            #se voltamos para a tela de listar, atualizamos do banco
            if nome_pagina == "listar":
                self.paginas["listar"].carregar_tarefas()

            self.paginas[nome_pagina].pack(fill="both", expand=True)