a = input()
b = input()
c = input()

scr_er = 0
war_num = 1

try:
    a = float(a)
except ValueError:
    print("Предупреждение#{}:\nпервое число не число".format(war_num))
    scr_er += 1
    war_num += 1
    pass

if b != "+" and b != "-" and b != "/" and b != "*":
    print("Предупреждение#{}:\nя не знаю эту команду".format(war_num))
    scr_er += 1
    war_num += 1

try:
    c = float(c)
except ValueError:
    print("Предупреждение#{}:\nвторое число не число".format(war_num))
    scr_er += 1
    pass

while scr_er == 0:
    if b == "-":
        print(a - c)
    elif b == "+":
        print(a + c)
    elif b == "/":
        print(a / c)
    elif b == "*":
        print(a * c)
    break
