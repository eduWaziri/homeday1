def fizz_buzz(num):
    # divisible by only 3
    if (num%3 == 0) and (num%5 != 0):
        return 'Fizz'

    # divisible by only 5
    elif (num%3 != 0) and (num%5 == 0):
        return 'Buzz'

    # divisible by both 3 and 5
    elif (num%3 == 0) and (num%5 == 0):
        return 'FizzBuzz'

    # divisible by neither 3 nor 5
    elif (num%3 != 0) and (num%5 != 0):
        return num

n = 101
print fizz_buzz(n)