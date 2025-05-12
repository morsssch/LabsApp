import customtkinter as ctk
from src.components.buttonComponent import buttonComponent


class MainMenu(ctk.CTkFrame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)
        self.app = app

        self.menu_items = [
            "Лабораторная работа 1",
            "Лабораторная работа 2",
            "Лабораторная работа 3",
            "Лабораторная работа 5",
            "Лабораторная работа 6",
            "Лабораторная работа 7",
            "О программе",
        ]

        self.create_menu_items()

    def create_menu_items(self):
        for item in self.menu_items:
            button = buttonComponent(
                self,
                text=item,
                command=lambda i=item: self.on_menu_item_click(i),
            )
            button.pack(fill="x", padx=10, pady=5, ipady=20, expand=True)

    def on_menu_item_click(self, item):
        frame = self.app.frames.get(item)
        if frame:
            self.app.show_frame(frame)
