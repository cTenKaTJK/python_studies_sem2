import csv, random


class CsvFile:

    def __init__(self, filename):
        self.name = filename
        with open(self.name) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            self.data = [row for row in reader]
        self.rows = len(self.data) - 1
        self.cols = len(self.data[0])
        self.maxLen = [0] * self.cols

    def show(self, output='top', lines=5, separator=','):

        def prettyLineOutput(arr):
            for s in out_data:
                self.maxLen = list(map(lambda x: max(self.maxLen[x[0]], len(x[1])), enumerate(s)))
            print(" ".join([str(arr[x]) + ' ' * (self.maxLen[x] - len(str(arr[x]))) + separator for x in range(self.cols)]))

        match output:
            case 'top':
                out_data = self.data[:lines + 1]
                [prettyLineOutput(row) for row in out_data]

            case 'bottom':
                out_data = [self.data[0]] + self.data[-lines:]
                [prettyLineOutput(row) for row in out_data]

            case 'random':
                r_nums = ['PassengerId']
                r_nums.extend(random.sample([row[0] for row in self.data], 5))
                out_data = [row for row in self.data if row[0] in r_nums]
                [prettyLineOutput(line) for line in out_data]

    def info(self):
        print(f'Table Dimension:    {self.rows}x{self.cols}\n')
        non_null = [0] * self.cols
        for row in self.data[1:]:
            non_null = [non_null[i] + int(item != '') for i, item in enumerate(row)]
        for x in range(self.cols):
            print(f'{self.data[0][x]}:\t{non_null[x]}')
        print('--------------------------------')

    def delNaN(self):
        for line in self.data:
            if not all(list(map(lambda x: x != '', line))):
                self.data.remove(line)
                self.rows -= 1

    def makeDS(self):
        pass
