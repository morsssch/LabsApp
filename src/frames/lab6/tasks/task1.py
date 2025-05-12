import customtkinter as ctk
from src.components.buttonComponent import buttonComponent
from styles import style


class Task1Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)

        self.label = ctk.CTkLabel(
            self, text="Задание 1: Подсчет ключей в словаре", font=style["title_font"]
        )
        self.label.pack(pady=20, side="top")

        self.input_label = ctk.CTkLabel(
            self,
            text="Введите словарь:",
            font=style["main_font"],
        )
        self.input_label.pack(pady=5, side="top")

        self.input_field = ctk.CTkTextbox(
            self, width=560, height=100, font=("Consolas", 12)
        )
        self.input_field.insert("1.0", "{'a': 1, 'b': 2, 'c': 3}")
        self.input_field.pack(pady=10, padx=10)

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20, side="top")

        self.submit_button = buttonComponent(
            self.button_frame, text="Отправить", command=self.count_keys
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

    def count_keys(self):
        try:
            input_text = self.input_field.get("1.0", "end").strip()
            dictionary = eval(input_text)
            if not isinstance(dictionary, dict):
                raise ValueError("Введенные данные не являются словарем")
            count = len(dictionary)
            self.output_label.configure(text=f"Количество ключей в словаре: {count}")
        except Exception as e:
            self.output_label.configure(text=f"Ошибка: {str(e)}")

    def reset(self):
        self.input_field.delete("1.0", ctk.END)
        self.input_field.insert("1.0", "{'a': 1, 'b': 2, 'c': 3}")
        self.output_label.configure(text="")
