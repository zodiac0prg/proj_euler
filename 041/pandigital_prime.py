from math import sqrt

num_list = [1, 2, 3, 4, 5, 6, 7]

def list_to_num(num_list):
    num_str = ""
    for i in num_list:
        num_str += str(i)

    return int(num_str)

def magic(number):
    return (''.join(str(i) for i in number))

perm_list = []

def perm(a,k=0):
   global perm_list
   #print "Entering perm with ", a, " and k is ", k 
   if(k == len(a)):
       #print "Reached here"
       perm_list.append(magic(a))
   else:
      for i in xrange(k,len(a)):
          #print i, k, a
          a[k],a[i] = a[i],a[k]
          perm(a, k+1)
          a[k],a[i] = a[i],a[k]

def is_prime(num):
    fact_num = []
    limit = sqrt(num)
    i = 1
    while True:
        if num % i == 0:
            fact_num.append(i)
            if (num/i != i):
                fact_num.append(num/i)

        i += 1
        if (i > limit):
            break
    if (len(fact_num) == 2):
        return True
    return False


"""
some simple analysis:

pandigital numbers for 1 though 9 are divisible by 3 (1 + 2 + ....+ 9 = 45).
This is also true for pandigital numbers from 1 to n for n=1, 2, 3, 5, 6, 8

so this leaves checking for n = 4, 7
we start with 7 as we are interested in the largest pandigital number.
It turns out that there are plenty of primes in this space and so we dont even
need to check for n=4 case.
"""
max_prime = 0

perm(num_list)
for i in perm_list:
    if (is_prime(int(i))):
        if (i > max_prime):
            max_prime = i
       
print max_prime



