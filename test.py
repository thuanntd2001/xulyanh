import math
r = 4
mask = []
for dy in range(-r, r+1):
    dx = int(math.sqrt(r*r-dy*dy))
    for x in range(-dx,dx+1):
        mask += [(x,dy)]
print(mask)