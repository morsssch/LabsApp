import customtkinter as ctk
from styles import style
from src.components.buttonComponent import buttonComponent


class Task3Frame(ctk.CTkFrame):
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
            self,
            text="Задание 3: Сложение элементов матрицы",
            font=style["title_font"],
        )
        self.label.pack(pady=(10, 5))

        self.input_field = ctk.CTkTextbox(
            self, width=480, height=160, font=("Consolas", 12)
        )
        self.input_field.insert("1.0", self.default_matrix_string)
        self.input_field.pack(pady=10, padx=10)

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=0)

        self.sum_rows_button = buttonComponent(
            self.button_frame, text="Сумма по строкам", command=self.sum_by_rows
        )
        self.sum_rows_button.pack(side="left", padx=5)

        self.reset_button = buttonComponent(
            self.button_frame, text="Сбросить", command=self.reset
        )
        self.reset_button.pack(side="left", padx=5)

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

    def parse_matrix(self):
        try:
            lines = self.input_field.get("1.0", "end").strip().split("\n")
            if not lines or all(line.strip() == "" for line in lines):
                return None
            matrix = [list(map(int, line.split())) for line in lines]

            if len(set(len(row) for row in matrix)) > 1:
                raise ValueError(
                    "Каждая строка должна содержать одинаковое количество чисел."
                )

            return matrix
        except Exception:
            return None

    def update_output(self, text):
        self.output_label.configure(text=text)

    def sum_by_rows(self):
        matrix = self.parse_matrix()
        if matrix is None:
            self.display_error("Ошибка: Введите корректную матрицу")
            return
        result = [sum(row) for row in matrix]
        self.update_output(f"Суммы по строкам:\n{', '.join(map(str, result))}")

    def reset(self):
        self.input_field.delete("1.0", "end")
        self.input_field.insert("1.0", self.default_matrix_string)
        self.update_output("")

    def display_error(self, message):
        self.output_label.configure(text=message)
