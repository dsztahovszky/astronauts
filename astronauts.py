import csv


def main():
    with open('astronauts.csv', newline='') as astr_file:
        datas_csvreader = csv.reader(astr_file)
        datas = [data for data in datas_csvreader]
    birthdate_index = datas[0].index('Birth Date')
    print(datas, birthdate_index, sep='\n')


main()
