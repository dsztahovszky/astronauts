def main():
    with open('astronauts.csv') as astr_file:
        datas = astr_file.readlines()
    qualif_indexes = datas[0].split(',').index('Undergraduate Major') + 1,\
        datas[0].split(',').index('Graduate Major') + 1
    all_qualifications = []
    for astronaut in datas[1:]:
        astronaut = astronaut.split(',')
        qualifications = astronaut[qualif_indexes[0]], astronaut[qualif_indexes[1]]
        all_qualifications.append(qualifications)
    print(all_qualifications)


main()
