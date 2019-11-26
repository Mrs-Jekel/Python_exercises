
def FizzBuzz():
  for num in range(1, 101):
    if num % 3 ==0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)


def counter(max_value):         
  for num in range(1, max_value):
    print(num)

FizzBuzz()