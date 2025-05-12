import customtkinter as ctk
from src.components.buttonComponent import buttonComponent
from styles import style


class Task9Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(
            self,
            text="Задание 9: Стоимость конфет",
            font=style["title_font"],
        )
        self.label.pack(pady=20, side="top")

        self.input_label = ctk.CTkLabel(
            self, text="Введите цену за 1 кг конфет:", font=style["main_font"]
        )
        self.input_label.pack(pady=5, side="top")

        self.input_entry = ctk.CTkEntry(self, width=400)
        self.input_entry.pack(pady=5, side="top")

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20, side="top")

        self.submit_button = buttonComponent(
            self.button_frame, text="Отправить", command=self.calculate_cost
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

    def calculate_cost(self):
        user_input = self.input_entry.get()

        try:
            price = float(user_input)
            result = []

            for kg in range(1, 11):
                cost = price * kg
                result.append(f"{kg} кг конфет стоит {round(cost, 3)}")

            self.output_label.configure(text="\n".join(result))

        except ValueError:
            self.output_label.configure(text="Пожалуйста, введите корректную цену.")

    def reset(self):
        self.input_entry.delete(0, ctk.END)
        self.output_label.configure(text="")
