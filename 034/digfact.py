dig_fact = {}

dig_fact[1] = dig_fact[0] = 1

for i in range(2,10):
    dig_fact[i] = i * dig_fact[i-1]

def num_to_list(num):
    c = []
    a = str(num)
    for i in a:
        c.append(int(i))
    return c

def check_fact_sum (num):
    num_list = num_to_list(num)

    tot_sum = 0
    for i in num_list:
        tot_sum += dig_fact[i]

    if (tot_sum == num):
        return True

    return False

"""
Safe to keep this as the upper limit as 9! * 7 is 2540160 which is less than
9999999.
"""
MAX_NUM = 9999999

tot_sum = 0
for i in range(3, MAX_NUM):
    if (check_fact_sum(i)):
        tot_sum += i

print tot_sum


