
words = [0,0,0,1,1,3,4]
dict1 = {}
for i in words:
    if i not in dict1.keys():
        dict1[i] = words.count(i)
print(dict1)
