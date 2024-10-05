def check_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is even")
            return num * 2
        else:
            print(f"{num} is odd")
            return num * 3
            
result = check_numbers([1, 2, 3, 4])
print(result)

def find_number(numbers):
    for i in numbers:
        if i == 5:
            return i * 2
        else:
            print(i)
            return i + 3
