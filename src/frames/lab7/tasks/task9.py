import customtkinter as ctk
from styles import style
from src.components.buttonComponent import buttonComponent


class Task9Frame(ctk.CTkFrame):
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
            text="Задание 9: Найти элемент по координатам",
            font=style["title_font"],
        )
        self.label.pack(pady=(10, 5))

        self.input_field = ctk.CTkTextbox(
            self, width=480, height=160, font=("Consolas", 12)
        )
        self.input_field.insert("1.0", self.default_matrix_string)
        self.input_field.pack(pady=10, padx=10)

        self.coords_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.coords_frame.pack(pady=(5, 5))

        self.row_label = ctk.CTkLabel(
            self.coords_frame, text="Строка:", font=style["main_font"]
        )
        self.row_label.pack(side="left", padx=5)
        self.row_entry = ctk.CTkEntry(self.coords_frame, width=50)
        self.row_entry.pack(side="left", padx=5)

        self.col_label = ctk.CTkLabel(
            self.coords_frame, text="Столбец:", font=style["main_font"]
        )
        self.col_label.pack(side="left", padx=5)
        self.col_entry = ctk.CTkEntry(self.coords_frame, width=50)
        self.col_entry.pack(side="left", padx=5)

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=5)

        self.find_button = buttonComponent(
            self.button_frame, text="Найти", command=self.find_value
        )
        self.find_button.pack(side="left", padx=5)

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
            matrix = [list(map(int, line.strip().split())) for line in lines]
            if len(set(len(row) for row in matrix)) > 1:
                raise ValueError("Разная длина строк.")
            return matrix
        except Exception:
            return None

    def find_value(self):
        matrix = self.parse_matrix()
        if matrix is None:
            self.output_label.configure(text="Ошибка: Неверный формат матрицы.")
            return

        try:
            row = int(self.row_entry.get()) - 1
            col = int(self.col_entry.get()) - 1
        except ValueError:
            self.output_label.configure(text="Ошибка: Введите числовые индексы.")
            return

        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            self.output_label.configure(text="Ошибка: Индексы вне диапазона.")
            return

        value = matrix[row][col]
        self.output_label.configure(
            text=f"Значение в позиции ({row + 1}, {col + 1}): {value}"
        )

    def reset(self):
        self.input_field.delete("1.0", "end")
        self.input_field.insert("1.0", self.default_matrix_string)
        self.row_entry.delete(0, ctk.END)
        self.col_entry.delete(0, ctk.END)
        self.output_label.configure(text="")
