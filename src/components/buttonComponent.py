import customtkinter as ctk
from styles import style


class buttonComponent(ctk.CTkButton):
    def __init__(self, parent, text="Кнопка", command=None, **kwargs):

        super().__init__(
            parent,
            text=text,
            command=command,
            corner_radius=10,
            border_width=0,
            font=style["main_font"],
            fg_color=style["button_background"],
            text_color=style["button_foreground"],
            hover_color=style["button_hover"],
            border_color=style["button_foreground"],
            **kwargs
        )
