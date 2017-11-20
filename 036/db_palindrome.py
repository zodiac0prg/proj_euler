

def check_bin_palindrome(num):
    c = []

    bin_str = str(bin(num))[2:]
    for i in bin_str:
        c.append(int(i))
    
    return (c == c[::-1])

def check_num_palindrome(num):

    c = []
    for i  in str(num):
        c.append(int(i))
    
    return (c == c[::-1])

MAX_NUM = 1000000

num = 1
max_sum = 0
while True:
    if (check_bin_palindrome(num) and check_num_palindrome(num)):
        #print num
        max_sum += num
    num += 1
    if (num == MAX_NUM):
        break

print max_sum
