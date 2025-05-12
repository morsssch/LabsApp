import customtkinter as ctk
import csv
import os
from prettytable import PrettyTable
from styles import style
from src.components.buttonComponent import buttonComponent


class Task3Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)

        self.default_data = [
            ["№", "ФИО", "Возраст", "Группа", "Номер телефона", "Email"],
            [
                "1",
                "Иванов Иван Иванович",
                "23",
                "БО-11",
                "+7998-676-2532",
                "todd@gmail.com",
            ],
            [
                "2",
                "Сидоров Семен Семенович",
                "21",
                "БО-11",
                "233-421-32",
                "s.sidorov@gmail.com",
            ],
            [
                "3",
                "Яшков Илья Петрович",
                "24",
                "БО-22",
                "+7445-341-0545",
                "i.yashkov@yandex.ru",
            ],
            [
                "4",
                "Смирнов Андрей Петрович",
                "22",
                "БО-21",
                "243-541-654",
                "smirnov_a@yandex.ru",
            ],
            ["5", "Петров Петр Семенович", "21", "БО-11", "245-721-62", ""],
            [
                "6",
                "Селиванов Ян Андреевич",
                "22",
                "БО-12",
                "+7495-341-0548",
                "i.yashkov@yandex.ru",
            ],
            ["7", "Королев Иван Петрович", "23", "БО-23", "243-541-658", ""],
        ]

        self.label = ctk.CTkLabel(
            self,
            text="Задание 3: Изменение возраста отфильтрованных студентов",
            font=style["title_font"],
        )
        self.label.pack(pady=(10, 5))

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=10)

        self.increase_button = buttonComponent(
            self.button_frame,
            text="Увеличить возраст",
            command=lambda: self.modify_ages(1),
        )
        self.increase_button.pack(side="left", padx=(0, 10))

        self.decrease_button = buttonComponent(
            self.button_frame,
            text="Уменьшить возраст",
            command=lambda: self.modify_ages(-1),
        )
        self.decrease_button.pack(side="left", padx=10)

        self.refresh_button = buttonComponent(
            self.button_frame, text="Обновить", command=self.refresh_table
        )
        self.refresh_button.pack(side="left", padx=10)

        self.reset_button = buttonComponent(
            self.button_frame, text="Сбросить", command=self.reset
        )
        self.reset_button.pack(side="left", padx=10)

        self.output = ctk.CTkTextbox(self, width=560, height=180, font=("Consolas", 12))
        self.output.configure(state="disabled")
        self.output.pack(padx=10, pady=(10, 10))

        os.makedirs("src/assets", exist_ok=True)
        if not os.path.exists("src/assets/students.csv"):
            self.save_to_file(self.default_data)

        self.display_table()

    def save_to_file(self, data):
        try:
            with open(
                "src/assets/students.csv", "w", encoding="utf-8", newline=""
            ) as f:
                writer = csv.writer(f, delimiter=";")
                writer.writerows(data)
        except Exception as e:
            self.show_error(f"Ошибка при сохранении файла: {str(e)}")

    def load_filtered_students(self):
        students_dict = {}
        with open("src/assets/students.csv", "r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f, delimiter=";")
            headers = next(reader)
            for row in reader:
                if len(row) == len(headers):
                    students_dict[row[0]] = row[1:]

        filtered_students = [
            [no] + info
            for no, info in students_dict.items()
            if info[2].endswith("1") and info[1].strip()
        ]

        filtered_students.sort(key=lambda x: int(x[2]) if x[2].strip() else 0)
        return headers, filtered_students

    def display_table(self):
        try:
            headers, filtered_students = self.load_filtered_students()

            table = PrettyTable(headers)
            for student in filtered_students:
                table.add_row(student)

            table.align = "l"
            table.border = False

            self.output.configure(state="normal")
            self.output.delete("1.0", "end")
            self.output.insert("1.0", table.get_string())
            self.output.configure(state="disabled")

        except Exception as e:
            self.show_error(f"Ошибка: {str(e)}")

    def refresh_table(self):
        try:
            self.display_table()
        except Exception as e:
            self.show_error(f"Ошибка при обновлении: {str(e)}")

    def modify_ages(self, change):
        try:
            students_dict = {}
            with open(
                "src/assets/students.csv", "r", encoding="utf-8", newline=""
            ) as f:
                reader = csv.reader(f, delimiter=";")
                headers = next(reader)
                for row in reader:
                    if len(row) == len(headers):
                        students_dict[row[0]] = row[1:]

            filtered_numbers = [
                no
                for no, info in students_dict.items()
                if info[2].endswith("1") and info[1].strip()
            ]

            modified_students = []
            for row in [headers] + [[no] + info for no, info in students_dict.items()]:
                if row[0] in filtered_numbers:
                    age = int(row[2]) + change if row[0] != headers[0] else row[2]
                    if age < 0:
                        raise ValueError("Возраст не может быть отрицательным")
                    row[2] = str(age)
                modified_students.append(row)

            self.save_to_file(modified_students)
            self.display_table()

        except Exception as e:
            self.show_error(f"Ошибка: {str(e)}")

    def reset(self):
        try:
            self.save_to_file(self.default_data)
            self.display_table()
        except Exception as e:
            self.show_error(f"Ошибка: {str(e)}")

    def show_error(self, message):
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", message)
        self.output.configure(state="disabled")
