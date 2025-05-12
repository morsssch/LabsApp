import customtkinter as ctk
import math
from src.components.buttonComponent import buttonComponent
from styles import style


class Task4Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(
            self,
            text="Задание 4: Проверка нахождения числа в диапазоне",
            font=style["title_font"],
        )
        self.label.pack(pady=20, side="top")

        self.input_label = ctk.CTkLabel(
            self, text="Введите число:", font=style["main_font"]
        )
        self.input_label.pack(pady=5, side="top")

        self.input_entry = ctk.CTkEntry(self, width=400)
        self.input_entry.pack(pady=5, side="top")

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20, side="top")

        self.submit_button = buttonComponent(
            self.button_frame, text="Проверить", command=self.submit
        )
        self.submit_button.pack(side="left", padx=10)

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
            text="",
            font=style["main_font"],
            wraplength=480,
            justify="left",
        )
        self.output_label.pack(pady=20, padx=10, ipady=10, ipadx=10, anchor="w")

    def submit(self):
        try:
            a = int(self.input_entry.get())

            if -15 < a <= 12:
                self.output_label.configure(
                    text=f"{a} находится в диапазоне от -15 до 12."
                )
            elif 14 < a < 17:
                self.output_label.configure(
                    text=f"{a} находится в диапазоне от 14 до 17."
                )
            elif 19 <= a < math.inf:
                self.output_label.configure(
                    text=f"{a} находится в диапазоне от 19 до бесконечности."
                )
            else:
                self.output_label.configure(
                    text="Число не входит ни в один из заданных диапазонов."
                )
        except ValueError:
            self.output_label.configure(text="Пожалуйста, введите корректное число.")

    def reset(self):
        self.input_entry.delete(0, ctk.END)
        self.output_label.configure(text="")
