# Определить, является ли год, который ввел пользователем, високосным или не високосным.
# Високосными годами считаются:
#   1. год, номер которого кратен 400, — високосный;
#   2. остальные годы, номер которых кратен 100, — невисокосные;
#   3. остальные годы, номер которых кратен 4, — високосные.

n = int(input(f'Введите год: '))

if n % 4 != 0:
    print(f'{n} это обычный год')
elif n % 100 == 0:
    if n % 400 == 0:
        print(f'{n} это високосный год')
    else:
        print(f'{n} это обычный год')
else:
    print(f'{n} это високосный год')

# Сложность O(1)
