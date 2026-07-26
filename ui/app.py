import customtkinter as ctk


from ui.components.topbar import TopBar

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