#калькулятор Егор и Ильдар)
a = int(input())
b = int(input())
c = str(input())
if c == "+": 
    z = a + b
    print(int(z))
elif c == "-":
    z = a - b
    print(int(z))
elif c == "*":
    z = a * b
    print(int(z))
elif c == "/":
    if b == 0: 
        print('На ноль делить нельзя!')
    else:
        z = a / b
        print(int(z))
else: 
    print('Неверная операция')
