stat1 = 5
if stat1 == 18:
    strmod = '+3'
elif stat1 <= 17 and stat1 >= 16:
    strmod = '+2'
elif stat1 <= 15 and stat1 >= 13:
    strmod = '+1'
elif stat1 <= 12 and stat1 >= 9:
    strmod = '0'
elif stat1 <= 8 and stat1 >= 6:
    strmod = '-1'
elif stat1 <= 5 and stat1 >= 4:
    strmod = '-2'
elif stat1 == 3:
    strmod = '-3'
print(strmod)