import customtkinter as ctk
from src.components.buttonComponent import buttonComponent
from styles import style


class Task2Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(
            self,
            text="Задание 2: Режим сна Ани",
            font=style["title_font"],
        )
        self.label.pack(pady=20, side="top")

        self.input_label_a = ctk.CTkLabel(
            self,
            text="Введите минимальное количество часов сна A:",
            font=style["main_font"],
        )
        self.input_label_a.pack(pady=5, side="top")

        self.input_entry_a = ctk.CTkEntry(self, width=400)
        self.input_entry_a.pack(pady=5, side="top")

        self.input_label_b = ctk.CTkLabel(
            self,
            text="Введите максимальное количество часов сна B:",
            font=style["main_font"],
        )
        self.input_label_b.pack(pady=5, side="top")

        self.input_entry_b = ctk.CTkEntry(self, width=400)
        self.input_entry_b.pack(pady=5, side="top")

        self.input_label_h = ctk.CTkLabel(
            self, text="Введите количество часов сна H:", font=style["main_font"]
        )
        self.input_label_h.pack(pady=5, side="top")

        self.input_entry_h = ctk.CTkEntry(self, width=400)
        self.input_entry_h.pack(pady=5, side="top")

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20, side="top")

        self.submit_button = buttonComponent(
            self.button_frame, text="Проверить режим сна", command=self.submit
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

    def submit(self):
        try:
            a = int(self.input_entry_a.get())
            b = int(self.input_entry_b.get())
            h = int(self.input_entry_h.get())

            if a <= h <= b:
                self.output_label.configure(text="Это нормально")
            elif h < a:
                self.output_label.configure(text="Недосып")
            elif h > b:
                self.output_label.configure(text="Пересып")
        except ValueError:
            self.output_label.configure(text="Пожалуйста, введите корректные числа.")

    def reset(self):
        self.input_entry_a.delete(0, ctk.END)
        self.input_entry_b.delete(0, ctk.END)
        self.input_entry_h.delete(0, ctk.END)
        self.output_label.configure(text="")
