from math import pow

pow_check = 5

def num_to_list(num):
    c = []
    num_str = str(num)

    for i in num_str:
        c.append(i)
    return c

def check_num(num):

    dig_list = num_to_list(num)
    sum_dig = 0
    for i in dig_list:
        sum_dig += (pow(float(i), pow_check))

    if (sum_dig == num):
        return True
    return False

num = 1
num_list = []
while True:
    if (check_num(num)):
        num_list.append(num)

    num += 1
    if (num == 10000000):
        break

print num_list
