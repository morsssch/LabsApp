import customtkinter as ctk
from styles import style


class AboutFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.title = ctk.CTkLabel(self, text="О программе", font=style["title_font"])
        self.title.pack(pady=(20, 10))

        self.label = ctk.CTkLabel(
            self,
            text="Выполнил: Ильинов Никита\n\nГруппа: ВИ11\n\nВерсия: 1.0",
            font=style["main_font"],
            anchor="w",
        )
        self.label.pack(pady=(10, 20), padx=20)
