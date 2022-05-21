import tkinter as tk
from tkinter import ttk
import json


class ViewDetails():
    def __init__(self, name):
        self.name = name
        self.age = ""
        self.sex = ""
        self.root = tk.Tk()
        self.root.title("Details")
        self.root.geometry("400x300")

        tk.Label(self.root, text="Details of Captured face", font=("Helvetica", 14)).pack()

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        self.fetchDetails()

        LName = tk.Label(frame, text="Name : ")
        LName.grid(column=0, row=0, pady=30)

        Name = tk.Label(frame, text=self.name)
        Name.grid(column=1, row=0, pady=30)

        LAge = tk.Label(frame, text="Age : ")
        LAge.grid(column=0, row=1)

        Age = tk.Label(frame, text=self.age)
        Age.grid(column=1, row=1)

        LSex = tk.Label(frame, text="Sex : ")
        LSex.grid(column=0, row=2, pady=30)

        Sex = tk.Label(frame, text=self.sex)
        Sex.grid(column=1, row=2, pady=30)

        self.root.mainloop()

    def fetchDetails(self):
        with open("Records.json", 'r+') as file:
            data = json.load(file)

            for i in data["Face_records"]:
                if i["Name"] == self.name:
                    self.age = i["Age"]
                    self.sex = i["Sex"]
