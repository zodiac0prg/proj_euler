def num_factors (a):
    if a == 1:
        return 1
    
    count = 2

    for i in range(2,a):
        if (a % i == 0):
            count += 1

    return count

def gen_triangle_number (a):

    b = 0

    for i in range (1,a +1):
        b += i
    return b

i = 1
while True:
    a = gen_triangle_number(i)
    if (num_factors(a) >= 500):
        print a
        break;
    i += 1


