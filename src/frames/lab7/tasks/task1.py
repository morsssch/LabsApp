import customtkinter as ctk
from src.components.buttonComponent import buttonComponent
from styles import style


class Task1Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.default_matrix_string = (
            "1 2 3 4 5 6 7 8\n"
            "8 7 6 5 4 3 2 1\n"
            "2 3 4 5 6 7 8 9\n"
            "9 8 7 6 5 4 3 2\n"
            "1 3 5 7 9 2 4 6\n"
            "3 5 7 9 1 2 4 6\n"
            "1 7 5 9 3 2 4 6\n"
            "2 3 4 5 6 7 8 9"
        )

        self.label = ctk.CTkLabel(
            self, text="Задание 1: Сумма элементов матрицы", font=style["title_font"]
        )
        self.label.pack(pady=20)

        self.input_label = ctk.CTkLabel(
            self,
            text="Введите матрицу (строки через перенос строки, числа через пробел):",
            font=style["main_font"],
        )
        self.input_label.pack()

        self.input_textbox = ctk.CTkTextbox(
            self, width=480, height=160, font=("Consolas", 12)
        )
        self.input_textbox.insert("1.0", self.default_matrix_string)
        self.input_textbox.pack(pady=10)

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack()

        self.calc_button = buttonComponent(
            self.button_frame, text="Посчитать сумму", command=self.calculate_sum
        )
        self.calc_button.pack(side="left", padx=10)

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

    def calculate_sum(self):
        input_text = self.input_textbox.get("1.0", "end").strip()
        try:
            matrix = []
            for line in input_text.splitlines():
                if not line.strip():
                    continue
                numbers = list(map(int, line.strip().split()))
                matrix.append(numbers)

            if len(set(len(row) for row in matrix)) > 1:
                raise ValueError(
                    "Каждая строка должна содержать одинаковое количество чисел."
                )

            total = sum(sum(row) for row in matrix)
            self.output_label.configure(text=f"Сумма всех элементов: {total}")

        except Exception as e:
            self.output_label.configure(text=f"Ошибка: {str(e)}")

    def reset(self):
        self.input_textbox.delete("1.0", "end")
        self.input_textbox.insert("1.0", self.default_matrix_string)
        self.output_label.configure(text="")
