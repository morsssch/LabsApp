import customtkinter as ctk
from src.components.buttonComponent import buttonComponent
from styles import style


class Task6Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(
            self,
            text="Задание 6: Каждый второй элемент + два дополнительных",
            font=style["title_font"],
        )
        self.label.pack(pady=20, side="top")

        self.input_label = ctk.CTkLabel(
            self, text="Введите список элементов через пробел:", font=style["main_font"]
        )
        self.input_label.pack(pady=5, side="top")

        self.input_entry = ctk.CTkEntry(self, width=400)
        self.input_entry.pack(pady=5, side="top")

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
            font=style["main_font"],
            wraplength=480,
            justify="left",
        )
        self.output_label.pack(pady=20, padx=10, ipady=10, ipadx=10, anchor="w")

    def submit(self):
        elements = self.input_entry.get().split()
        result = [elements[i] for i in range(1, len(elements), 2)]
        result.extend(["y", "z"])
        if result:
            self.output_label.configure(text=f"Результат: {result}")
        else: self.output_label.configure(text="Ошибка: введите строку")

    def reset(self):
        self.input_entry.delete(0, ctk.END)
        self.output_label.configure(text="")
