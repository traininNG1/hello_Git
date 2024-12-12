def case_check(n):
    match n:
        case n if n<0:
            print(f"{n} : is negative")
        case n if n>0:
            print(f"{n} : is positive")
        case n if n==0:
            print(f"{n} : is zero")
n = float(input("Enter the number:"))
case_check(n)