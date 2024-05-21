import csv, random, os


class CsvFile:

    def __init__(self, path, filename):
        self.path = path
        self.filename = filename
        with open(self.path + '/' + self.filename, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            self.data = [row for row in reader]
        self.head = self.data[0]
        self.data = self.data[1:]
        self.rows = len(self.data)
        self.cols = len(self.head)
        self.maxLen = [0] * self.cols

    def show(self, output='top', lines=5, separator=','):

        def prettyLineOutput():
            for s in [self.head] + out_data:
                self.maxLen = list(map(lambda x: max(self.maxLen[x[0]], len(x[1])), enumerate(s)))

            print('┌' + "".join(['─' * (x + 1) + '┬' for x in self.maxLen])[1:-1] + '┐')
            print('│' + " ".join([str(self.head[x]) + ' ' * (self.maxLen[x] - len(str(self.head[x])))
                                  + separator for x in range(self.cols)]))
            print('├' + "".join(['─' * (x + 1) + '┼' for x in self.maxLen])[1:-1] + '┤')

            for line in out_data:
                print('│' + " ".join([str(line[x]) + ' ' * (self.maxLen[x] - len(str(line[x]))) + separator
                                     for x in range(self.cols)]))

            print('└' + "".join(['─' * (x + 1) + '┴' for x in self.maxLen])[1:-1] + '┘')

        match output:
            case 'top':
                out_data = self.data[:lines]
                prettyLineOutput()

            case 'bottom':
                out_data = self.data[-lines:]
                prettyLineOutput()

            case 'random':
                r_nums = random.sample([row[0] for row in self.data], lines)
                out_data = [row for row in self.data if row[0] in r_nums]
                prettyLineOutput()

    def info(self):
        def get_type(line, types):
            for i, item in enumerate(line):
                item = item.strip().rstrip()
                if len(item) == 1 and ord(item) in (48, 49):
                    continue
                for sym in item:
                    if types[i] == 'bool' and 47 < ord(sym) < 58:
                        types[i] = 'int'
                    elif types[i] == 'int' and sym == '.':
                        print(item)
                        types[i] = 'float'
                    elif (ord(sym) < 48 or ord(sym) > 57) and sym != '.':
                        types[i] = 'str'
                        break
            return types

        non_null = [0] * self.cols
        types = ['bool'] * self.cols
        for row in self.data:
            non_null = [non_null[i] + int(item != '') for i, item in enumerate(row)]
            types = get_type(row, types)

        print('┌' + '─' * 32 + '┐')
        print(f'│Table Dimension:{"." * (15 - len(str(self.rows) + str(self.cols)))}{self.rows}x{self.cols}│')
        for x in range(self.cols):
            print(f'│{self.head[x]}: {"." * (18 - len(self.head[x]) - len(str(non_null[x])))}{non_null[x]} type: {types[x] + (" " * (5 - len(types[x])))}│')
        print('└' + '─' * 32 + '┘')

    def delNaN(self):
        self.data = list(filter(lambda x: all(list(map(lambda y: y != '', x))), self.data))
        self.rows = len(self.data)
        print('┌─────────────────────────────────────────────────────────┐')
        print('│ -> null values having rows are successfully deleted! <- │')
        print('└─────────────────────────────────────────────────────────┘')

    def makeDS(self):
        sep = int(self.rows * 0.7)
        nums = [row[0] for row in self.data]
        random.shuffle(nums)
        learning_items, testing_items = nums[:sep], nums[sep:]
        learning_data = [row for row in self.data if row[0] in learning_items]
        testing_data = [row for row in self.data if row[0] in testing_items]

        learning_path = self.path + '/workdata' + '/learning'
        testing_path = self.path + '/workdata' + '/testing'
        if not os.path.exists(self.path + '/workdata'): os.mkdir(self.path + '/workdata')
        if not os.path.exists(learning_path): os.mkdir(learning_path)
        if not os.path.exists(testing_path): os.mkdir(testing_path)

        with open(learning_path + '/train.csv', 'w', newline='') as file1:
            writer = csv.writer(file1)
            writer.writerow(self.head)
            [writer.writerow(row) for row in learning_data]

        with open(testing_path + '/test.csv', 'w', newline='') as file2:
            writer = csv.writer(file2)
            writer.writerow(self.head)
            [writer.writerow(row) for row in testing_data]

        if os.path.exists(learning_path + '/train.csv') and os.path.exists(testing_path + '/test.csv'):
            print('┌───────────────────────────────────────────┐')
            print('│ -> csv-files are successfully created! <- │')
            print('└───────────────────────────────────────────┘')
            return learning_path, 'train.csv', testing_path, 'test.csv'
