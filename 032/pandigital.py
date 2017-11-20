
pandigital = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def num_to_list(num):
    num_list = []

    a = str(num)
    for i in a:
        num_list.append(i)
    return num_list

def check_pandigital (a, b ,c):
    
    a_list = num_to_list(a)
    b_list = num_to_list(b)
    c_list = num_to_list(c)

    a_list += b_list + c_list

    a_list.sort()

    if (a_list == pandigital):
        return True

    return False

prod_list = []
for i in range(10, 100):
    for j in range(100, 1000):
        temp = i*j
        if (check_pandigital(i, j , temp)):
            if temp not in prod_list:
                print i, j , temp
                prod_list.append(temp)

for i in range(2, 10):
    for j in range(1000, 10000):
        temp = i*j
        if (check_pandigital(i, j , temp)):
            if temp not in prod_list:
                print i, j , temp
                prod_list.append(temp)

print sum(prod_list)    
