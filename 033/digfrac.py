def num_to_list (num):
    c = []
    a = str(num)
    for i in a:
        c.append(i)
    return c

def list_to_num (num_list):
    return int(num_list[0])

def check_digit_cancel(i, j):
    i_list = num_to_list(i)
    j_list = num_to_list(j)

    i_list_copy = list(i_list)
    j_list_copy = list(j_list)
    
    for a in i_list:
        if a in j_list:
            i_list_copy.remove(a)
            j_list_copy.remove(a)
            a_num = list_to_num(i_list_copy)
            b_num = list_to_num(j_list_copy)
            if (float(float(a_num)/float(b_num)) == float(i)/float(j)):
                return True
            break
    return False

frac_list = []

for i in range (10, 100):
    for j in range (i+1, 100):
        if (i % 10 != 0 and j % 10 != 0):
            if check_digit_cancel(i, j):
                frac_list.append([i, j])

print frac_list
