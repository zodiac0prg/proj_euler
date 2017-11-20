NUM = 100

def sum_of_squares( max_num):
    sum = 0

    for i in range(1,max_num + 1):
        sum += i * i
    
    return sum


def square_of_sum( max_num):
    sum = 0

    for i in range(1,max_num + 1):
        sum += i

    return sum * sum

print square_of_sum(NUM) - sum_of_squares(NUM)
