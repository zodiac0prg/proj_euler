from math import sqrt

fact_sum = 0;
num = 1
abud_list = []

while True:
    fact_sum = 0
    limit = sqrt(num)
    i = 1
    while True:
        if num % i == 0:
            fact_sum += i
            if (num/i != i):
                fact_sum += (num/i)

        i += 1
        if (i > limit):
            break
    if (fact_sum - num > num):
        abud_list.append(num)
        
    #print num, fact_sum - num    
    num += 1
    if (num == 28123):
        break
            
#print len(abud_list)
new_abud_list = []

for i in abud_list:
    for j in abud_list:
        new_abud_list.append( i + j)

num = 1
tot_sum = 0
while True:
    print num
    if num not in new_abud_list:
        tot_sum += num
    num += 1
    if num == 28123:
        break

print "Total sum"
print tot_sum

