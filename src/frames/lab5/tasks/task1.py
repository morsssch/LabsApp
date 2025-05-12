import os
import customtkinter as ctk
from tkinter import filedialog
from src.components.buttonComponent import buttonComponent
from styles import style


class Task1Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(
            self, text="Задание 1: Подсчёт файлов в папке", font=style["title_font"]
        )
        self.label.pack(pady=20, side="top")

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20, side="top")

        self.select_button = buttonComponent(
            self.button_frame, text="Выбрать папку", command=self.select_directory
        )
        self.select_button.pack(side="left", padx=10)

        self.reset_button = buttonComponent(
            self.button_frame, text="Сбросить", command=self.reset
        )
        self.reset_button.pack(side="left", padx=10)

        self.output_frame = ctk.CTkFrame(
            self, corner_radius=0, fg_color=style["background_secondary"]
        )
        self.output_frame.pack(side="bottom", fill="both")

        self.output_label = ctk.CTkLabel(
            self.output_frame,
            text="Папка не выбрана",
            font=style["main_font"],
            wraplength=480,
            justify="left",
        )
        self.output_label.pack(pady=20, padx=10, ipady=10, ipadx=10, anchor="w")

    def select_directory(self):
        folder_path = filedialog.askdirectory()

        if folder_path:
            try:
                files = [
                    f
                    for f in os.listdir(folder_path)
                    if os.path.isfile(os.path.join(folder_path, f))
                ]
                count = len(files)
                self.output_label.configure(
                    text=f"Выбрана папка:\n{folder_path}\n\nФайлов в папке: {count}"
                )
            except Exception as e:
                self.output_label.configure(text=f"Ошибка: {e}")
        else:
            self.output_label.configure(text="Папка не выбрана.")

    def reset(self):
        self.output_label.configure(text="Папка не выбрана")
