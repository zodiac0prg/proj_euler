from math import sqrt

fact_sum = 0;
num_dict = {}
num = 1
amicable_list = []

while True:
    fact_sum = 0
    limit = sqrt(num)
    i = 1
    while True:
        if num % i == 0:
            fact_sum += i
            if (num/i != i):
                fact_sum += (num/i)

        i += 1
        if (i > limit):
            break
    num_dict[num] = fact_sum - num   
    #print num, fact_sum - num    
    num += 1
    if (num == 10000):
        break
            
print num_dict

for i in num_dict:
    print i
    count = num_dict[i]
    if count in num_dict:
        print "Count exist ", count
        if num_dict[count] == i and i != count:
            print "Amicable? " , count , i
            if count not in amicable_list:
                amicable_list.append(i)
                amicable_list.append(count)

print amicable_list
print sum(amicable_list)
