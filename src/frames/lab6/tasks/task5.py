import customtkinter as ctk
from src.components.buttonComponent import buttonComponent
from styles import style


class Task5Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)

        items_pady = 5

        self.label = ctk.CTkLabel(
            self, text="Задание 4: Общие символы двух строк", font=style["title_font"]
        )
        self.label.pack(pady=20, side="top")

        self.first_string_label = ctk.CTkLabel(
            self, text="Введите первую строку:", font=style["main_font"]
        )
        self.first_string_label.pack(pady=items_pady, side="top")
        self.first_string_entry = ctk.CTkEntry(self, width=400)
        self.first_string_entry.insert(0, "")
        self.first_string_entry.pack(pady=items_pady, side="top")

        self.second_string_label = ctk.CTkLabel(
            self, text="Введите вторую строку:", font=style["main_font"]
        )
        self.second_string_label.pack(pady=items_pady, side="top")
        self.second_string_entry = ctk.CTkEntry(self, width=400)
        self.second_string_entry.insert(0, "")
        self.second_string_entry.pack(pady=items_pady, side="top")

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20, side="top")

        self.submit_button = buttonComponent(
            self.button_frame, text="Проверить", command=self.find_common_chars
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

    def find_common_chars(self):
        try:
            first_string = self.first_string_entry.get().strip()
            second_string = self.second_string_entry.get().strip()

            if not first_string or not second_string:
                raise ValueError("Обе строки должны быть непустыми")

            common_chars = sorted(set(first_string) & set(second_string))

            if common_chars:
                self.output_label.configure(
                    text=f"Общие символы в порядке возрастания:\n{', '.join(common_chars)}",
                    font=style["main_font"],
                )
            else:
                self.output_label.configure(
                    text="Нет общих символов", font=style["main_font"]
                )

        except Exception as e:
            self.output_label.configure(
                text=f"Ошибка: {str(e)}", font=style["main_font"]
            )

    def reset(self):
        self.first_string_entry.delete(0, ctk.END)
        self.first_string_entry.insert(0, "")
        self.second_string_entry.delete(0, ctk.END)
        self.second_string_entry.insert(0, "")
        self.output_label.configure(text="")
