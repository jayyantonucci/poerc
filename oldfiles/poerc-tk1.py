#building out from the concept in poerc-tk.py
#next stage is saving values to a file

from tkinter import *

def insert_values():
    #weapon
    wep_fire_res_val = int(wep_fire_res_entry.get())
    wep_fire_res_txt.set(wep_fire_res_val)
    wep_cold_res_val = int(wep_cold_res_entry.get())
    wep_cold_res_txt.set(wep_cold_res_val)
    wep_lightning_res_val = int(wep_lightning_res_entry.get())
    wep_lightning_res_txt.set(wep_lightning_res_val)
    wep_chaos_res_val = int(wep_chaos_res_entry.get())
    wep_chaos_res_txt.set(wep_chaos_res_val)
    #offhand
    oh_fire_res_val = int(oh_fire_res_entry.get())
    oh_fire_res_txt.set(oh_fire_res_val)
    oh_cold_res_val = int(oh_cold_res_entry.get())
    oh_cold_res_txt.set(oh_cold_res_val)
    oh_lightning_res_val = int(oh_lightning_res_entry.get())
    oh_lightning_res_txt.set(oh_lightning_res_val)
    oh_chaos_res_val = int(oh_chaos_res_entry.get())
    oh_chaos_res_txt.set(oh_chaos_res_val)
    #helm
    helm_fire_res_val = int(helm_fire_res_entry.get())
    helm_fire_res_txt.set(helm_fire_res_val)
    helm_cold_res_val = int(helm_cold_res_entry.get())
    helm_cold_res_txt.set(helm_cold_res_val)
    helm_lightning_res_val = int(helm_lightning_res_entry.get())
    helm_lightning_res_txt.set(helm_lightning_res_val)
    helm_chaos_res_val = int(helm_chaos_res_entry.get())
    helm_chaos_res_txt.set(helm_chaos_res_val)
    #chest
    chest_fire_res_val = int(chest_fire_res_entry.get())
    chest_fire_res_txt.set(chest_fire_res_val)
    chest_cold_res_val = int(chest_cold_res_entry.get())
    chest_cold_res_txt.set(chest_cold_res_val)
    chest_lightning_res_val = int(chest_lightning_res_entry.get())
    chest_lightning_res_txt.set(chest_lightning_res_val)
    chest_chaos_res_val = int(chest_chaos_res_entry.get())
    chest_chaos_res_txt.set(chest_chaos_res_val)
    #gloves
    gloves_fire_res_val = int(gloves_fire_res_entry.get())
    gloves_fire_res_txt.set(gloves_fire_res_val)
    gloves_cold_res_val = int(gloves_cold_res_entry.get())
    gloves_cold_res_txt.set(gloves_cold_res_val)
    gloves_lightning_res_val = int(gloves_lightning_res_entry.get())
    gloves_lightning_res_txt.set(gloves_lightning_res_val)
    gloves_chaos_res_val = int(gloves_chaos_res_entry.get())
    gloves_chaos_res_txt.set(gloves_chaos_res_val)
    #boots
    boots_fire_res_val = int(boots_fire_res_entry.get())
    boots_fire_res_txt.set(boots_fire_res_val)
    boots_cold_res_val = int(boots_cold_res_entry.get())
    boots_cold_res_txt.set(boots_cold_res_val)
    boots_lightning_res_val = int(boots_lightning_res_entry.get())
    boots_lightning_res_txt.set(boots_lightning_res_val)
    boots_chaos_res_val = int(boots_chaos_res_entry.get())
    boots_chaos_res_txt.set(boots_chaos_res_val)
    #belt
    belt_fire_res_val = int(belt_fire_res_entry.get())
    belt_fire_res_txt.set(belt_fire_res_val)
    belt_cold_res_val = int(belt_cold_res_entry.get())
    belt_cold_res_txt.set(belt_cold_res_val)
    belt_lightning_res_val = int(belt_lightning_res_entry.get())
    belt_lightning_res_txt.set(belt_lightning_res_val)
    belt_chaos_res_val = int(belt_chaos_res_entry.get())
    belt_chaos_res_txt.set(belt_chaos_res_val)
    #ring1
    ring1_fire_res_val = int(ring1_fire_res_entry.get())
    ring1_fire_res_txt.set(ring1_fire_res_val)
    ring1_cold_res_val = int(ring1_cold_res_entry.get())
    ring1_cold_res_txt.set(ring1_cold_res_val)
    ring1_lightning_res_val = int(ring1_lightning_res_entry.get())
    ring1_lightning_res_txt.set(ring1_lightning_res_val)
    ring1_chaos_res_val = int(ring1_chaos_res_entry.get())
    ring1_chaos_res_txt.set(ring1_chaos_res_val)
    #ring2
    ring2_fire_res_val = int(ring2_fire_res_entry.get())
    ring2_fire_res_txt.set(ring2_fire_res_val)
    ring2_cold_res_val = int(ring2_cold_res_entry.get())
    ring2_cold_res_txt.set(ring2_cold_res_val)
    ring2_lightning_res_val = int(ring2_lightning_res_entry.get())
    ring2_lightning_res_txt.set(ring2_lightning_res_val)
    ring2_chaos_res_val = int(ring2_chaos_res_entry.get())
    ring2_chaos_res_txt.set(ring2_chaos_res_val)
    #amulet
    amulet_fire_res_val = int(amulet_fire_res_entry.get())
    amulet_fire_res_txt.set(amulet_fire_res_val)
    amulet_cold_res_val = int(amulet_cold_res_entry.get())
    amulet_cold_res_txt.set(amulet_cold_res_val)
    amulet_lightning_res_val = int(amulet_lightning_res_entry.get())
    amulet_lightning_res_txt.set(amulet_lightning_res_val)
    amulet_chaos_res_val = int(amulet_chaos_res_entry.get())
    amulet_chaos_res_txt.set(amulet_chaos_res_val)
    #total
    tot_fire_res_val = int(wep_fire_res_entry.get()) + int(oh_fire_res_entry.get()) + int(helm_fire_res_entry.get()) + int(chest_fire_res_entry.get()) + int(gloves_fire_res_entry.get()) + int(boots_fire_res_entry.get()) + int(belt_fire_res_entry.get()) + int(ring1_fire_res_entry.get()) + int(ring2_fire_res_entry.get()) + int(amulet_fire_res_entry.get())
    tot_fire_res_txt.set(tot_fire_res_val)
    tot_cold_res_val = int(wep_cold_res_entry.get()) + int(oh_cold_res_entry.get()) + int(helm_cold_res_entry.get()) + int(chest_cold_res_entry.get()) + int(gloves_cold_res_entry.get()) + int(boots_cold_res_entry.get()) + int(belt_cold_res_entry.get()) + int(ring1_cold_res_entry.get()) + int(ring2_cold_res_entry.get()) + int(amulet_cold_res_entry.get())
    tot_cold_res_txt.set(tot_cold_res_val)
    tot_lightning_res_val = int(wep_lightning_res_entry.get()) + int(oh_lightning_res_entry.get()) + int(helm_lightning_res_entry.get()) + int(chest_lightning_res_entry.get()) + int(gloves_lightning_res_entry.get()) + int(boots_lightning_res_entry.get()) + int(belt_lightning_res_entry.get()) + int(ring1_lightning_res_entry.get()) + int(ring2_lightning_res_entry.get()) + int(amulet_lightning_res_entry.get())
    tot_lightning_res_txt.set(tot_lightning_res_val)
    tot_chaos_res_val = int(wep_chaos_res_entry.get()) + int(oh_chaos_res_entry.get()) + int(helm_chaos_res_entry.get()) + int(chest_chaos_res_entry.get()) + int(gloves_chaos_res_entry.get()) + int(boots_chaos_res_entry.get()) + int(belt_chaos_res_entry.get()) + int(ring1_chaos_res_entry.get()) + int(ring2_chaos_res_entry.get()) + int(amulet_chaos_res_entry.get())
    tot_chaos_res_txt.set(tot_chaos_res_val)


