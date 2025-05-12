import customtkinter as ctk
from src.components.buttonComponent import buttonComponent
from styles import style


class Task10Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(
            self,
            text="Задание 10: Сумма и количество чисел",
            font=style["title_font"],
        )
        self.label.pack(pady=20, side="top")

        self.input_label = ctk.CTkLabel(
            self,
            text="Введите число:",
            font=style["main_font"],
        )
        self.input_label.pack(pady=5, side="top")

        self.input_entry = ctk.CTkEntry(self, width=400)
        self.input_entry.pack(pady=5, side="top")

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20, side="top")

        self.submit_button = buttonComponent(
            self.button_frame, text="Добавить", command=self.add_number
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
            text="Сумма чисел: 0\nКоличество чисел: 0",
            font=style["main_font"],
            wraplength=480,
            justify="left",
        )
        self.output_label.pack(pady=20, padx=10, ipady=10, ipadx=10, anchor="w")

        self.sum_n = 0
        self.count_n = 0

    def add_number(self):
        try:
            num = int(self.input_entry.get())
            self.sum_n += num
            self.count_n += 1
            self.input_entry.delete(0, ctk.END)
            self.output_label.configure(
                text=f"Сумма чисел: {self.sum_n}\nКоличество чисел: {self.count_n}"
            )
        except ValueError:
            self.output_label.configure(text="Пожалуйста, введите корректное число.")

    def reset(self):
        self.sum_n = 0
        self.count_n = 0
        self.input_entry.delete(0, ctk.END)
        self.output_label.configure(text="Сумма чисел: 0\nКоличество чисел: 0")
