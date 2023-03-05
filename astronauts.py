import csv


def main():
    with open('astronauts.csv', newline='') as astr_file:
        datas_csvreader = csv.reader(astr_file)
        datas = [data for data in datas_csvreader]
    birthdate_index = datas[0].index('Birth Date')
    birthdate_months = []
    for astronaut in datas[1:]:
        birthdate_months.append(int(astronaut[birthdate_index].split('/')[0]))
    months = []
    for index in range(1, 13):
        months.append(birthdate_months.count(index))
    all_months = months.copy()
    most_month_1 = [months.index(max(months)), round((max(months) / sum(all_months)) * 100, 1)]
    del months[most_month_1[0]]
    if most_month_1[0] <= months.index(max(months)):
        most_month_2 = [months.index(max(months)) + 1, round((max(months) / sum(all_months)) * 100, 1)]
    else:
        most_month_2 = [months.index(max(months)), round((max(months) / sum(all_months)) * 100, 1)]
    del months[most_month_2[0]]
    if most_month_1[0] <= months.index(max(months)):
        if most_month_2[0] <= months.index(max(months)):
            most_month_3 = [months.index(max(months)) + 2, round((max(months) / sum(all_months)) * 100, 1)]
        else:
            most_month_3 = [months.index(max(months)) + 1, round((max(months) / sum(all_months)) * 100, 1)]
    elif most_month_2[0] <= months.index(max(months)):
        if most_month_1[0] > months.index(max(months)):
            most_month_3 = [months.index(max(months)) + 1, round((max(months) / sum(all_months)) * 100, 1)]
    else:
        most_month_3 = [months.index(max(months)), round((max(months) / sum(all_months)) * 100, 1)]
    months_words = {0: 'Január',
                    1: 'Február',
                    2: 'Március',
                    3: 'Április',
                    4: 'Május',
                    5: 'Június',
                    6: 'Július',
                    7: 'Augusztus',
                    8: 'Szeptember',
                    9: 'Október',
                    10: 'November',
                    11: 'December'}
    most_months = [most_month_1, most_month_2, most_month_3]
    for month in most_months:
        month[0] = months_words[month[0]]
    print('A három leggyakoribb születési hónap a NASA űrhajósai körében százalékos aránnyal kiegészítve:', end='\n')


main()
