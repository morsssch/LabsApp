import customtkinter as ctk
from prettytable import PrettyTable
from styles import style
from src.components.buttonComponent import buttonComponent


class Task2Frame(ctk.CTkFrame):
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
            text="Задание 2: Возведение элементов матрицы в квадрат",
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

        self.all_button = buttonComponent(
            self.button_frame, text="Возвести в квадрат", command=self.square_all
        )
        self.all_button.pack(side="left", padx=5)

        self.reset_button = buttonComponent(
            self.button_frame, text="Сбросить", command=self.reset
        )
        self.reset_button.pack(side="left", padx=5)

        self.output = ctk.CTkTextbox(self, width=480, height=200, font=("Consolas", 12))
        self.output.configure(state="disabled")
        self.output.pack(padx=10, pady=(10, 10))
        self.display_matrix()

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

    def display_matrix(self, matrix=None):
        if matrix is None:
            matrix = [
                list(map(int, line.split()))
                for line in self.default_matrix_string.strip().split("\n")
            ]

        table = PrettyTable()
        for row in matrix:
            table.add_row(row)
        table.header = False
        table.align = "l"
        table.border = False

        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", table.get_string())
        self.output.configure(state="disabled")

    def square_all(self):
        matrix = self.parse_matrix()
        if matrix is None:
            self.display_error()
            return
        result = [[val**2 for val in row] for row in matrix]
        self.display_matrix(result)

    def reset(self):
        self.input_field.delete("1.0", "end")
        self.input_field.insert("1.0", self.default_matrix_string)
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.display_matrix()
        self.output.configure(state="disabled")

    def display_error(self):
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", "Ошибка: Введите корректную матрицу")
        self.output.configure(state="disabled")
