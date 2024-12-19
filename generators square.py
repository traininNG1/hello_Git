def square(numbers):
    for n in numbers:
        yield n**2

numbers =[2,4,3,10]

val = square(numbers)
for i in val:
    print(i)