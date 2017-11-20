
NUM = 1000
def check_palindrome(a):
    b = 0;
    org = a
    b += a % 10
    
    while True:
        if (a / 10 > 0):
            a = a / 10
            b = b * 10
            b += a % 10
        else:
            break
    
    if (b == org):
       return True
    return False

palindromes=[]
for i in range(NUM - 1, (NUM/10) + 1, -1):    
    for j in range (NUM - 1, (NUM/10) + 1, -1):
        if (check_palindrome(i * j)):
            palindromes.append(i * j)

print max(palindromes)
