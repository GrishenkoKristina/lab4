def q0():
    a = int(input())
    if a%3 == 0:
        print("делится нацело")
    else:
        print("не делится нацело")

def q1():
    try:
        a = int(input())
        b = 100/a
    except ValueError:
        print("строки запрещены")
    except ZeroDivisionError:
        print("делить на ноль нельзя")
    else:
        print(b)

def q2():
    a = int(input("день "))
    b = int(input("месяц (номер) "))
    c = int(input("год (полностью) "))
    if a*b == c%100:
        print("дата магическая")
    else:
        print("дата не магическая")

def q3():
    n = input()
    q = 0
    w = 0
    if len(str(n)) % 2 == 0:
        for i in (0, len(str(n)) / 2):
            q = q + int(i)
        for i in n[int(len(n) / 2):int(len(n))+1]:
            w = w + int(i)
        if q == w:
            print("билет счастливый")
        else:
            print("билет несчастливый")
    else:
        print("№ билета не подходит")


q0()
q1()
q2()
q3()