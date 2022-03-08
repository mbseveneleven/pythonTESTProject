name = input("What is your name? ")
c = '+'
if name == 'Vladimir':
    print("Hello", name, "!")

    a = input("Input value of 'a'!")
    b = input("Input value of 'b'!")

    while c == '+' or '-' or '*' or '/':
        c = input("Input arithmetic sign, pls!")
        if c == '+':
            c = float(a) + float(b)
            print("a + b = ", c)
        elif c == '-':
            c = float(a) - float(b)
            print("a - b = ", c)
        elif c == '*':
            c = float(a) * float(b)
            print("a * b = ", c)
        elif c == '/':
            c = float(a) / float(b)
            print("a / b = ", c)
        elif c == '0':
            break
        else:
            print("Incorrect sign! For exit input 0")
else:
    exit(-1)

print(c)
