from new_item import new_item
import tkinter as tk

window = tk.Tk()
window.geometry("400x300")

button = tk.Button(window, text="New item", command=new_item)
button.pack()

window.mainloop()
