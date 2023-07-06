for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

num = int(input("Enter any integer number: "))
print('\n'.join('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or str(i) for i in range(1, num + 1)))

for i in range(1, int(input('Enter the number: ')) + 1):
    print(str(i) + ': ' + ('Fizz' if i % 3 == 0 else '') + ('Buzz' if i % 5 == 0 else ''))
