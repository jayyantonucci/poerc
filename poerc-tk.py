##tkinter concept
##need to organize
##impliment save/load





from tkinter import *



def calculate_res():
    total_fire_res = int(weapon_fire_entry.get()) + int(offhand_fire_entry.get())
    total_fire_res_text.set(total_fire_res)
    

gs = ["weapon", "offhand", "helm", "chest", "gloves", "boots", "belt", "ring1", "ring2", "amulet"]
res = ["fire", "cold", "lightning", "chaos"]
master = Tk()
master.title("poe reference chart")
frame = Frame(master)
total_fire_res_text = StringVar()

Label(master, text='res/slot').grid(row=0, column=0)
#slot labels
cnum=1
for i in gs:
    cnum += 1
    Label(master, text=i, width=10).grid(row=0, column=cnum)
    Label(master, text=i, width=10).grid(row=6, column=cnum)
#res labels
rnum=1
for i in res:
    rnum += 1
    Label(master, text=i).grid(row=rnum, column=0)
    Label(master, text=i).grid(row=rnum+6, column=0)
#entry
weapon_fire_entry = Entry(master, width=5)
weapon_fire_entry.grid(row=2, column=2)
weapon_cold_entry = Entry(master, width=5).grid(row=3, column=2)
weapon_lightning_entry = Entry(master, width=5).grid(row=4, column=2)
weapon_chaos_entry = Entry(master, width=5).grid(row=5, column=2)

offhand_fire_entry = Entry(master, width=5)
offhand_fire_entry.grid(row=2, column=3)
offhand_cold_entry = Entry(master, width=5).grid(row=3, column=3)
offhand_lightning_entry = Entry(master, width=5).grid(row=4, column=3)
offhand_chaos_entry = Entry(master, width=5).grid(row=5, column=3)



total_fire_res_label = Label(master, text="", textvariable=total_fire_res_text).grid(row=13, column=2)


    

calculate_button = Button(master, text="calculate", command=calculate_res).grid(row=12, column=0)

rnum=12
for i in res:
    rnum += 1
    label = Label(master, text=i).grid(row=rnum, column=0)


master.mainloop()