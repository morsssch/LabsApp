import customtkinter as ctk
from src.components.buttonComponent import buttonComponent
from styles import style


class Task1Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        items_pady = 5

        self.label = ctk.CTkLabel(
            self, text="Задание 1: Угадай число", font=style["title_font"]
        )
        self.label.pack(pady=20, side="top")

        self.my_number_label = ctk.CTkLabel(
            self, text="Введите предустановленное число:", font=style["main_font"]
        )
        self.my_number_label.pack(pady=items_pady, side="top")
        self.my_number_entry = ctk.CTkEntry(self, width=400)
        self.my_number_entry.pack(pady=items_pady, side="top")

        self.user_number_label = ctk.CTkLabel(
            self, text="Введите ваше число:", font=style["main_font"]
        )
        self.user_number_label.pack(pady=items_pady, side="top")
        self.user_number_entry = ctk.CTkEntry(self, width=400)
        self.user_number_entry.pack(pady=items_pady, side="top")

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20, side="top")

        self.submit_button = buttonComponent(
            self.button_frame, text="Проверить", command=self.check_number
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

    def check_number(self):
        try:
            my_number = int(self.my_number_entry.get())
            user_number = int(self.user_number_entry.get())
        except ValueError:
            self.output_label.configure(
                text="Ошибка: Пожалуйста, введите корректные числа.",
                font=style["main_font"],
            )
            return

        if my_number == user_number:
            self.output_label.configure(
                text=f"Число пользователя {user_number} оказалось равно предустановленному числу {my_number}!",
                font=style["main_font"],
            )
        else:
            self.output_label.configure(
                text="Попробуйте ещё раз", font=style["main_font"]
            )

    def reset(self):
        self.my_number_entry.delete(0, ctk.END)
        self.user_number_entry.delete(0, ctk.END)
        self.output_label.configure(text="")
