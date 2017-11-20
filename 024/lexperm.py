
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

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

perm(num_list)
perm_list.sort()
print perm_list[999999]


