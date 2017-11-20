def gen_triangle_num(a):
    return a * (a + 1)/2

def gen_pent_num(a):
    return a * (3 * a - 1)/2

def gen_hex_num(a):
    return a * (2 * a - 1)

trian_list=[]
pent_list=[]
hex_list=[]

NUM = 1000000
i = 1
for i in range(1, NUM):
    trian_list.append(gen_triangle_num(i))
    pent_list.append(gen_pent_num(i))
    hex_list.append(gen_hex_num(i))

for i in trian_list:
    if i in pent_list and i in hex_list:
        print(i)
