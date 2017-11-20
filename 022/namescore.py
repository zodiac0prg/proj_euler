

print (ord('C') - ord('A')) + 1

def name_score(name, index):
    score = 0
    for i in name:
        #print i
        if i == '\'':
            continue
        elif i == '\"':
            continue
        else:            
            score += ord(i) - ord('A') + 1
    return score * (index)

with open("p022_names.txt") as f:
    content = f.read().split(',')

#print content
content.sort()
#print content

index = 0
tot_name_score = 0

for i in content:
    tot_name_score += name_score(i, index + 1)
    index += 1
    
print tot_name_score
    
