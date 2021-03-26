import tkinter as tk


def list_items():
    window = tk.Tk()

    for line in open("test.txt"):
        var = tk.StringVar()
        nline = line.strip("[").rstrip("\n]")
        var.set(nline)
        text = tk.Entry(window, state="readonly", width=40)
        text.config(textvariable=var)
        text.pack()

    window.mainloop()


def new_item():
    window = tk.Tk()
    window.geometry("300x200")
    item_var = tk.StringVar()

    def submit():
        r1 = r2 = r3 = r4 = r5 = r6 = r7 = r8 = r9 = r10 = r11 = 0
        a = item_var.get()
        splitstring = a.splitlines()
        lines = len(splitstring)
        b = []
        n = splitstring[0]
        for i in range(lines):
            if splitstring[i].find("% to Fire Resistance") != -1:
                x = splitstring[i].split("%")
                r1 = x[0].replace("+", "")
            if splitstring[i].find("% to Fire and Cold Resistance") != -1:
                x = splitstring[i].split("%")
                r5 = x[0].replace("+", "")
            if splitstring[i].find("% to Fire and Lightning Resistance") != -1:
                x = splitstring[i].split("%")
                r6 = x[0].replace("+", "")
            if splitstring[i].find("% to Fire and Chaos Resistance") != -1:
                x = splitstring[i].split("%")
                r7 = x[0].replace("+", "")
            if splitstring[i].find("% to Cold Resistance") != -1:
                x = splitstring[i].split("%")
                r2 = x[0].replace("+", "")
            if splitstring[i].find("% to Cold and Lightning Resistance") != -1:
                x = splitstring[i].split("%")
                r8 = x[0].replace("+", "")
            if splitstring[i].find("% to Cold and Chaos Resistance") != -1:
                x = splitstring[i].split("%")
                r9 = x[0].replace("+", "")
            if splitstring[i].find("% to Lightning Resistance") != -1:
                x = splitstring[i].split("%")
                r3 = x[0].replace("+", "")
            if splitstring[i].find("% to Lightning and Chaos Resistance") != -1:
                x = splitstring[i].split("%")
                r10 = x[0].replace("+", "")
            if splitstring[i].find("% to Chaos Resistance") != -1:
                x = splitstring[i].split("%")
                r4 = x[0].replace("+", "")
            if splitstring[i].find("% to all Elemental Resistances") != -1:
                x = splitstring[i].split("%")
                r11 = x[0].replace("+", "")

        rf = int(r1) + int(r5) + int(r6) + int(r7) + int(r11)
        rc = int(r2) + int(r5) + int(r8) + int(r9) + int(r11)
        rl = int(r3) + int(r6) + int(r8) + int(r10) + int(r11)
        rx = int(r4) + int(r7) + int(r9) + int(r10)
        b = [n, rf, rc, rl, rx]
        print(b)
        entry.delete(0, 'end')
        label = tk.Label(window, text=f"{b} added")
        label.pack()
        f = open("test.txt", "a+")
        f.write(f"{b}\n")

    entry = tk.Entry(window, textvariable=item_var)
    entry.pack()
    button = tk.Button(window, text="enter", command=submit)
    button.pack()

    window.mainloop()


window = tk.Tk()
window.geometry("400x300")

button = tk.Button(window, text="New item", command=new_item)
button.pack()
button = tk.Button(window, text="list items", command=list_items)
button.pack()

window.mainloop()
