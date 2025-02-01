#program that writes out the number from 1 to 100
#if the number is divisible by 3, write Fizz instead.
#if the number is divisible by 5, write Buzz instead.
#if the number is divisible by both 3 and 5, write FizzBuzz

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0: print(i, 'FizzBuzz')
    elif i % 3 == 0: print(i, 'Fizz')
    elif i % 5 == 0: print(i, 'Buzz')