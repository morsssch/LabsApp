import customtkinter as ctk
from src.components.buttonComponent import buttonComponent
from styles import style


class headerComponent(ctk.CTkFrame):
    def __init__(
        self, parent, title="Заголовок", button_text="Кнопка", command=None, **kwargs
    ):
        super().__init__(parent, height=50, corner_radius=0, **kwargs)
        self.title = title
        self.button_text = button_text

        self.header_title = ctk.CTkLabel(self, text=title, font=style["title_font"])
        self.header_title.pack(side="left", padx=20)

        self.header_button = buttonComponent(
            self,
            text=button_text,
            command=command,
        )
        self.header_button.pack(side="right", padx=10, pady=10)

        self.pack(fill="x", side="top")
