import customtkinter as ctk
import csv
import os
from prettytable import PrettyTable
from styles import style
from src.components.buttonComponent import buttonComponent
from tkinter import filedialog


class Task4Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(
            self,
            text="Задание 4: Просмотр и скачивание students.csv",
            font=style["title_font"],
        )
        self.label.pack(pady=(10, 5))

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=10)

        self.download_button = buttonComponent(
            self.button_frame,
            text="Скачать CSV",
            command=self.download_csv,
        )
        self.download_button.pack(side="left", padx=10)

        self.refresh_button = buttonComponent(
            self.button_frame, text="Обновить", command=self.refresh_table
        )
        self.refresh_button.pack(side="left", padx=10)

        self.output = ctk.CTkTextbox(self, width=560, height=180, font=("Consolas", 12))
        self.output.configure(state="disabled")
        self.output.pack(padx=10, pady=(10, 10))

        os.makedirs("src/assets", exist_ok=True)

        self.display_table()

    def display_table(self):
        try:
            students = []
            with open(
                "src/assets/students.csv", "r", encoding="utf-8", newline=""
            ) as f:
                reader = csv.reader(f, delimiter=";")
                headers = next(reader)
                for row in reader:
                    if len(row) == len(headers):
                        students.append(row)

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
            self.display_table()
        except Exception as e:
            self.show_error(f"Ошибка при обновлении: {str(e)}")

    def download_csv(self):
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv")],
                initialfile="students.csv",
                title="Сохранить CSV файл",
            )
            if file_path:
                with open("src/assets/students.csv", "r", encoding="utf-8") as source:
                    with open(file_path, "w", encoding="utf-8", newline="") as dest:
                        dest.write(source.read())
        except Exception as e:
            self.show_error(f"Ошибка при скачивании: {str(e)}")

    def show_error(self, message):
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", message)
        self.output.configure(state="disabled")
