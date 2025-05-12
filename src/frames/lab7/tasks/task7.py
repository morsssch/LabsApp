import customtkinter as ctk
from prettytable import PrettyTable
from styles import style
from src.components.buttonComponent import buttonComponent


class Task7Frame(ctk.CTkFrame):
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
            text="Задание 7: Удалить строку с указанным номером",
            font=style["title_font"],
        )
        self.label.pack(pady=(10, 5))

        self.input_field = ctk.CTkTextbox(
            self, width=480, height=160, font=("Consolas", 12)
        )
        self.input_field.insert("1.0", self.default_matrix_string)
        self.input_field.pack(pady=(5, 10), padx=10)

        self.row_number_input = ctk.CTkEntry(
            self,
            width=400,
            placeholder_text="Введите номер строки (от 1)",
            font=style["main_font"],
            corner_radius=5,
            border_width=2,
            border_color="gray",
        )

        self.row_number_input.pack(pady=(0, 10))

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=0)

        self.delete_button = buttonComponent(
            self.button_frame, text="Удалить строку", command=self.delete_row
        )
        self.delete_button.pack(side="left", padx=5)

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

    def delete_row(self):
        matrix = self.parse_matrix()
        if matrix is None:
            self.display_error("Ошибка: Введите корректную матрицу")
            return

        try:
            row_str = self.row_number_input.get().strip()
            if not row_str.isdigit():
                raise ValueError("Введите число")

            row_number = int(row_str) - 1
            if not (0 <= row_number < len(matrix)):
                raise ValueError(f"Введите число от 1 до {len(matrix)}")

            matrix.pop(row_number)
            self.display_matrix(matrix)

        except ValueError as e:
            self.display_error(f"Ошибка: {e}")

    def reset(self):
        self.input_field.delete("1.0", "end")
        self.input_field.insert("1.0", self.default_matrix_string)
        self.row_number_input.delete(0, "end")
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.display_matrix()
        self.output.configure(state="disabled")

    def display_error(self, message):
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", message)
        self.output.configure(state="disabled")
