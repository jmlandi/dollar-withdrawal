print('''\033[37mThis program considers $1, $2, $5, $10, $20, $50, and $100 bills.
Enter an integer number for the withdrawal.\033[m''')
while True:
    print(f'\033[40m{"  Withdraw  ":~^40}\033[m')
    value = str(input('Type a value: $'))
    while value.isnumeric() is False:
        print('\033[31mSorry, invalid value. Enter an integer number.\033[m')
        value = str(input('Type a value: $'))
    v = int(value)
    ced = 100
    while True:
        if v >= ced:
            tot_ced = v // ced
            v -= tot_ced * ced
            print(f'{tot_ced} bill(s) of ${ced}.')
        else:
            if ced == 100:
                ced = 50
            elif ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 5
            elif ced == 5:
                ced = 2
            elif ced == 2:
                ced = 1
            else:
                break
    w = str(input('Do you want a new withdraw [Y/N]? ')).strip().upper()[0]
    while w not in 'YN':
        print('\033[31mWe could not understand your answer. Please, try again.\033[m')
        w = str(input('Do you want a new withdraw [Y/N]? ')).strip().upper()[0]
    if w == 'N':
        print('\033[1;37mThank you for using our services. Kind regards.\033[m')
        break
    print()
