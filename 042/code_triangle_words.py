word_value_list = []

triangle_num_list = []

def word_value(word):
    score = 0
    for i in word:
        #print i
        if i == '\'':
            continue
        elif i == '\"':
            continue
        else:            
            score += ord(i) - ord('A') + 1
    return score

with open("p042_words.txt") as f:
    content = f.read().split(',')

for i in content:
    word_value_list.append(word_value(i))

#print max(word_value_list)

num = 1
while True:
    triangle_num = num * (num + 1)/2
    triangle_num_list.append(triangle_num)

    num += 1

    if (triangle_num >= max(word_value_list)):
        break

triangle_word_count = 0

for i in word_value_list:
    if i in triangle_num_list:
        triangle_word_count += 1

print triangle_word_count
