
with open("test1.txt") as f:
    content = f.read().splitlines()

numbers = []
for i in content:
    numbers.append([int(j) for j in i.split()])

num_layers = len(numbers)    

numbers2 = []

for i in numbers:
    for j in i:
        numbers2.append(j)

tot_len = len(numbers2)
i = (tot_len - 1) - (num_layers - 1) - (num_layers - 1)
j = i + (num_layers - 1)
k = (num_layers - 1)
start_i = i

while True:
    
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
        continue

if (numbers2[0] + numbers2[1] > numbers2[0] + numbers2[2]):
    print "Max sum is ", numbers2[0] + numbers2[1]
else:
    print "Max sum is ", numbers2[0] + numbers2[2]

