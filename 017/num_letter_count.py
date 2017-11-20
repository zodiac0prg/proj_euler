num_letter= {
        1  : len('one'),
        2  : len('two'),
        3  : len('three'),
        4  : len('four'),
        5  : len('five'),
        6  : len('six'),
        7  : len('seven'),
        8  : len('eight'),
        9  : len('nine'),
        10 : len('ten'),
        11 : len('eleven'),
        12 : len('twelve'),
        13 : len('thirteen'),
        14 : len('fourteen'),
        15 : len('fifteen'),
        16 : len('sixteen'),
        17 : len('seventeen'),
        18 : len('eighteen'),
        19 : len('nineteen'),
        20 : len('twenty'),
        30 : len('thirty'),
        40 : len('forty'),
        50 : len('fifty'),
        60 : len('sixty'),
        70 : len('seventy'),
        80 : len('eighty'),
        90 : len('ninety'),
        100: len('hundred'),
        1000: len('thousand')}

def ret_num_letters(a):
    if a == 1000:
        return num_letter[1] + num_letter[1000]
    if (a <= 20):
        return num_letter[a]
    if (a < 100):
        if (a % 10 == 0):
            return num_letter[a]
        else:
            return num_letter[a % 10] + num_letter[(a/10) * 10]
    elif (a >= 100):
        if (a % 100 == 0):
            return num_letter[a/100] + num_letter[100]
        else:
            temp = a % 100
            #print temp

            if temp < 20 or temp % 10 == 0:
                return num_letter[a/100] + num_letter[100] + num_letter[temp] + 3
            else:
                return num_letter[a/100] + num_letter[100] + num_letter[temp % 10] + num_letter[(temp/10) * 10] + 3    

count = 0
i = 1

while True:
    #print i
    count += ret_num_letters(i)
    i += 1
    if i == 1001:
        break

print count
#print ret_num_letters(801) # eight hundred and one = 5 + 7 + 3 + 3 = 18
