import csv


def main():
    with open('astronauts.csv', newline='') as astr_file:
        datas_csvreader = csv.reader(astr_file)
        datas = [data for data in datas_csvreader]
    birthdate_index = datas[0].index('Birth Date')
    birthdate_months = []
    for astronaut in datas[1:]:
        birthdate_months.append(int(astronaut[birthdate_index].split('/')[0]))
    months = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    for index in range(1, 13):
        months[index] = birthdate_months.count(index)
    print(months)


main()
