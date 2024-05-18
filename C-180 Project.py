from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Language Translator")
root.geometry("500x500")
root.config(bg = "#DC143C")

lbl_title = Label(root, text = "Language Translator", bg = "#DC143C")
lbl_title.place(relx = 0.5, rely = 0.1, anchor = CENTER)

lbl_enter_text = Label(root, text = "Enter Text", bg = "#DC143C")
lbl_enter_text.place(relx = 0.1, rely = 0.3, anchor = W)

entry_enter_text = Text(root, bg = "white", height = 7, wrap = WORD, width = 55, padx = 3, pady = 3, bd = 0)
entry_enter_text.place(relx = 0.1, rely = 0.5, anchor = W)

root.mainloop() 