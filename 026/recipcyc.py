from decimal import *

getcontext().prec = 100

num = 2

num_list = []
num_dict = {}
rem_list = []


while True:
    temp =  Decimal(1)/Decimal(num)
    number_dec = str(temp)[2:]
    num_list.append(number_dec)
    print num, number_dec
    num += 1
    if (num == 20):
        break

#print num_list  

def convert_num_to_list(num):
    b = str(num)
    c = []

    for digit in b:
        c.append( int(digit))
    return c    

def update_reci_cycle(num):
    global repeat_list
    global num_dict
    length = 0
    alt_list = []
    index = 0
    diff = 0
    for j in num:
        if j not in repeat_list:
            repeat_list.append(j)
            index += 1
        else:
            k = repeat_list.index(j)
            alt_list.append(j)
            print repeat_list[k:]
            count = len(repeat_list[k:])
            if (count == 1):
                count += 4
                
            for m in range(0, count-1):
                print m
                if (num[index] != num[index+1]):
                    diff = 1
                index += 1
                alt_list.append(num[index])

            if (alt_list == repeat_list[k:]):
                length = len(repeat_list[k:])
                num_dict[i] = length
                print "Repeat_list", repeat_list
                break
            else:
                if (diff == 0):
                    length = 1
                    num_dict[i] = length
                    print "Repeat list ", repeat_list            
                    break
                else:
                    print "Alt list", alt_list
                    repeat_list += alt_list
                    continue

            """
            if (diff == 0):
                length = 1
                num_dict[i] = length
                print "Repeat list ", repeat_list            
                break
            else:
                repeat_list += alt_list
                continue
            """
            
            if (k == len(repeat_list) - 1):                
                length = 1
                num_dict[i] = length
                print "Repeat list ", repeat_list            
                break
            else:
                length = len(repeat_list[k:])
                num_dict[i] = length
                print "Repeat list ", repeat_list            
                break

    print "Length is ", length  

"""
for i in num_list:
    repeat_list = []
    num = convert_num_to_list(i)
    print i
    if len(num) >= 10:
        update_reci_cycle(num)
"""        
#print (num_dict)


num = 2;
num_dict = {}
rem_list = []
max_count = 0
max_num = 1

while True:
    print "Number is ", num
    rem = 1 % num
    count = 1
    rem_list = []
    rem_list.append(rem)
    while (rem != 0):
        rem = (10 * rem) % num
        print "Remainder ", rem
        if (rem != 0):
            if (rem not in rem_list):
                rem_list.append(rem)
                count += 1
            else:
                #num_dict[num] = count
                print rem_list
                if (max_count < count):
                    max_count = count
                    max_num = num
                print "Count is ", count
                break
        else:
            if (len(rem_list) == 0):
                rem *= 10
            else:
                print rem_list

    num += 1
    if (num == 1000):
        break

#print num_dict

print "Number with longest recurring fractional cycle is ", max_num," and the count is ", max_count 
