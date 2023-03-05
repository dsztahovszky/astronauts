import csv


def main():
    with open('astronauts.csv', newline='') as astr_file:
        datas_csvreader = csv.reader(astr_file)
        datas = [data for data in datas_csvreader]
    birthdate_index = datas[0].index('Birth Date')
    birthdate_months = []
    for astronaut in datas[1:]:
        birthdate_months.append(astronaut[birthdate_index].split('/')[0])
    print(birthdate_months)


main()
