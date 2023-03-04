#FizzBuzz interview question - IMP***
#program that automatically prints the solution to the FizzBuzz game.

#conditions --> 3-fizz,4-buzz and 3&5- fizzbuzz

for num in range(1,101):
    if (num%3==0) and (num%5==0):
        print('FizzBuzz')
    elif num %3==0:
        print('Fizz')
    elif num%5==0:
        print('Buzz')
    else:
        print(num)
    


