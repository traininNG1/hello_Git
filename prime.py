
def prime_check(num):
    if num<=1:
        print(num,"is not a prime number, enter a number greater than 1")
        return
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            print(num,": is not a prime number")
            return
    else:
        print(num,": is a prime number")
num = int(input("Enter the number:"))
prime_check(num)



