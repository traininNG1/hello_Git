numbers = [2,4,5,10,12]

def find_sqr(numbers):
    sqr =[]
    n=iter(numbers)

    while True:
        try:
            a = next(n)**2
            print(a)
        except StopIteration:
            break
    return sqr
        

find_sqr(numbers)
 
        