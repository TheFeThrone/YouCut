import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

def prompt(topic, question, empty):
    ROOT = tk.Tk()

    ROOT.withdraw()
    # the input dialog
    userinp = rf"{simpledialog.askstring(title=topic, prompt=question)}"
    ROOT.destroy()  # destroy the Tk object after the prompt is closed
    if userinp =="None": return None
    elif userinp =="": 
        return None if empty == False else userinp
    else: return userinp

def info(title, message):
    ROOT = tk.Tk()

    ROOT.withdraw()

    #the dialog
    messagebox.showinfo(title, message)

def alert(title, message, mode):
    ROOT = tk.Tk()

    ROOT.withdraw()

    #the dialog
    if (mode=="error"):
        messagebox.showerror(title, message)
        quit()
    if (mode=="warning"):
        messagebox.showwarning(title, message)