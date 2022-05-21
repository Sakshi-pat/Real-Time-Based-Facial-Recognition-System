import tkinter as tk
from tkinter import ttk
import os

root = tk.Tk()
root.title('Face Recognition')

root.geometry("500x200")

tk.Label(root, text="Face Recognition Project", font=("Helvetica", 14)).pack()

# frame = ttk.Frame(root)


def addFace():
    os.system('python addPerson.py')


def recFace():
    os.system('python final.py')


button1 = ttk.Button(root, text="Add Face", command=addFace)
button1.pack(ipadx=10, ipady=5, expand=True)

button2 = ttk.Button(root, text="Recognize Face", command=recFace)
button2.pack(ipadx=10, ipady=5, expand=True)
root.mainloop()
