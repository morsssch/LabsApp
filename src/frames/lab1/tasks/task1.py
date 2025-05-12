import customtkinter as ctk
from src.components.buttonComponent import buttonComponent
from styles import style


class Task1Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        items_pady = 5

        self.label = ctk.CTkLabel(
            self, text="Задание 1: Анкета", font=style["title_font"]
        )
        self.label.pack(pady=20, side="top")

        self.name_label = ctk.CTkLabel(
            self, text="Как Вас зовут?", font=style["main_font"]
        )
        self.name_label.pack(pady=items_pady, side="top")
        self.name_entry = ctk.CTkEntry(self, width=400)
        self.name_entry.pack(pady=items_pady, side="top")

        self.university_label = ctk.CTkLabel(
            self,
            text="Укажите название ВУЗа, в котором вы обучаетесь:",
            font=style["main_font"],
        )
        self.university_label.pack(pady=items_pady, side="top")
        self.university_entry = ctk.CTkEntry(self, width=400)
        self.university_entry.pack(pady=items_pady, side="top")

        self.group_name_label = ctk.CTkLabel(
            self, text="Укажите номер вашей группы:", font=style["main_font"]
        )
        self.group_name_label.pack(pady=items_pady, side="top")
        self.group_name_entry = ctk.CTkEntry(self, width=400)
        self.group_name_entry.pack(pady=items_pady, side="top")

        self.lang_label = ctk.CTkLabel(
            self,
            text="Какой язык программирования вы начинаете изучать?",
            font=style["main_font"],
        )
        self.lang_label.pack(pady=items_pady, side="top")
        self.lang_entry = ctk.CTkEntry(self, width=400)
        self.lang_entry.pack(pady=items_pady, side="top")

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20, side="top")

        self.submit_button = buttonComponent(
            self.button_frame, text="Отправить", command=self.submit
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
            font=("Arial", 12),
            wraplength=480,
            justify="left",
        )
        self.output_label.pack(pady=20, padx=10, ipady=10, ipadx=10, anchor="w")

    def submit(self):
        name = self.name_entry.get()
        university = self.university_entry.get()
        group_name = self.group_name_entry.get()
        lang = self.lang_entry.get()

        if not name:
            self.output_label.configure(
                text="Ошибка: Пожалуйста, введите ваше имя.", font=style["main_font"]
            )
            return
        if not university:
            self.output_label.configure(
                text="Ошибка: Пожалуйста, введите название университета."
            )
            return
        if not group_name:
            self.output_label.configure(
                text="Ошибка: Пожалуйста, введите вашу группу", font=style["main_font"]
            )
            return
        if not lang:
            self.output_label.configure(
                text="Ошибка: Пожалуйста, введите язык программирования.",
                font=style["main_font"],
            )
            return

        self.output_label.configure(
            text=f"Добрый день, {name}\n"
            f"Вы обучаетесь в образовательной организации {university} в группе {group_name}\n"
            f"{name}, желаем Вам успешного обучения программированию на языке {lang}",
            font=style["main_font"],
        )

    def reset(self):
        self.name_entry.delete(0, ctk.END)
        self.university_entry.delete(0, ctk.END)
        self.group_name_entry.delete(0, ctk.END)
        self.lang_entry.delete(0, ctk.END)
        self.output_label.configure(text="")
