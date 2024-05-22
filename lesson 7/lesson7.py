import numpy as np


def task1():
    print('┌─────────┐')
    print('│ TASK №1 │')
    print('└─────────┘')
    arr = np.loadtxt('./src/1/input.txt', delimiter=',')
    print(f'sum:\t{arr.sum()}\nmax:\t{arr.max()}\nmin:\t{arr.min()}\n')


def task2(inp):
    print('┌─────────┐')
    print('│ TASK №2 │')
    print('└─────────┘')
    arr = np.array(list(map(int, inp.split())))
    nums, reps = np.zeros(arr.size), np.zeros(arr.size)
    curr = arr[0]
    count, length = 1, 0
    for i in range(1, arr.size):
        if arr[i] == curr:
            count += 1
        else:
            nums[length] = curr
            reps[length] = count
            curr = arr[i]
            count = 1
            length += 1
    if True:
        nums[length] = curr
        reps[length] = count
    print(*nums[:length + 1])
    print(*reps[:length + 1], '\n')
    return nums[:length], reps[:length]


def task3():
    print('┌─────────┐')
    print('│ TASK №3 │')
    print('└─────────┘')
    matrix = np.random.randn(10, 4)
    print('min:\t', np.min(matrix))
    print('max:\t', np.max(matrix))
    print('mean value:\t', np.mean(matrix))
    print('standart deviation:\t', np.std(matrix))
    print('first 5 rows:\n', matrix[:5, :], '\n')


def task4(vector):
    print('┌─────────┐')
    print('│ TASK №4 │')
    print('└─────────┘')
    zeroes = np.where(vector == 0)[0]
    if vector.size == zeroes[-1] + 1:
        zeroes = zeroes[:-1]
    print('max value after 0:\t', np.max(vector[zeroes + 1]), '\n')


'''
точка X
размер R x C
мат.ожидание M
вектор длины D
матрица ковариаций C
размер C x C
'''


def task5(matrix, m, cov_matrix):
    pass


def task6():
    print('┌─────────┐')
    print('│ TASK №6 │')
    print('└─────────┘')
    arr = np.arange(16).reshape(4, 4)
    print(arr, '\n')
    arr[[1, 3]] = arr[[3, 1]]
    print(arr, '\n')


def task7():
    print('┌─────────┐')
    print('│ TASK №7 │')
    print('└─────────┘')
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris = np.genfromtxt(url, delimiter=',', dtype='object')
    species = iris[:, -1]
    uniq, count = np.unique(species, return_counts=True)
    print(*[f'{uniq[i]} — {count[i]}; ' for i in range(uniq.size)], '\n')


def task8():
    print('┌─────────┐')
    print('│ TASK №8 │')
    print('└─────────┘')
    arr = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])
    print(*np.nonzero(arr)[0])


if __name__ == '__main__':
    task1()
    task2('2 2 2 3 3 3 5 4 4')
    task3()
    task4(np.array([6, 2, 0, 3, 0, 0, 5, 7, 0]))
    # task5()
    task6()
    task7()
    task8()
    input('\n...press enter to escape...')


