import csv


def get_datas():
    with open('astronauts.csv', newline='') as astr_file:
        datas_csvreader = csv.reader(astr_file)
        return [data for data in datas_csvreader]


def get_birth_months():
    datas = get_datas()
    birthdate_index = datas[0].index('Birth Date')
    birth_months = []
    for astronaut in datas[1:]:
        birth_months.append(int(astronaut[birthdate_index].split('/')[0]))
    return birth_months


def make_months_list(birth_months):
    months = []
    for index in range(1, 13):
        months.append(birth_months.count(index))
    return months


def make_most_monts_datas(months):
    all_months = months.copy()
    most_months = []
    most_months.insert(0, [months.index(max(months)), round((max(months) / sum(all_months)) * 100, 1)])
    del months[most_months[0][0]]
    if most_months[0][0] <= months.index(max(months)):
        most_months.insert(1, [months.index(max(months)) + 1, round((max(months) / sum(all_months)) * 100, 1)])
    else:
        most_months.insert(1, [months.index(max(months)), round((max(months) / sum(all_months)) * 100, 1)])
    del months[most_months[1][0]]
    if most_months[0][0] <= months.index(max(months)):
        if most_months[1][0] <= months.index(max(months)):
            most_months.insert(2, [months.index(max(months)) + 2, round((max(months) / sum(all_months)) * 100, 1)])
        else:
            most_months.insert(2, [months.index(max(months)) + 1, round((max(months) / sum(all_months)) * 100, 1)])
    elif most_months[1][0] <= months.index(max(months)):
        if most_months[0][0] > months.index(max(months)):
            most_months.insert(2, [months.index(max(months)) + 1, round((max(months) / sum(all_months)) * 100, 1)])
    else:
        most_months.insert(2, [months.index(max(months)), round((max(months) / sum(all_months)) * 100, 1)])
    return most_months


def pair_months_words(most_months):
    for month in most_months:
        month[0] += 1
    return most_months


def print_datas(datas):
    print('A három leggyakoribb születési hónap a NASA űrhajósai körében százalékos arányokkal kiegészítve:',
          end='\n\n')
    print(datas[0][0], '.; ', datas[0][1], '%', sep='')
    print(datas[1][0], '.; ', datas[1][1], '%', sep='')
    print(datas[2][0], '.; ', datas[2][1], '%', sep='')


def main():
    birth_months = get_birth_months()
    months = make_months_list(birth_months)
    most_months = make_most_monts_datas(months)
    pair_months_words(most_months)
    print_datas(most_months)


main()
