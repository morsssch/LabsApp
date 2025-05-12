import customtkinter as ctk
from src.components.buttonComponent import buttonComponent
from styles import style


class Task2Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        items_pady = 5

        self.label = ctk.CTkLabel(
            self, text="Задание 2: Вычисление", font=style["title_font"]
        )
        self.label.pack(pady=20, side="top")

        self.a_label = ctk.CTkLabel(
            self, text="Введите число a:", font=style["main_font"]
        )
        self.a_label.pack(pady=items_pady, side="top")
        self.a_entry = ctk.CTkEntry(self, width=400)
        self.a_entry.pack(pady=items_pady, side="top")

        self.b_label = ctk.CTkLabel(
            self, text="Введите число b:", font=style["main_font"]
        )
        self.b_label.pack(pady=items_pady, side="top")
        self.b_entry = ctk.CTkEntry(self, width=400)
        self.b_entry.pack(pady=items_pady, side="top")

        self.c_label = ctk.CTkLabel(
            self, text="Введите число c:", font=style["main_font"]
        )
        self.c_label.pack(pady=items_pady, side="top")
        self.c_entry = ctk.CTkEntry(self, width=400)
        self.c_entry.pack(pady=items_pady, side="top")

        self.d_label = ctk.CTkLabel(
            self, text="Введите число d:", font=style["main_font"]
        )
        self.d_label.pack(pady=items_pady, side="top")
        self.d_entry = ctk.CTkEntry(self, width=400)
        self.d_entry.pack(pady=items_pady, side="top")

        self.k_label = ctk.CTkLabel(
            self, text="Введите число k:", font=style["main_font"]
        )
        self.k_label.pack(pady=items_pady, side="top")
        self.k_entry = ctk.CTkEntry(self, width=400)
        self.k_entry.pack(pady=items_pady, side="top")

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20, side="top")

        self.calculate_button = buttonComponent(
            self.button_frame, text="Вычислить", command=self.calculate
        )
        self.calculate_button.pack(side="left", padx=10)

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

    def calculate(self):
        try:

            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())
            d = float(self.d_entry.get())
            k = float(self.k_entry.get())

            if b == 0 or a == 0:
                self.output_label.configure(
                    text="Ошибка: деление на ноль.", font=style["main_font"]
                )
                return

            result = abs(
                (
                    (a**2 - b**3 - c**3 * a**2) * (b - c + c * (k - d / b**3))
                    - (k / b - k / a) * c
                )
                ** 2
                - 20000
            )

            self.output_label.configure(
                text=f"Результат вычисления: {round(result, 2)}",
                font=style["main_font"],
            )
        except ValueError:
            self.output_label.configure(
                text="Ошибка: Пожалуйста, введите корректные числа.",
                font=style["main_font"],
            )

    def reset(self):
        self.a_entry.delete(0, ctk.END)
        self.b_entry.delete(0, ctk.END)
        self.c_entry.delete(0, ctk.END)
        self.d_entry.delete(0, ctk.END)
        self.k_entry.delete(0, ctk.END)
        self.output_label.configure(text="")
