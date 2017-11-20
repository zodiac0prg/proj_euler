from math import sqrt

prime_list = [2, 3, 5, 7]

def num_to_list(num):
    c = []
    a = str(num)
    for i in a:
        c.append(int(i))
    return c

def list_to_num(a):
    b = ""
    for i in a:
        b += str(i)
    return int(b)

def is_prime(num):
    fact_num = []
    limit = sqrt(num)
    i = 1
    while True:
        if num % i == 0:
            fact_num.append(i)
            if (num/i != i):
                fact_num.append(num/i)

        i += 1
        if (i > limit):
            break
    if (len(fact_num) == 2):
        return True
    return False

def check_trun_prime(num):
    num_list = num_to_list(num)
    
    # Truncate from left
    for i in range(len(num_list)):
        a = num_list[i:]
        num_a = list_to_num(a)
        if (not is_prime(num_a)):
            return False

    # Truncate from right
    for i in range(len(num_list) - 1, 0, -1):
        a = num_list[:i]
        num_a = list_to_num(a)
        if (not is_prime(num_a)):
            return False

    return True

num = 10
count = 0
trun_prime_list = []
while True:
    if (check_trun_prime(num)):
        count += 1
        trun_prime_list.append(num)
        if (count == 11):
            break

    num += 1

print "List is ", trun_prime_list
print "Sum is ", sum(trun_prime_list)
