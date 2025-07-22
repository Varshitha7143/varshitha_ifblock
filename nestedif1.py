a=int(input('enter first num:'))
b=int(input('enter second num:'))
c=int(input('enter third num:'))
d=int(input('enter fourth num:'))

if a>b:
    if a>c:
        if a>d:
            print(f'a={a} is max')
        else:
            print(f'd={d} is max')
    else:
        if c>d:
            print(f'c={c} is max')
        else:
            print(f'd={d} is max')
            
else:
    if b>c:
        if b>d:
            print(f'b={b} is max')
        else:
            print(f'a={a} is max')
    else:
        if c>d:
             print(f'c={c} is max')
        else:
             print(f'd={d} is max')
            
