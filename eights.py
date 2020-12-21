count = 0
eights = 0
total = 0
while count != 2000000:
    n = count 
    digits = [int(x) for x in str(n)]
    count += 1
    if 8 in digits:
        total = (total + (count - 1))
        eights += 1
print(eights)
print(total)