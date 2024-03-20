from collections import Counter as ct


#   task 1
def dif_count(nums):
    print(len(set(nums)))


#   task 2
def is_sub_set(set1, set2):
    print((set1 >= set2) or (set2 >= set1))


#   task 3
def game(count):
    cities = set()
    for x in range(count):
        city = input()
        if city not in cities:
            print("OK")
            cities.add(city)
        else:
            print("REPEAT")


#   task 4
def word_count(line):
    d = {word.strip() : 0 for word in line}
    for word in line:
        word = word.strip()
        print(d[word], end=' ')
        d[word] += 1
    print()


#   task 5
def purchases(count):
    consumers = {}
    for _ in range(count):
        id, product, amount = input("Введите покупателя, товар и количество товара через пробел:    ").split()
        if id not in consumers:
            consumers[id] = {product : int(amount)}
        elif product not in consumers[id]:
            consumers[id][product] = int(amount)
        else:
            consumers[id][product] += int(amount)
    for person in consumers:
        print(f'покупатель {person}:')
        for item in consumers[person]:
            print(item, ':', consumers[person][item], "штук")
        print("================")


#   task 6
def sort_words(line):
    d, line = {}, line.split()
    for word in set(line):
        c = line.count(word)
        if c not in d:
            d[c] = [word]
        else:
            d[c].append(word)
    for key in sorted(d.keys(), reverse=True):
        if len(d[key]) == 1:
            print(d[key][0], key)
        else:
            for word in sorted(d[key]):
                print(word, key)


dif_count(map(int, input("Введите значения списка через пробел и запятую:    ").split(", ")))
is_sub_set(set(input("Введите значения множества 1 через пробел и запятую:    ").split(", ")),
           set(input("Введите значения множества 2 через пробел и запятую:    ").split(", ")))
game(int(input("Введите число городов, названных в игре:    ")))
word_count(input("Введите строку:    ").split())
purchases(int(input("Число покупок:    ")))
sort_words(input("Введите строку:    "))

