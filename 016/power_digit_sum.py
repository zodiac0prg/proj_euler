num = 2**1000

max_sum = 0

while True:
    if (num / 10):
        max_sum += num % 10
        num = num / 10
    else:
        max_sum += num
        break
print max_sum


