import numpy as np
from scipy.linalg import cholesky, solve_triangular
from scipy.stats import multivariate_normal as mn
import time


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
    print('standard deviation:\t', np.std(matrix))
    print('first 5 rows:\n', matrix[:5, :], '\n')


def task4(vector):
    print('┌─────────┐')
    print('│ TASK №4 │')
    print('└─────────┘')
    zeroes = np.where(vector == 0)[0]
    if vector.size == zeroes[-1] + 1:
        zeroes = zeroes[:-1]
    print('max value after 0:\t', np.max(vector[zeroes + 1]), '\n')


def task5(matrix, cov_matrix, m):
    print('┌─────────┐')
    print('│ TASK №5 │')
    print('└─────────┘')
    n, d = matrix.shape
    diff = matrix - m

    start1_time = time.time()

    ch = cholesky(cov_matrix, lower=True)
    inv = solve_triangular(ch, np.eye(d), lower=True)
    invars = inv.T @ inv
    log_calculated = 0.5 * (np.sum(diff @ invars * diff, axis=1) + (-2 * np.sum(np.log(np.diag(ch)))) + d * np.log(2 * np.pi))

    fin1_time = time.time()


    print(f'log calculation time:\t{fin1_time - start1_time}')

    scipy_calculated = mn(m, cov_matrix).logpdf(matrix)

    fin2_time = time.time()

    print(f'scipy calculation time:\t{fin2_time - fin1_time}')
    print(f'max accuracy difference:\t{np.max(np.abs(log_calculated - scipy_calculated))}')


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
    task5(np.random.randn(1000, 2), np.array([[1, 0.5], [0.5, 2]]), np.array([0, 0]))
    task6()
    task7()
    task8()
    input('\n...press enter to escape...')
