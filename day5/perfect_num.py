sum = 0
for num in range(1,100):
    for counter in range(1,num):
        if num % counter == 0:
            sum =  sum + counter
    if sum == num:
        print(num)
        sum = 0
