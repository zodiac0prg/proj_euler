class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def value(self):
        print self.data

with open("test2.txt") as f:
    content = f.read().splitlines()

#print content
numbers = []
for i in content:
    #print i.split()
    numbers.append([int(j) for j in i.split()])

num_layers = len(numbers)    

numbers2 = []

for i in numbers:
    for j in i:
        numbers2.append(j)

print numbers2
tot_len = len(numbers2)
i = (tot_len - 1) - (num_layers - 1) - (num_layers - 1)
j = i + (num_layers - 1)
k = (num_layers - 1)
start_i = i
#print tot_len, i, j ,k

while True:
    
    #print "Before start"
    #print start_i, i, j ,k
    
    if (numbers2[i] + numbers2[j] > numbers2[i] + numbers2[j+1]):
        numbers2[i] += numbers2[j]
    else:
        numbers2[i] += numbers2[j+1]

    i += 1
    j += 1

    if ((i - start_i) == k):
        k -= 1
        if (k == 1):
            break
        start_i -= k 
        i = start_i
        j = i + k
        #print "After start"
        #print start_i, i, j ,k
        continue

#print numbers2
if (numbers2[0] + numbers2[1] > numbers2[0] + numbers2[2]):
    print "Max sum is ", numbers2[0] + numbers2[1]
else:
    print "Max sum is ", numbers2[0] + numbers2[2]
'''
while True:
    print "Comparing ", numbers2[j], "and ",  numbers2[j + 1]
    if (numbers2[j + 1] > numbers2[j]):        
        k = j + 1
        max_sum += numbers2[j + 1]
    else:
        k = j
        max_sum += numbers2[j]
    
    print "Before update"
    print i, j ,k

    i += 1
    k += (i)
    j = k

    print "After update"
    print i, j ,k

    if i == len(numbers):
        break

print max_sum
'''


