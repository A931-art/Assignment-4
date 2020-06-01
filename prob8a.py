import random

interval=1000

cir_pt=0
sq_pt=0

for i in range(interval**2):
    rand_x=random.uniform(-1,1)
    rand_y=random.uniform(-1,1)

    dist=rand_x**2+rand_y**2

    if dist<=1:
        cir_pt+=1

    sq_pt+=1

    area=4*cir_pt/sq_pt

print("area of the unit circle = ",area)
