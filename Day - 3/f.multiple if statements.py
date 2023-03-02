#Multiple if statements in Succession

print('Using Multiple if statements')

height = int(input('What is your height (in cm)?'))
bill =0

if height>120:
    age=int(input('Enter your age?'))
    if age<12:
        bill=5
        print('You pay $5.')
    elif age<18:
        bill=7
        print('You pay $7.')   
    else:
        bill=12
        print('You pay $12.')

    want_photos = input('Do you want to take photos? Y or N.')
    res = want_photos.lower()
    if res == 'y':
        bill += 3
        print(f'Your final Bill pay ${bill}')
    else:
        print(f'Your final Bill pay ${bill}')
else:
    print("You can't ride!")
