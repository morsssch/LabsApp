import customtkinter as ctk
from prettytable import PrettyTable
from styles import style
from src.components.buttonComponent import buttonComponent


class Task7Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.my_string_default = (
            "Ф;И;О;Возраст;Категория;"
            "_Иванов;Иван;Иванович;23 года;Студент 3 курса;"
            "_Петров;Семен;Игоревич;22 года;Студент 2 курса"
        )

        self.label = ctk.CTkLabel(
            self, text="Задание 7: Таблица студентов", font=style["title_font"]
        )
        self.label.pack(pady=(10, 5))

        self.input_field = ctk.CTkTextbox(self, width=480, height=100)
        self.input_field.insert("1.0", self.my_string_default)
        self.input_field.pack(pady=10, padx=10)

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=0)

        self.generate_button = buttonComponent(
            self.button_frame, text="Сгенерировать таблицу", command=self.generate_table
        )
        self.generate_button.pack(side="left", padx=(0, 10))

        self.reset_button = buttonComponent(
            self.button_frame, text="Сбросить", command=self.reset
        )
        self.reset_button.pack(side="left")

        self.output = ctk.CTkTextbox(self, width=480, height=180)
        self.output.configure(state="disabled")
        self.output.pack(padx=10, pady=(10, 10))

    def generate_table(self):
        input_text = self.input_field.get("1.0", "end").strip()

        try:
            data = input_text.split(";")

            headers = [
                (data[0] + data[1] + data[2]).center(max(len(x) for x in data)),
                data[3],
                data[4],
            ]

            rows = []
            i = 5
            while i < len(data):
                if data[i].startswith("_"):
                    rows.append(
                        [
                            f"{data[i][1:]} {data[i+1]} {data[i+2]}",
                            data[i + 3],
                            data[i + 4],
                        ]
                    )
                    i += 5
                else:
                    raise ValueError("Ошибка синтаксиса")

            table = PrettyTable(headers)
            for row in rows:
                table.add_row(row)

            table.align = "l"
            table.border = False

            self.output.configure(state="normal")
            self.output.delete("1.0", "end")
            self.output.insert("1.0", table.get_string())
            self.output.configure(state="disabled")

        except Exception as e:
            self.output.configure(state="normal")
            self.output.delete("1.0", "end")
            self.output.insert("1.0", f"{str(e)}")
            self.output.configure(state="disabled")

    def reset(self):
        self.input_field.delete("1.0", "end")
        self.input_field.insert("1.0", self.my_string_default)
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.configure(state="disabled")
