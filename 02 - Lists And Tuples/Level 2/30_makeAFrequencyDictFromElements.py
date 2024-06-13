# list = ["a","a","b","c","a","b"]
list = [1,2,3,4,3,2,1,2]
unique = sorted(set(list))
dic = {}

for item in unique:
    count = 0
    for char in list:
        if item == char:
            count += 1
    dic[item] = count

print(dic)