import tkinter as tk

window = tk.Tk()

for line in open("test.txt"):
    var = tk.StringVar()
    nline = line.strip("[").rstrip("\n]")
    var.set(nline)
    text = tk.Entry(window, state="readonly", width=40)
    text.config(textvariable=var)
    text.pack()


window.mainloop()
