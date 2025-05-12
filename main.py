import os
import sys
import customtkinter as ctk
from src.components.headerComponent import headerComponent
from src.frames.mainMenu import MainMenu
from src.frames.lab1.lab1 import Lab1Frame
from src.frames.lab2.lab2 import Lab2Frame
from src.frames.lab3.lab3 import Lab3Frame
from src.frames.lab5.lab5 import Lab5Frame
from src.frames.lab6.lab6 import Lab6Frame
from src.frames.lab7.lab7 import Lab7Frame
from src.frames.about import AboutFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("labsApp")
        self.wm_minsize(900, 670)

        self.header = headerComponent(
            self,
            title="LABS.APP",
            button_text="Домой",
            command=self.show_home_page,
        )
        self.header.pack(fill="x", side="top")

        self.MainMenu = MainMenu(self, app=self)
        self.frames = {
            "Лабораторная работа 1": Lab1Frame(self),
            "Лабораторная работа 2": Lab2Frame(self),
            "Лабораторная работа 3": Lab3Frame(self),
            "Лабораторная работа 5": Lab5Frame(self),
            "Лабораторная работа 6": Lab6Frame(self),
            "Лабораторная работа 7": Lab7Frame(self),
            "О программе": AboutFrame(self),
        }

        self.current_frame = None
        self.show_home_page()

    def show_home_page(self):
        self.show_frame(self.MainMenu)

    def show_frame(self, frame):
        if self.current_frame:
            self.current_frame.pack_forget()

        frame.pack(fill="both", expand=True)
        self.current_frame = frame


if __name__ == "__main__":
    app = App()
    app.mainloop()
