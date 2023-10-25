
print('Welcome to Burger Shop!');
size = input('What size Burger you want? M, N,or L: ');
add_mushroom = input('Do you want mushroom? Y/N: ');
add_cheese = input('Do you want cheese? Y/N: ');

bill = 0;
if size == 'M':
    bill +=5
elif size == 'N':
    bill +=8
else:
    bill +=10;

if add_mushroom == 'Y':
    if size == 'L':
        bill +=2;
    else:
        bill +=1;

print(f"Your bill is: {bill}");
