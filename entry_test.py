import tkinter as tk

window = tk.Tk()
window.geometry("600x400")
item_var = tk.StringVar()


def submit():
    r1 = r2 = r3 = r4 = 0
    a = item_var.get()
    splitstring = a.splitlines()
    lines = len(splitstring)
    n = splitstring[0]
    for i in range(lines):
        if splitstring[i].find("% to Fire Resistance") != -1:
            x = splitstring[i].split("%")
            r1 = x[0].replace("+", "")
        if splitstring[i].find("% to Cold Resistance") != -1:
            x = splitstring[i].split("%")
            r2 = x[0].replace("+", "")
        if splitstring[i].find("% to Lightning Resistance") != -1:
            x = splitstring[i].split("%")
            r3 = x[0].replace("+", "")
        if splitstring[i].find("% to Chaos Resistance") != -1:
            x = splitstring[i].split("%")
            r4 = x[0].replace("+", "")
    b = [n, r1, r2, r3, r4, a]
    entry.delete(0, 'end')


entry = tk.Entry(window, textvariable=item_var)
entry.pack()
button = tk.Button(window, text="enter", command=submit)
button.pack()

window.mainloop()
