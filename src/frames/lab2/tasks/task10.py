import customtkinter as ctk
import re
from src.components.buttonComponent import buttonComponent
from styles import style


class Task10Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(
            self,
            text="Задание 10: Проверка правильности госномера",
            font=style["title_font"],
        )
        self.label.pack(pady=20, side="top")

        self.input_label = ctk.CTkLabel(
            self, text="Введите госномер:", font=style["main_font"]
        )
        self.input_label.pack(pady=5, side="top")

        self.input_field = ctk.CTkEntry(self, width=400, font=("Consolas", 12))
        self.input_field.pack(pady=5, side="top")

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20, side="top")

        self.submit_button = buttonComponent(
            self.button_frame, text="Проверить", command=self.check_car_number
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

    def check_car_number(self):
        car_num = self.input_field.get()
        regex = re.findall(
            r"[АВЕКМНОРСТУХавекмнорстух]{1}[0-9]{3}[АВЕКМНОРСТУХавекмнорстух]{2}_[0-9]{2,3}",
            car_num,
        )
        is_valid = bool(regex)
        if car_num:
            self.output_label.configure(
                text=f"Госномер {car_num} {'валиден' if is_valid else 'невалиден'}"
            )
        else:
            self.output_label.configure(text="Ошибка: введите госномер")

    def reset(self):
        self.input_field.delete(0, "end")
        self.output_label.configure(text="")
