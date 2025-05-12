import customtkinter as ctk
from src.components.buttonComponent import buttonComponent


class sidebarComponent(ctk.CTkFrame):
    def __init__(self, master, tasks, on_task_click, **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)
    
        self.on_task_click = on_task_click
        self.buttons = []

        for task_number in tasks:
            button = buttonComponent(
                self,
                text=str(task_number),
                command=lambda i=task_number: self.on_task_click(i),
                width=40,
                height=40,
            )
            button.pack(padx=10, pady=5, fill="x")
            self.buttons.append(button)

        self.pack(side="left", fill="y")
