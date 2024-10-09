
string = "Mahendra-6066681"

alpha_count = 0
num_count = 0

for i in string:
    if i.isalpha():
        alpha_count +=1
    elif i.isnumeric():
        num_count +=1
        
print(alpha_count, num_count)
