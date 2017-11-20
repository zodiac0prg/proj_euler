def gen_pent_num(a):
    return a * (3 * a - 1)/2

pent_list=[]

NUM = 10000
i = 1
for i in range(1, NUM):
    pent_list.append(gen_pent_num(i))

d = 0
print ("Pent list created")
print (len(pent_list))

for i in range(0, len(pent_list)):
    for j in range(i, len(pent_list)):
        if (pent_list[i] + pent_list[j]) in pent_list and abs(pent_list[i] - pent_list[j]) in pent_list:
            temp = abs(pent_list[i] - pent_list[j])
            print (pent_list[i])
            print (pent_list[j])
            break



