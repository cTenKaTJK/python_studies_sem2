from collections import Counter as ct
from numpy import array as arr
from numpy.linalg import det


def num(s):
    return 47 < ord(s) < 58


#   task 1
def encode(in_str):
    out_str, count = in_str[0], 1
    for i in range(1, len(in_str)):
        if in_str[i] == in_str[i - 1]:
            count += 1
        else:
            if count > 1:
                out_str += str(count)
            out_str += in_str[i]
            count = 1
    if count > 1:
        out_str += str(count)
    print(out_str)
    return out_str


#   task 2
def decode(in_str):
    out_str, n, curr = in_str[0], "", ""
    for i in range(1, len(in_str)):
        if num(in_str[i]):
            if not n:
                curr = in_str[i - 1]
            n += in_str[i]
        else:
            if n:
                out_str += (curr * (int(n) - 1))
                n = ""
            out_str += in_str[i]
    if n:
        out_str += (out_str[-1] * (int(n) - 1))
    print(out_str)
    return out_str


#   task 3
def to_str(num):
    out = ""
    if not num:
        out = "ноль"
        print(out)
        return out
    digs1 = {1 : "один", 2 : "два", 3 : "три", 4 : "четыре", 5 : "пять",
            6 : "шесть", 7 : "семь", 8 : "восемь", 9 : "девять"}

    digs2 = {2 : "двадцать", 3 : "тридцать", 4 : "сорок", 5 : "пятьдесят",
            6 : "шестьдесят", 7 : "семьдесят", 8 : "восемьдесят", 9 : "девяносто"}

    digs3 = {1 : "сто", 2 : "двести", 3 : "триста", 4 : "четыреста", 5 : "пятьсот",
            6 : "шестьсот", 7 : "семьсот", 8 : "восемьсот", 9 : "девятьсот"}

    digs4 = {0 : "десять", 1 : "одиннадцать", 2 : "двенадцать", 3 : "тринадцать", 4 : "четырнадцать", 5 : "пятнадцать",
            6 : "шестнадцать", 7 : "семнадцать", 8 : "восемнадцать", 9 : "девятнадцать"}

    while num > 0:
        if num == 1000:
            out += "тысяча"
            break
        if num > 99:
            out += digs3[num // 100]
            num %= 100
        if num > 9:
            if num // 10 == 1:
                out += digs4[num % 10]
                break
            out += digs2[num // 10]
            num %= 10
        else:
            out += digs1[num]
            break
    print(out)
    return out


#   task 4
def repeating(items):
    print(*list(dict(ct(items))[i] for i in list(items[x] for x in range(len(items)) if items[x] not in items[:x])))


#   task 5
def is_linear(matr):
    return det(matr) == 0


#   task 6
def abb(s):
    return " ".join(map(lambda x: x[0].upper(), s.split()))


if __name__ == '__main__':
    decode(encode(input("Введите строку (с повторяющимися символами):    ")))
    to_str(int(input("Введите число (1-1000):    ")))
    repeating(input("Введите элементы через пробел:    ").split())
    print(is_linear(arr([list(map(int, input(f'Введите {i + 1} строку матрицы через пробел:    ').split())) for i in range(3)], dtype=int)))
    print(abb(input("Введите строку (на аббревиатуру):    ")))
