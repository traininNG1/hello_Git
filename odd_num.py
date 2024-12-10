#Calculate sum of all odd numbers from 1 to 50?

def odd_sum():
    sum = 0
    for i in range(1,51):
        if i%2 !=0:
            sum = sum+i
    return sum
result = odd_sum()
print("The sum of odd numbers upto 50 is",result)



