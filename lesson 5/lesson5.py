import json, csv, functools


#   task 1
def multiplication():
    in_f = open('./src/1/input.txt', 'r')
    out_f = open('./src/1/output.txt', 'w')

    out_f.write(str(functools.reduce(lambda a, b: a * b, list(map(int, str(in_f.read()).split())))))

    in_f.close()
    out_f.close()
    print('task1..........ready')


#   task 2
def sort_file():
    in_f = open('./src/2/input.txt', 'r')
    out_f = open('./src/2/output.txt', 'w')

    nums = list(map(int, str(in_f.read()).split('\n')))
    nums.sort(key=lambda x: str(x))
    [out_f.write(str(x) + '\n') for x in nums]

    in_f.close()
    out_f.close()
    print('task2..........ready')


#   task 3
def kindergarten():
    with open('./src/3/input.txt', 'r', encoding='utf-8') as file:
        children = [tuple(x.split()) for x in str(file.read()).split('\n')]

    oldest = open('./src/3/max.txt', 'w', encoding='utf-8')
    youngest = open('./src/3/min.txt', 'w', encoding='utf-8')

    oldest.write(" ".join(max(children, key=lambda x: int(x[2]))))
    youngest.write(" ".join(min(children, key=lambda x: int(x[2]))))

    oldest.close()
    youngest.close()
    print('task3..........ready')


#   task 4
def json_to_csv(jason_name):
    with open(jason_name, 'r') as json_file:
        data = json.load(json_file)
    with open(f'./src/4/{list(data.keys())[0]}.csv', 'w') as csv_file:
        data = list(data.values())[0]
        writer = csv.DictWriter(csv_file, fieldnames=list(data[0].keys()))
        writer.writeheader()
        for item in data:
            writer.writerow(item)
    print('task4..........ready')


if __name__ == '__main__':
    multiplication()
    sort_file()
    kindergarten()
    json_to_csv(input())   # ./src/4/example.json for example
