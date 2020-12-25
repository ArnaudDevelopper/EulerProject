first,second = 1,2
summ = 0
while second <= 4000000:
    if second%2==0:
        summ += second
    first,second = second,first+second
print(summ)