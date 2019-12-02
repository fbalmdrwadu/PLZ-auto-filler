from pandas import DataFrame, read_csv
from sys import argv
from numpy import select

PATH = read_csv('/home/dominik/Schreibtisch/nov_4.csv', encoding='ISO-8859-1', sep=';', header=None)
column_1 = int(argv[2])


def main():

    df = PATH.drop([0, 1, 2], axis=0).drop([2], axis=1).fillna(value=0)
    plz = df[column_1].astype('int64')
    inter = lambda l, v, u: ((l <= v) & (v <= u))

    e = ' €'
    conditions = [inter(5000, plz, 6999) | plz == 99,
                  inter(4000, plz, 4999) | inter(8000, plz, 9899),
                  inter(1000, plz, 7999)]
    choices = ['90'+e, '70'+e, '60'+e]

    df['Preis'] = select(conditions, choices)
    output = DataFrame({'PLZ': plz, 'Preis': df['Preis']})

    return output.to_csv('/home/dominik/Schreibtisch/output_.csv')


if __name__ == '__main__':
    main()