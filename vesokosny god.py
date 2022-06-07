print('Ну приветик')
while 1:
    try:
        god = int(input("Введи год: "))
        if god % 4 != 0:
            print('Год не високосный.');
        elif god % 100 == 0:
            if god % 400 == 0:
                print('Год високосный.')
            else:
                print('Год не високосный.')
        else:
            print('Год високосный.')
        print("Бб")
    except:
        print("Не число")
        print("ты чо")

input()