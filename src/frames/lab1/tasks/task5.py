import customtkinter as ctk
from src.components.buttonComponent import buttonComponent
from styles import style


class Task5Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        items_pady = 5

        self.label = ctk.CTkLabel(
            self, text="Задание 5: Минимальное число", font=style["title_font"]
        )
        self.label.pack(pady=20, side="top")

        self.list_label = ctk.CTkLabel(
            self, text="Введите список чисел через пробел:", font=style["main_font"]
        )
        self.list_label.pack(pady=items_pady, side="top")
        self.list_entry = ctk.CTkEntry(self, width=400)
        self.list_entry.pack(pady=items_pady, side="top")

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20, side="top")

        self.process_button = buttonComponent(
            self.button_frame, text="Обработать", command=self.process_list
        )
        self.process_button.pack(side="left", padx=10)

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
            font=("Arial", 12),
            wraplength=480,
            justify="left",
        )
        self.output_label.pack(pady=20, padx=10, ipady=10, ipadx=10, anchor="w")

    def process_list(self):
        input_text = self.list_entry.get()

        if not input_text.strip():
            self.output_label.configure(
                text="Ошибка: Пожалуйста, введите список чисел.",
                font=style["main_font"],
            )
            return

        try:
            some_list = list(map(int, input_text.split()))
        except ValueError:
            self.output_label.configure(
                text="Ошибка: Пожалуйста, введите только числа.",
                font=style["main_font"],
            )
            return

        result = min(some_list)

        self.output_label.configure(
            text=f"Минимальное число в списке: {result}", font=style["main_font"]
        )

    def reset(self):
        self.list_entry.delete(0, ctk.END)
        self.output_label.configure(text="")
