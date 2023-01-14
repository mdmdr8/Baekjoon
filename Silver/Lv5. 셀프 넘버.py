numbers = list(range(1,10001))
remove_li = []

for num in numbers:
    for n in str(num):
        num+= int(n)
    if num <= 10000:
        remove_li.append(num)
for re in set(remove_li):
    numbers.remove(re)
for self_num in numbers:
    print(self_num)