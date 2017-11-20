
def is_prime (a):
    count = 0
    for i in range(2, a):
        if (a % i == 0):
            count += 1

    if (count == 0):
        return True
    return False        

i = 2;
prime_list=[]
count = 0

while True:
    if(is_prime(i)):
        prime_list.append(i)
        count += 1
    i += 1    
    if (count > 10002):
        break

print prime_list[1 -1]
print prime_list[6 -1]
print prime_list[100 -1]
print prime_list[10001 -1]
