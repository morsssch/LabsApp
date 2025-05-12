import customtkinter as ctk
from src.components.buttonComponent import buttonComponent
from styles import style


class Task11Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(
            self, text="Задание 11: Сортировка слов", font=style["title_font"]
        )
        self.label.pack(pady=20, side="top")

        self.input_label = ctk.CTkLabel(
            self, text="Введите три слова для сортировки:", font=style["main_font"]
        )
        self.input_label.pack(pady=5, side="top")

        self.input_field1 = ctk.CTkEntry(self, width=400, font=("Consolas", 12))
        self.input_field1.pack(pady=5, side="top")

        self.input_field2 = ctk.CTkEntry(self, width=400, font=("Consolas", 12))
        self.input_field2.pack(pady=5, side="top")

        self.input_field3 = ctk.CTkEntry(self, width=400, font=("Consolas", 12))
        self.input_field3.pack(pady=5, side="top")

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20, side="top")

        self.submit_button = buttonComponent(
            self.button_frame, text="Сортировать", command=self.sort_words
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

    def sort_words(self):
        words = [
            self.input_field1.get(),
            self.input_field2.get(),
            self.input_field3.get(),
        ]
        if all(words):
            words.sort()
            self.output_label.configure(
                text=f"Отсортированные слова: {', '.join(words)}"
            )
        else:
            self.output_label.configure(text="Ошибка: заполните все поля")

    def reset(self):
        self.input_field1.delete(0, "end")
        self.input_field2.delete(0, "end")
        self.input_field3.delete(0, "end")
        self.output_label.configure(text="")
