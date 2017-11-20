
def give_diag_elem(dim):
    diag_elem = []
    num = 1; mark = 1; last_add = 0;

    while True:
        if (mark > dim):
            break
        if last_add == 0:
            print num
            diag_elem.append(num)
            last_add = num
        else:
            print last_add, mark , num
            if (last_add + mark - 1 == num):
                print num
                diag_elem.append(num)
                last_add = num
        
        if (num == mark * mark):
            mark += 2
        
        num += 1

    return diag_elem

print sum(give_diag_elem(1001))
