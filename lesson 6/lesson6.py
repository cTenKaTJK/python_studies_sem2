from module import CsvFile


if __name__ == '__main__':
    table = CsvFile(filename='Titanic.csv')
    table.info()
    table.delNaN()
    table.info()
    table.show(output='random', separator='|', lines=3)
