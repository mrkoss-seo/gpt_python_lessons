#task 1
first = int(input('Enter a number:'))
second = int(input('Enter a number:'))
result = round(first/second, 2)

#task 2
first = int(input('Enter a number:'))
second = int(input('Enter a number:'))
third = input('Enter a number:')
if first < second and first < third:
    print(first)

if second < first and second < third:
    print(second)

if third < first and third < second:
    print(third)

# task 3
first = int(input('Enter a number:'))
second = int(input('Enter a number:'))
summary = first + second
residual = first - second
multiple = first * second
quotient = first / second
print(summary, residual, multiple, quotient)

# task 4
first = int(input('Длинна первого катета:'))
second = int(input('Длинна второго катета:'))
square = (first*second)/2
hypotenuse = (first**2 + second**2)**0.5
print(square, hypotenuse)

# task 5
number = input('value pls')
print(number[-1])

#end
