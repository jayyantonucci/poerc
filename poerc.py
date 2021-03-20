

#gear piece [Fire, Cold, Lightning, Chaos]

gloves = [20, 15, 0, 10]
boots = [0, 15, 0, 5]
helm = [5, 15, 0, 15]

fire = 0
cold = 0
lightning = 0
chaos = 0

items = [gloves, boots, helm]


for i in items:
    fire = fire + i[0]
    cold = cold + i[1]
    lightning = lightning + i[2]
    chaos = chaos + i[3]

res = [fire, cold, lightning, chaos]


