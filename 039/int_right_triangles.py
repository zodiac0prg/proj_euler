
perim_dict = {}

for x in range(1,1000):
    y = x+1
    z = y+1
    
    while z <= 1000:
        while z*z < (x*x + y*y):
            z += 1
        
        if z*z == (x*x + y*y) and z <= 1000 :
            if (x + y + z) not in perim_dict:
                perim_dict[x + y + z] = 1
            else:
                perim_dict[x + y + z] += 1
            
        y += 1

max_perim = 12
max_perim_sol = 1

for i in (perim_dict):
    if (i <= 1000):
        if (perim_dict[i] > max_perim_sol):
            max_perim_sol = perim_dict[i]
            max_perim = i

print max_perim
print max_perim_sol
    
