"""
Rather than using brute force, let us use some analysis to shrink our search
space for this problem.

Since we want the largest pandigital number, "n" should probably start with 9.

The integer "n" cannot have 5 digits or more since (n * 1) yields a 5 digit number,
and (n *2) would yield atleast another 5 digit number. Total would be 10 digits,
which would fail the 1 through 9 pandigital condition.

"n" cannot be a 2-digit number. (n*1) <+> (n*2) <+> ... would yield a 8-digit
number after concatenation with n *3 and a 11-digit number after (n*4) and so on.

For the same reason, n also cannot be a 3-digit number.

So the solution space is from 9123 to 9876.

"""

pandigital = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def num_to_list(num):
    num_list = []

    a = str(num)
    for i in a:
        num_list.append(i)
    return num_list

def list_to_num(a):
    b = ""
    for i in a:
        b += i

    return int(b)

def check_pandigital (a, b):
    
    a_list = num_to_list(a)
    b_list = num_to_list(b)
    
    a_list += b_list
    
    a_list.sort()

    if (a_list == pandigital):
        return True

    return False

num = 9123
max_pan_num = 123456789

while True:

    if (check_pandigital(num * 1, num * 2)):
        num1_list = num_to_list(num * 1)
        num2_list = num_to_list(num * 2)

        num1_list += num2_list

        pan_num = list_to_num(num1_list)

        if (pan_num > max_pan_num):
            max_pan_num = pan_num

    num += 1
    if (num == 9877):
        break
    
print max_pan_num

