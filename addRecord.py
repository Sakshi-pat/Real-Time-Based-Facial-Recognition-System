import tkinter as tk
from tkinter import ttk
import json


class AddRecords():
    def __init__(self):
        self.name = ""
        self.age = ""
        self.sex = ""
        self.recName = ""
        self.recAge = ""
        self.recSex = ""
        self.root = tk.Tk()

    def takeInput(self):

        self.root.title("Add Records")
        self.root.geometry("400x300")

        tk.Label(self.root, text="Add Details for Captured face", font=("Helvetica", 14)).pack()

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        Name = tk.Label(frame, text="Name : ")
        Name.grid(column=0, row=0, pady=30)
        self.name = tk.Entry(frame, bd=5)
        self.name.grid(column=1, row=0)

        Age = tk.Label(frame, text="Age : ")
        Age.grid(column=0, row=1)
        self.age = tk.Entry(frame, bd=5)
        self.age.grid(column=1, row=1)

        Sex = tk.Label(frame, text="Sex : ")
        Sex.grid(column=0, row=2, pady=30)
        self.sex = tk.Entry(frame, bd=5)
        self.sex.grid(column=1, row=2)

        newframe = tk.Frame(self.root)
        newframe.pack()

        submitbutton = ttk.Button(newframe, text="Submit", command=self.submitRec)
        submitbutton.pack(ipadx=10, ipady=5, expand=True)

        self.root.mainloop()

    def submitRec(self):
        self.recName = self.name.get()
        self.recAge = self.age.get()
        self.recSex = self.sex.get()
        self.root.destroy()

    def fillInfo(self):
        new_data = {
            "Name": self.recName,
            "Age": self.recAge,
            "Sex": self.recSex
        }
        with open("Records.json", 'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["Face_records"].append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent=4)

        return self.recName


# Ar = AddRecords()
# Ar.takeInput()
# Ar.fillInfo()

