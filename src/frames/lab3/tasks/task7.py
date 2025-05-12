import customtkinter as ctk
import math
from src.components.buttonComponent import buttonComponent
from styles import style


class Task7Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(
            self,
            text="Задание 7: Вычисление наименьшего общего кратного (НОК)",
            font=style["title_font"],
        )
        self.label.pack(pady=20, side="top")

        self.input_label_a = ctk.CTkLabel(
            self, text="Введите число a:", font=style["main_font"]
        )
        self.input_label_a.pack(pady=5, side="top")

        self.input_entry_a = ctk.CTkEntry(self, width=400)
        self.input_entry_a.pack(pady=5, side="top")

        self.input_label_b = ctk.CTkLabel(
            self, text="Введите число b:", font=style["main_font"]
        )
        self.input_label_b.pack(pady=5, side="top")

        self.input_entry_b = ctk.CTkEntry(self, width=400)
        self.input_entry_b.pack(pady=5, side="top")

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20, side="top")

        self.submit_button = buttonComponent(
            self.button_frame, text="Вычислить НОК", command=self.calculate_lcm
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

    def calculate_lcm(self):
        try:
            a = int(self.input_entry_a.get())
            b = int(self.input_entry_b.get())

            lcm = abs(a * b) // math.gcd(a, b)

            self.output_label.configure(
                text=f"Наименьшее общее кратное для чисел {a} и {b}: {lcm}"
            )
        except ValueError:
            self.output_label.configure(text="Пожалуйста, введите целые числа.")

    def reset(self):
        self.input_entry_a.delete(0, ctk.END)
        self.input_entry_b.delete(0, ctk.END)
        self.output_label.configure(text="")
