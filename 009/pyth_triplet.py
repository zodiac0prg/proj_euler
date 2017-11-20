

found = 0
for x in range(1,1000):
    y = x+1
    z= y+1
    
    while z <= 1000:
        while z*z < (x*x + y*y):
            z += 1
        
        if z*z == (x*x + y*y) and z <= 1000 :
            if (x + y + z == 1000):
                print x, y, z
                print x * y * z
                found = 1
                break
        y += 1

        if found == 1 :
            break
    if found == 1:
        break
