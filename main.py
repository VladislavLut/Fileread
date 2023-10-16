goods = ['Пепсі(2л)', 39.00, 'Сир косічка (1кг)', 415.00, 'Сир сулугуні(1кг)', 250.00, 'Суші(1кг)', 840.50, 'Бургер(1кг)', 160.00
         , 'Ребра свинні(200г)', 55.00, 'Салака г/к(200г)', 68.00, 'Гречка(1кг)', 150.00, 'Крупа Артек(1кг)', 400.00, 'Паніні(500г)', 150.00, 'куряче філе', 17.90, 'свинна лопатка', 19.80, 'сало', 19.80, 'Борщ', 7.80, 'пончики', 9.80, 'Крильця смажені', 10.50, 'Кровлянка', 16.82, 'Телятена', 18.40, 'Голубці', 50.00, 'Живчик', 33.00, 'Тушена капуста', 150.00, 'Сільодка під шубою', 299.99]
users = ['vladlutsenko@gmail.com', '1111']
admins = ['vl@admin.com', 'qwerty']
basket = []
admin_email_pattern = '@admin.com'

is_login_true = False
is_admin = False
try:
    #Авторизація
    while True:
        while True:
            login = input("Введіть логін: ")
            password = input("Введіть пароль: ")

            if admin_email_pattern in login:
                if admins.count(login) == 0:
                    print("Такого адміністратора не існує. Спробуйте ще раз")
                    continue
                if admins[admins.index(login) + 1] == password:
                    print("Ви увійшли як адміністратор")
                    is_admin = True
                    break
                else:
                    print("Пароль не вірний. Спробуйте ще раз")

                    continue



            elif login in users:
                if users[users.index(login) + 1] == password:
                    print(f"Ви ввійшли як користувач - {login}")
                    with open("admins.txt", "r", encoding="utf8") as file:
                        str = file.read()
                    print(str, end="")
                    while True:
                        print('Для виходу введіть "exit"')
                        print('Для додавання товару введіть "add"')
                        print('Для видалення товару введіть "del"')
                        print('Для виходу від адміністратора введіть "exit admin"')
                        answer = input("Введіть команду: ")
                        if answer == 'exit':
                            exit()
                        elif answer == 'add':
                            name = input("Введіть назву товару: ")
                            price = input("Введіть ціну товару: ")
                            goods.append(name)
                            goods.append(price)
                            print("Товар додано")
                        elif answer == 'del':
                            name = input("Введіть назву товару: ")
                            if name in goods:
                                goods.remove(name)
                                goods.remove(goods[goods.index(name) + 1])
                                print("Товар видалено")
                            else:
                                print("Такого товару не існує")
                        elif answer == 'exit admin':
                            is_admin = False
                            break



                else:
                    print("Пароль не вірний")
            else:
                print("Користувача з таким логіном не існує")
                print("Бажаєте зареєструватися?")
                answer = input("Ведіть так або ні: ")
                if answer == 'так':
                    users.append(login)
                    users.append(password)
                    print("Ви успішно зареєструвались")
                    print("Ви можете увійти в систему")


        while True:
            if is_admin == True:
                print('Ви ввійшли як адміністратор')
                with open("users.txt", "r", encoding="utf8") as file:
                    str = file.read()
                print(str, end="")

                while True:
                    print('Для виходу введіть "exit"')
                    print('Для додавання товару введіть "add"')
                    print('Для видалення товару введіть "del"')
                    print('Для виходу від адміністратора введіть "exit admin"')
                    answer = input("Введіть команду: ")
                    if answer == 'exit':
                        exit()
                    elif answer == 'add':
                        name = input("Введіть назву товару: ")
                        price = input("Введіть ціну товару: ")
                        goods.append(name)
                        goods.append(price)
                        print("Товар додано")
                    elif answer == 'del':
                        name = input("Введіть назву товару: ")
                        if name in goods:
                            goods.remove(name)
                            goods.remove(goods[goods.index(name) + 1])
                            print("Товар видалено")
                        else:
                            print("Такого товару не існує")
                    elif answer == 'exit admin':
                        is_admin = False
                        break
            else:
                counter = 0
                for i in range(0, len(goods), 2):
                    counter += 1
                    print(f"{counter} : {goods[i]}\t\t{goods[i + 1]}грн")
                print('Який продукт бажаєте купити?')
                print('Для виходу введіть "exit"')
                answer = input("Введіть назву продукту: ")
                if answer == 'exit':
                    print('Бажаєте вийти з програми?')
                    answer = input("Введіть так або ні: ")
                    if answer == 'так':
                        print('До зустрічі!')
                        exit()
                    else:
                        break

                else:
                    if answer in goods:
                        basket.append(answer)
                        print("Продукт додано до кошика")
                    else:
                        print("Такого продукту не існує")
                        continue
            break



except Exception as e:
    print(e)