
num = 1
digit_count = 1
constant_string = ""

while True:
    constant_string += str(num)
    digit_count = len(constant_string)
    if (digit_count >= 1000001):
        break
    num += 1

i = 1
prod = 1
while True:
    prod *= int(constant_string[i - 1])
    i = i * 10
    if (i >= 1000001):
        break

print prod
