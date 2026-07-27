from db.models import criar_banco

from ui.app import App


if __name__ == "__main__":
    #inicia o banco
    criar_banco()

    #roda a interface (customtkinter)
    app = App()
    app.mainloop()