import customtkinter as ctk
from src.components.buttonComponent import buttonComponent
from styles import style


class Task6Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(
            self,
            text="Задание 6: Суммирование чисел",
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
            self.button_frame, text="Добавить", command=self.submit
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

        self.total_sum = 0

    def submit(self):
        try:
            user_input = int(self.input_entry.get())
            self.total_sum += user_input
            self.output_label.configure(text=f"Текущая сумма: {self.total_sum}")
            self.input_entry.delete(0, ctk.END)
        except ValueError:
            self.output_label.configure(text="Пожалуйста, введите целое число.")

    def reset(self):
        self.input_entry.delete(0, ctk.END)
        self.output_label.configure(text="")
        self.total_sum = 0
