from math import pow

pow_list = []

for a in range(2, 101):
    for b in range(2, 101):
        temp = pow (a, b)
        if temp not in pow_list:
            pow_list.append(temp)
            
for b in range(2, 101):
    for a in range(2, 101):
        temp = pow (b, a)
        if temp not in pow_list:
            pow_list.append(temp)

print len(pow_list)            
