def check_even_or_odd(c):
    if c % 2 == 0:
        return "even"
    else:
        return "odd"

c= int(input("Enter an integer: "))
print("The number is", check_even_or_odd(c))
