def move_disk(first, last, tower):
    item = tower[first].pop()
    print(f'Переміщуємо диск {item} from {first} to {last}')
    tower[last].append(item)
    print(f'Проміжний стан: {tower}')

def move_tower(n, first, last, help, tower):
    if n == 1:
        move_disk(first, last, tower)
    else:
        move_tower(n-1, first, help, last, tower)
        move_disk(first, last, tower)
        move_tower(n-1, help, last, first, tower)

if __name__ == '__main__':
    n = 0
    while n <= 0:
        value = input('Введіть число дисків вежі:\n')
        if value.isnumeric():
            n = int(value)
        else:
            print('Некоректне значення кількості дисків (має бути додатнє число)')
    start_state = list(range(n, 0, -1))
    tower = {'A': start_state, 'B':[], 'C': []}
    print(f'Початковий стан: {tower}')
    move_tower(n, 'A', 'C', 'B', tower)
    print(f'Кінцевий стан: {tower}')
