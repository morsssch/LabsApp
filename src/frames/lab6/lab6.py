import customtkinter as ctk
from src.components.sidebarComponent import sidebarComponent
from src.frames.lab6.tasks.task1 import Task1Frame
from src.frames.lab6.tasks.task2 import Task2Frame
from src.frames.lab6.tasks.task3 import Task3Frame
from src.frames.lab6.tasks.task4 import Task4Frame
from src.frames.lab6.tasks.task5 import Task5Frame


class Lab6Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)

        self.tasks = [1, 2, 3, 4, 5]

        self.sidebar = sidebarComponent(self, self.tasks, self.on_task_click)

        self.content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.task_frames = {
            1: Task1Frame(self.content_frame),
            2: Task2Frame(self.content_frame),
            3: Task3Frame(self.content_frame),
            4: Task4Frame(self.content_frame),
            5: Task5Frame(self.content_frame),
        }

        for frame in self.task_frames.values():
            frame.pack_forget()

        self.on_task_click(self.tasks[0])

    def on_task_click(self, task_number):

        for frame in self.task_frames.values():
            frame.pack_forget()

        selected_task_frame = self.task_frames.get(task_number)
        if selected_task_frame:
            selected_task_frame.pack(fill="both", expand=True)
        else:
            error_label = ctk.CTkLabel(self.content_frame, text="Задание не найдено!")
            error_label.pack(fill="both", expand=True)
