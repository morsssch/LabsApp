import customtkinter as ctk
from src.components.buttonComponent import buttonComponent
from styles import style


class Task9Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(
            self,
            text="Задание 9: Подсчёт гласных и согласных в названии команды",
            font=style["title_font"],
        )
        self.label.pack(pady=20, side="top")

        self.input_label = ctk.CTkLabel(
            self, text="Введите название футбольной команды:", font=style["main_font"]
        )
        self.input_label.pack(pady=5, side="top")

        self.input_field = ctk.CTkEntry(self, width=400, font=("Consolas", 12))
        self.input_field.pack(pady=5, side="top")

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20, side="top")

        self.submit_button = buttonComponent(
            self.button_frame, text="Подсчитать", command=self.count_letters
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

    def count_letters(self):
        name = self.input_field.get()
        vowels = 0
        cons = 0

        for i in name:
            i = i.lower()
            if i in "ауоиэыяюеё":
                vowels += 1
            elif i in "бвгджзйклмнпрстфхцчшщ":
                cons += 1

        if name:
            self.output_label.configure(
                text=f'Футбольная команда "{name}" имеет длину {len(name)} символов, '
                f"количество гласных букв = {vowels}, количество согласных букв = {cons}"
            )
        else:
            self.output_label.configure(text="Ошибка: введите название команды")

    def reset(self):
        self.input_field.delete(0, "end")
        self.output_label.configure(text="")
