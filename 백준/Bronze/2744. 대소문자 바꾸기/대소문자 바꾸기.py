a = input()

str_list = []

for i in range(len(a)):
    if (a[i].isupper() == True):
        str_list.append(a[i].lower()) 
    else :
        str_list.append(a[i].upper())
        
print("".join(str_list))