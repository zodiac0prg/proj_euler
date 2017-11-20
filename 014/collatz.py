
large_num = 0
large_count = 0
NUM = 1000000

def gen_collatz(a):
    global large_count, large_num

    count = 1
    num = a
    while True:
        if (num == 1):
            break
        if (num % 2 != 0):
            num = 3 *num  + 1
        else:
            num = num / 2
        count += 1

    if (count > large_count):
        large_count = count
        large_num = a

i = 1

while True:
    gen_collatz(i)
    i += 1
    if (i == NUM):
        break

print large_num, large_count
