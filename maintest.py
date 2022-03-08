name = input("What is your name? ")

if name == 'Vladimir':
    print("Hello", name, "!")

    a = input("Input value of 'a'! ")
    sign = '+'
    while sign == '+' or '-' or '*' or '/':
        sign = input("Input arithmetic sign, pls! For exit input '0' ")
        if sign == '0':
            break
        else:
            b = input("Input value of 'b'! ")
            if sign == '+':
                a = float(a) + float(b)
                print("a + b = ", a)
            elif sign == '-':
                a = float(a) - float(b)
                print("a - b = ", a)
            elif sign == '*':
                a = float(a) * float(b)
                print("a * b = ", a)
            elif sign == '/':
                a = float(a) / float(b)
                print("a / b = ", a)
            else:
                print("Incorrect sign! For exit input 0")


else:
    print("Wrong name!")
    exit(-1)

print(a)
