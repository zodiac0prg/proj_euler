from math import sqrt

num = 1

prime_list = []

def quad_formula (num, a, b):
    return (num * num) + a * num + b

def is_prime(num):
    if num in prime_list:
        return True
    return False

while True:
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
        prime_list.append(num)
    #print num, fact_sum - num    
    num += 1
    if (num == 10000):
        break

max_a = 0
max_b = 0
max_prime_count = 0 

for a in range(-1000, 1000):
    for b in range(-1000, 1001):
        num = 0
        prime_count = 0
        while True:
            if (is_prime(quad_formula(num, a, b))):
                prime_count += 1
                num += 1            
            else:
                break
        if (prime_count > max_prime_count):
            max_prime_count  = prime_count
            max_a = a
            max_b = b
            
    
print max_prime_count
print max_a
print max_b
print max_a * max_b
#print prime_count
    

#print prime_list
