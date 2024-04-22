from module import CsvFile
import sys, os


if __name__ == '__main__':
    path = os.path.dirname(sys.argv[0]).replace('\\', '/')

    table = CsvFile(path=path, filename='Titanic.csv')
    table.info()
    table.delNaN()
    table.info()
    table.show(output='random', separator='│', lines=3)

    path1, name1, path2, name2 = table.makeDS()

    train = CsvFile(path=path1, filename=name1)
    train.info()
    train.show(separator='│')

    test = CsvFile(path=path2, filename=name2)
    test.info()
    test.show(separator='│')
