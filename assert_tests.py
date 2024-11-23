from prob_test import square, square_root, even_odd_int, list_range

assert square(4) == 16, 'Неверно посчитан квадрат числа'
assert square_root(4) == 2, 'Неверно посчитан корень числа'
assert even_odd_int(4) == 'Четное', 'Неверно определена четность числа'
assert list_range(4) == [1, 2, 3, 4], 'Неверный список'