root = Tk()


### window labels
gear_slot = ["weapon", "offhand", "helm", "chest", "gloves", "boots", "belt", "ring1", "ring2", "amulet"]
res = ["fire", "cold", "lightning", "chaos"]
#gear slot labels
cnum=0
for i in gear_slot:
    cnum += 1
    Label(root, text=i, width=10).grid(row=0, column=cnum)
    Label(root, text=i, width=10).grid(row=6, column=cnum)
#resistance type labels
rnum=1
for i in res:
    rnum += 1
    Label(root, text=i).grid(row=rnum, column=0)
    Label(root, text=i).grid(row=rnum+6, column=0)
    Label(root, text=i).grid(row=rnum+11, column=0)

### weapon
#fire
wep_fire_res_txt = StringVar()
wep_fire_res_entry = Entry(root, width=5)
wep_fire_res_entry.grid(row=2, column=1)
wep_fire_res_lbl = Label(root, text="", textvariable=wep_fire_res_txt).grid(row=8, column=1)
#cold
wep_cold_res_txt = StringVar()
wep_cold_res_entry = Entry(root, width=5)
wep_cold_res_entry.grid(row=3, column=1)
wep_cold_res_lbl = Label(root, text="", textvariable=wep_cold_res_txt).grid(row=9, column=1)
#lightning
wep_lightning_res_txt = StringVar()
wep_lightning_res_entry = Entry(root, width=5)
wep_lightning_res_entry.grid(row=4, column=1)
wep_lightning_res_lbl = Label(root, text="", textvariable=wep_lightning_res_txt).grid(row=10, column=1)
#chaos
wep_chaos_res_txt = StringVar()
wep_chaos_res_entry = Entry(root, width=5)
wep_chaos_res_entry.grid(row=5, column=1)
wep_chaos_res_lbl = Label(root, text="", textvariable=wep_chaos_res_txt).grid(row=11, column=1)
### offhand
#fire
oh_fire_res_txt = StringVar()
oh_fire_res_entry = Entry(root, width=5)
oh_fire_res_entry.grid(row=2, column=2)
oh_fire_res_lbl = Label(root, text="", textvariable=oh_fire_res_txt).grid(row=8, column=2)
#cold
oh_cold_res_txt = StringVar()
oh_cold_res_entry = Entry(root, width=5)
oh_cold_res_entry.grid(row=3, column=2)
oh_cold_res_lbl = Label(root, text="", textvariable=oh_cold_res_txt).grid(row=9, column=2)
#lightning
oh_lightning_res_txt = StringVar()
oh_lightning_res_entry = Entry(root, width=5)
oh_lightning_res_entry.grid(row=4, column=2)
oh_lightning_res_lbl = Label(root, text="", textvariable=oh_lightning_res_txt).grid(row=10, column=2)
#chaos
oh_chaos_res_txt = StringVar()
oh_chaos_res_entry = Entry(root, width=5)
oh_chaos_res_entry.grid(row=5, column=2)
oh_chaos_res_lbl = Label(root, text="", textvariable=oh_chaos_res_txt).grid(row=11, column=2)
### helm
#fire
helm_fire_res_txt = StringVar()
helm_fire_res_entry = Entry(root, width=5)
helm_fire_res_entry.grid(row=2, column=3)
helm_fire_res_lbl = Label(root, text="", textvariable=helm_fire_res_txt).grid(row=8, column=3)
#cold
helm_cold_res_txt = StringVar()
helm_cold_res_entry = Entry(root, width=5)
helm_cold_res_entry.grid(row=3, column=3)
helm_cold_res_lbl = Label(root, text="", textvariable=helm_cold_res_txt).grid(row=9, column=3)
#lightning
helm_lightning_res_txt = StringVar()
helm_lightning_res_entry = Entry(root, width=5)
helm_lightning_res_entry.grid(row=4, column=3)
helm_lightning_res_lbl = Label(root, text="", textvariable=helm_lightning_res_txt).grid(row=10, column=3)
#chaos
helm_chaos_res_txt = StringVar()
helm_chaos_res_entry = Entry(root, width=5)
helm_chaos_res_entry.grid(row=5, column=3)
helm_chaos_res_lbl = Label(root, text="", textvariable=helm_chaos_res_txt).grid(row=11, column=3)
### chest
#fire
chest_fire_res_txt = StringVar()
chest_fire_res_entry = Entry(root, width=5)
chest_fire_res_entry.grid(row=2, column=4)
chest_fire_res_lbl = Label(root, text="", textvariable=chest_fire_res_txt).grid(row=8, column=4)
#cold
chest_cold_res_txt = StringVar()
chest_cold_res_entry = Entry(root, width=5)
chest_cold_res_entry.grid(row=3, column=4)
chest_cold_res_lbl = Label(root, text="", textvariable=chest_cold_res_txt).grid(row=9, column=4)
#lightning
chest_lightning_res_txt = StringVar()
chest_lightning_res_entry = Entry(root, width=5)
chest_lightning_res_entry.grid(row=4, column=4)
chest_lightning_res_lbl = Label(root, text="", textvariable=chest_lightning_res_txt).grid(row=10, column=4)
#chaos
chest_chaos_res_txt = StringVar()
chest_chaos_res_entry = Entry(root, width=5)
chest_chaos_res_entry.grid(row=5, column=4)
chest_chaos_res_lbl = Label(root, text="", textvariable=chest_chaos_res_txt).grid(row=11, column=4)
### gloves
#fire
gloves_fire_res_txt = StringVar()
gloves_fire_res_entry = Entry(root, width=5)
gloves_fire_res_entry.grid(row=2, column=5)
gloves_fire_res_lbl = Label(root, text="", textvariable=gloves_fire_res_txt).grid(row=8, column=5)
#cold
gloves_cold_res_txt = StringVar()
gloves_cold_res_entry = Entry(root, width=5)
gloves_cold_res_entry.grid(row=3, column=5)
gloves_cold_res_lbl = Label(root, text="", textvariable=gloves_cold_res_txt).grid(row=9, column=5)
#lightning
gloves_lightning_res_txt = StringVar()
gloves_lightning_res_entry = Entry(root, width=5)
gloves_lightning_res_entry.grid(row=4, column=5)
gloves_lightning_res_lbl = Label(root, text="", textvariable=gloves_lightning_res_txt).grid(row=10, column=5)
#chaos
gloves_chaos_res_txt = StringVar()
gloves_chaos_res_entry = Entry(root, width=5)
gloves_chaos_res_entry.grid(row=5, column=5)
gloves_chaos_res_lbl = Label(root, text="", textvariable=gloves_chaos_res_txt).grid(row=11, column=5)
### boots
#fire
boots_fire_res_txt = StringVar()
boots_fire_res_entry = Entry(root, width=5)
boots_fire_res_entry.grid(row=2, column=6)
boots_fire_res_lbl = Label(root, text="", textvariable=boots_fire_res_txt).grid(row=8, column=6)
#cold
boots_cold_res_txt = StringVar()
boots_cold_res_entry = Entry(root, width=5)
boots_cold_res_entry.grid(row=3, column=6)
boots_cold_res_lbl = Label(root, text="", textvariable=boots_cold_res_txt).grid(row=9, column=6)
#lightning
boots_lightning_res_txt = StringVar()
boots_lightning_res_entry = Entry(root, width=5)
boots_lightning_res_entry.grid(row=4, column=6)
boots_lightning_res_lbl = Label(root, text="", textvariable=boots_lightning_res_txt).grid(row=10, column=6)
#chaos
boots_chaos_res_txt = StringVar()
boots_chaos_res_entry = Entry(root, width=5)
boots_chaos_res_entry.grid(row=5, column=6)
boots_chaos_res_lbl = Label(root, text="", textvariable=boots_chaos_res_txt).grid(row=11, column=6)
### belt
#fire
belt_fire_res_txt = StringVar()
belt_fire_res_entry = Entry(root, width=5)
belt_fire_res_entry.grid(row=2, column=7)
belt_fire_res_lbl = Label(root, text="", textvariable=belt_fire_res_txt).grid(row=8, column=7)
#cold
belt_cold_res_txt = StringVar()
belt_cold_res_entry = Entry(root, width=5)
belt_cold_res_entry.grid(row=3, column=7)
belt_cold_res_lbl = Label(root, text="", textvariable=belt_cold_res_txt).grid(row=9, column=7)
#lightning
belt_lightning_res_txt = StringVar()
belt_lightning_res_entry = Entry(root, width=5)
belt_lightning_res_entry.grid(row=4, column=7)
belt_lightning_res_lbl = Label(root, text="", textvariable=belt_lightning_res_txt).grid(row=10, column=7)
#chaos
belt_chaos_res_txt = StringVar()
belt_chaos_res_entry = Entry(root, width=5)
belt_chaos_res_entry.grid(row=5, column=7)
belt_chaos_res_lbl = Label(root, text="", textvariable=belt_chaos_res_txt).grid(row=11, column=7)
### ring1
#fire
ring1_fire_res_txt = StringVar()
ring1_fire_res_entry = Entry(root, width=5)
ring1_fire_res_entry.grid(row=2, column=8)
ring1_fire_res_lbl = Label(root, text="", textvariable=ring1_fire_res_txt).grid(row=8, column=8)
#cold
ring1_cold_res_txt = StringVar()
ring1_cold_res_entry = Entry(root, width=5)
ring1_cold_res_entry.grid(row=3, column=8)
ring1_cold_res_lbl = Label(root, text="", textvariable=ring1_cold_res_txt).grid(row=9, column=8)
#lightning
ring1_lightning_res_txt = StringVar()
ring1_lightning_res_entry = Entry(root, width=5)
ring1_lightning_res_entry.grid(row=4, column=8)
ring1_lightning_res_lbl = Label(root, text="", textvariable=ring1_lightning_res_txt).grid(row=10, column=8)
#chaos
ring1_chaos_res_txt = StringVar()
ring1_chaos_res_entry = Entry(root, width=5)
ring1_chaos_res_entry.grid(row=5, column=8)
ring1_chaos_res_lbl = Label(root, text="", textvariable=ring1_chaos_res_txt).grid(row=11, column=8)
### ring2
#fire
ring2_fire_res_txt = StringVar()
ring2_fire_res_entry = Entry(root, width=5)
ring2_fire_res_entry.grid(row=2, column=9)
ring2_fire_res_lbl = Label(root, text="", textvariable=ring2_fire_res_txt).grid(row=8, column=9)
#cold
ring2_cold_res_txt = StringVar()
ring2_cold_res_entry = Entry(root, width=5)
ring2_cold_res_entry.grid(row=3, column=9)
ring2_cold_res_lbl = Label(root, text="", textvariable=ring2_cold_res_txt).grid(row=9, column=9)
#lightning
ring2_lightning_res_txt = StringVar()
ring2_lightning_res_entry = Entry(root, width=5)
ring2_lightning_res_entry.grid(row=4, column=9)
ring2_lightning_res_lbl = Label(root, text="", textvariable=ring2_lightning_res_txt).grid(row=10, column=9)
#chaos
ring2_chaos_res_txt = StringVar()
ring2_chaos_res_entry = Entry(root, width=5)
ring2_chaos_res_entry.grid(row=5, column=9)
ring2_chaos_res_lbl = Label(root, text="", textvariable=ring2_chaos_res_txt).grid(row=11, column=9)
### amulet
#fire
amulet_fire_res_txt = StringVar()
amulet_fire_res_entry = Entry(root, width=5)
amulet_fire_res_entry.grid(row=2, column=10)
amulet_fire_res_lbl = Label(root, text="", textvariable=amulet_fire_res_txt).grid(row=8, column=10)
#cold
amulet_cold_res_txt = StringVar()
amulet_cold_res_entry = Entry(root, width=5)
amulet_cold_res_entry.grid(row=3, column=10)
amulet_cold_res_lbl = Label(root, text="", textvariable=amulet_cold_res_txt).grid(row=9, column=10)
#lightning
amulet_lightning_res_txt = StringVar()
amulet_lightning_res_entry = Entry(root, width=5)
amulet_lightning_res_entry.grid(row=4, column=10)
amulet_lightning_res_lbl = Label(root, text="", textvariable=amulet_lightning_res_txt).grid(row=10, column=10)
#chaos
amulet_chaos_res_txt = StringVar()
amulet_chaos_res_entry = Entry(root, width=5)
amulet_chaos_res_entry.grid(row=5, column=10)
amulet_chaos_res_lbl = Label(root, text="", textvariable=amulet_chaos_res_txt).grid(row=11, column=10)
### totals
Label(root, text="Total:").grid(row=12, column=1)
tot_fire_res_txt = StringVar()
tot_fire_res_lbl = Label(root, text="", textvariable=tot_fire_res_txt).grid(row=13, column=1)
tot_cold_res_txt = StringVar()
tot_cold_res_lbl = Label(root, text="", textvariable=tot_cold_res_txt).grid(row=14, column=1)
tot_lightning_res_txt = StringVar()
tot_lightning_res_lbl = Label(root, text="", textvariable=tot_lightning_res_txt).grid(row=15, column=1)
tot_chaos_res_txt = StringVar()
tot_chaos_res_lbl = Label(root, text="", textvariable=tot_chaos_res_txt).grid(row=16, column=1)




calcbtn = Button(root, text="calculate", command=insert_values).grid(row=17, column=0)


root.mainloop()