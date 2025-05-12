import customtkinter as ctk
import csv
import os
from prettytable import PrettyTable
from styles import style
from src.components.buttonComponent import buttonComponent
import tkinter.filedialog as filedialog


class Task2Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.default_data = (
            "№;ФИО;Возраст;Группа\n"
            "1;Иванов Иван Иванович;23;БО-111111\n"
            "2;Сидоров Семен Семенович;23;БО-111111\n"
            "3;Яшков Илья Петрович;24;БО-222222"
        )

        self.label = ctk.CTkLabel(
            self,
            text="Задание 2: Сортировка студентов по фамилии",
            font=style["title_font"],
        )
        self.label.pack(pady=(10, 5))

        initial_data = self.load_initial_data()
        self.input_field = ctk.CTkTextbox(
            self, width=560, height=100, font=("Consolas", 12)
        )
        self.input_field.insert("1.0", initial_data)
        self.input_field.pack(pady=10, padx=10)

        self.input_field.bind("<KeyRelease>", self.save_on_change)

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=0)

        self.generate_button = buttonComponent(
            self.button_frame, text="Отправить", command=self.generate_table
        )
        self.generate_button.pack(side="left", padx=(0, 10))

        self.upload_button = buttonComponent(
            self.button_frame, text="Загрузить файл", command=self.upload_file
        )
        self.upload_button.pack(side="left", padx=10)

        self.refresh_button = buttonComponent(
            self.button_frame, text="Обновить", command=self.refresh_table
        )
        self.refresh_button.pack(side="left", padx=10)

        self.reset_button = buttonComponent(
            self.button_frame, text="Сбросить", command=self.reset
        )
        self.reset_button.pack(side="left")

        self.output = ctk.CTkTextbox(self, width=560, height=180, font=("Consolas", 12))
        self.output.configure(state="disabled")
        self.output.pack(padx=10, pady=(10, 10))

        os.makedirs("src/assets", exist_ok=True)

        self.save_to_file(initial_data)

    def load_initial_data(self):
        """Load data from file if exists, otherwise return default data"""
        file_path = "src/assets/students.csv"
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    return f.read()
            except:
                return self.default_data
        return self.default_data

    def save_to_file(self, content):
        try:
            with open(
                "src/assets/students.csv", "w", encoding="utf-8", newline=""
            ) as f:
                f.write(content)
        except Exception as e:
            self.show_error(f"Ошибка при сохранении файла: {str(e)}")

    def save_on_change(self):
        content = self.input_field.get("1.0", "end").strip()
        self.save_to_file(content)

    def generate_table(self):
        try:
            input_text = self.input_field.get("1.0", "end").strip()
            self.save_to_file(input_text)

            students = []
            with open(
                "src/assets/students.csv", "r", encoding="utf-8", newline=""
            ) as f:
                reader = csv.reader(f, delimiter=";")
                headers = next(reader)
                for row in reader:
                    if len(row) == len(headers):
                        students.append(row)

            students.sort(key=lambda x: x[1].split()[0])

            table = PrettyTable(headers)
            for student in students:
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
            content = self.load_initial_data()
            self.input_field.delete("1.0", "end")
            self.input_field.insert("1.0", content)
        except Exception as e:
            self.show_error(f"Ошибка при обновлении: {str(e)}")

    def upload_file(self):
        try:
            file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
            if file_path:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                self.input_field.delete("1.0", "end")
                self.input_field.insert("1.0", content)
                self.save_to_file(content)
                self.generate_table()

        except Exception as e:
            self.show_error(f"Ошибка при загрузке файла: {str(e)}")

    def reset(self):
        self.input_field.delete("1.0", "end")
        self.input_field.insert("1.0", self.default_data)
        self.save_to_file(self.default_data)
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.configure(state="disabled")

    def show_error(self, message):
        """Display error message in output textbox"""
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", message)
        self.output.configure(state="disabled")
