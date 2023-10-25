
print('Welcome to Mortage Calculator');
salary = int(input('Enter your salary'));
rate = 0;

if salary >=2000:
    print('Enter your eligible for mortage')
    credit_score = int(input('Enter your credit score'))
    if credit_score >800:
        rate = 4;
        print(f'rate of interest:{rate}%');
    elif credit_score > 750:
        rate = 6;
        print(f'rate of interest:{rate}%');
    else:
        rate = 8;
        print(f'rate of interest:{rate}%')
    disability = input('Do you have disability? Y or N');
    if disability == 'Y':
        rate = 2;
        print(f'Final interest rate: {rate}')
else:
    print('You are not eligible');

