from math import sqrt

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
    if num in prime_list:
        return True
    return False

def provide_rotate_list(num):
    num_list = num_to_list(num)
    rot_list = []
    for i in range(len(num_list)):
        a = num_list[i:] + num_list[:i]
        rot_list.append(list_to_num(a))

    return rot_list

num = 1

prime_list = []


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
    #print num
    if (num == 1000000):
        break

print "Done with prime list generation"

num = 2
circ_prime_list = []

for i in prime_list:
    rot_list = provide_rotate_list(i)
    circ_prime_check = True
    for j in rot_list:
        if (j not in prime_list):
            circ_prime_check = False
            break
    if (circ_prime_check):
        #print i
        circ_prime_list.append(i)
            
print "Circular Prime list is ", circ_prime_list
print "Number of Circular primes below 1 million ", len(circ_prime_list)





