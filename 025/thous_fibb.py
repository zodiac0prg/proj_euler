i = 1
j = 1

count = 2

while True:
    temp = j
    j += i
    i = temp

    count += 1

    if len(str(j)) == 1000:
        print j
        break

print count    
