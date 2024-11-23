def square(num):
    return num ** 2


def list_range(num):
    nums = []
    for i in range(1, num + 1):
        nums.append(i)
    return nums


def square_root(num):
    return num ** 0.5


def even_odd_int(num):
    if (num % 2) == 0:
        return ('Четное')
    else:
        return ('Нечетное')


def main():
    x = int(input("Введите число:"))
    answer = int(input(
        '''Выберете действие:
           1. Квадрат числа;
           2. Корень числа;
           3. Список чисел;
           4. Четное/Нечетное
        '''
        )
    )
    if answer == 1:
        print(square(x))
    elif answer == 2:
        print(square_root(x))
    elif answer == 3:
        print(list_range(x))
    elif answer == 4:
        print(even_odd_int(x))
    else:
        print('Действие еще не добавлено.')
        main()


if __name__ == "__main__":
    main()
