import tkinter as tk
fullstring = """Diamond Ring
+50 to Strength 
+28% to Fire Resistance
+8% to Cold Resistance
some extra text"""

window = tk.Tk()
window.geometry("600x400")

item_var = tk.StringVar()


def check_item():
    print(userstring)
    splitstring = fullstring.splitlines()
    lines = len(splitstring)
    for i in range(lines):
        if splitstring[i].find("% to Fire Resistance") != -1:
            x = splitstring[i].split("%")
            r1 = x[0].replace("+", "")
            print(r1, "fire")
        if splitstring[i].find("% to Cold Resistance") != -1:
            x = splitstring[i].split("%")
            r2 = x[0].replace("+", "")
            print(r2, "cold")
        if splitstring[i].find("% to Lightning Resistance") != -1:
            x = splitstring[i].split("%")
            r3 = x[0].replace("+", "")
            print(r3, "lightning")
        if splitstring[i].find("% to Chaos Resistance") != -1:
            x = splitstring[i].split("%")
            r4 = x[0].replace("+", "")
            print(r4, "chaos")


def submit():
    item = item_var.get()
    print(item)
    splitstring = item.splitlines()
    lines = len(splitstring)
    for i in range(lines):
        if splitstring[i].find("% to Fire Resistance") != -1:
            x = splitstring[i].split("%")
            r1 = x[0].replace("+", "")
            print(r1, "fire")
        if splitstring[i].find("% to Cold Resistance") != -1:
            x = splitstring[i].split("%")
            r2 = x[0].replace("+", "")
            print(r2, "cold")
        if splitstring[i].find("% to Lightning Resistance") != -1:
            x = splitstring[i].split("%")
            r3 = x[0].replace("+", "")
            print(r3, "lightning")
        if splitstring[i].find("% to Chaos Resistance") != -1:
            x = splitstring[i].split("%")
            r4 = x[0].replace("+", "")
            print(r4, "chaos")


userstring = tk.Entry(window, textvariable=item_var)
userstring.pack()
button = tk.Button(window, text="enter", command=submit)
button.pack()

window.mainloop()
