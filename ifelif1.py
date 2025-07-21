a= int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
e = int(input("Enter fifth number: "))

if a >= b and a >= c and a >= d and a >= e:
    print(f"{a} is the greatest number.")
elif b >= c and b >= d and b >= e:
    print(f"{b} is the greatest number.")
elif c >= d and c >= e:
    print(f"{c} is the greatest number.")
elif d >= e:
    print(f"{d} is the greatest number.")
else:
    print(f"{e} is the greatest number.")
