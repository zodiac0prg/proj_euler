
num_list = [1, 2, 5, 10, 20, 50, 100, 200]

def give_index (target):
    index = 0
    for i in num_list:
        if i == target:
            break
        if i > target:
            index -= 1
            break
        index += 1
    return index

def num_ways (target, start_index):
    #index = give_index(target)
    y = start_index

    print "Reached here with target ", target, " start_index ", start_index
    count = 0
    i = 1

    if (y == 0):
        return 1;

    while True:
        print "i is and num_list[y] is ", i , num_list[y]
        if (i * num_list[y] == target):
            #print "i is and num_list[y] is ", i , num_list[y]
            count += 1
            i += 1
        elif (i * num_list[y] < target):
            temp = target - (i * num_list[y])
            print "temp is ", temp
            
            count += num_ways(temp, y - 1)
            #count -= 1
            i += 1
                
        elif (i * num_list[y] > target):
            y -= 1
            i = 1
            if (y == 0):
                count += 1
                break
    print "count is ", count
    return count

print "NUM WAYS 200"
target = 200
index = give_index(target)
print "Starting index ", index
print num_ways(target, index)

