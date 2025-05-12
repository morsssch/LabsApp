import customtkinter as ctk
from prettytable import PrettyTable
from src.components.buttonComponent import buttonComponent
from styles import style


class Task8Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.default_string = (
            "ФИО;Возраст;Категория;"
            "_Иванов Иван Иванович;23 года;Студент 3 курса;"
            "_Петров Семен Игоревич;22 года;Студент 2 курса;"
            "_Иванов Семен Игоревич;22 года;Студент 2 курса;"
            "_Акибов Ярослав Наумович;23 года;Студент 3 курса;"
            "_Борков Станислав Максимович;21 год;Студент 1 курса;"
            "_Петров Семен Семенович;21 год;Студент 1 курса;"
            "_Романов Станислав Андреевич;23 года;Студент 3 курса;"
            "_Петров Всеволод Борисович;21 год;Студент 2 курса"
        )

        self.label = ctk.CTkLabel(
            self,
            text="Задание 8: Таблица студентов младше 22 лет",
            font=style["title_font"],
        )
        self.label.pack(pady=20)

        self.input_field = ctk.CTkTextbox(
            self, width=600, height=200, font=("Consolas", 12)
        )
        self.input_field.pack(padx=10, pady=10)
        self.input_field.insert("1.0", self.default_string)

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=10)

        self.submit_button = buttonComponent(
            self.button_frame, text="Сгенерировать таблицу", command=self.generate_table
        )
        self.submit_button.pack(side="left", padx=10)

        self.reset_button = buttonComponent(
            self.button_frame, text="Сбросить", command=self.reset
        )
        self.reset_button.pack(side="left", padx=10)

        self.output = ctk.CTkTextbox(self, width=600, height=200, font=("Consolas", 12))
        self.output.configure(state="disabled")
        self.output.pack(padx=10, pady=(10, 10))

    def generate_table(self):
        try:
            raw = self.input_field.get("1.0", "end").strip()
            data = raw.split(";")

            headers = [data[0], data[1], data[2]]
            rows = []
            i = 3
            while i < len(data):
                if data[i].startswith("_"):
                    age_text = data[i + 1]
                    if age_text.startswith("21"):
                        rows.append([data[i][1:], data[i + 1], data[i + 2]])
                    i += 3
                else:
                    raise ValueError(
                        "Нарушена структура данных. Ожидается символ '_' перед ФИО."
                    )

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
            self.output.insert("1.0", f"Ошибка: {str(e)}")
            self.output.configure(state="disabled")

    def reset(self):
        self.input_field.delete("1.0", "end")
        self.input_field.insert("1.0", self.default_string)
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.configure(state="disabled")
