x= input("Enter numbers separated by spaces or commas: ")
clean_data = x.replace(',', ' ').split()
numbers = [int(x) for x in clean_data]

divisors = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = {}

for d in divisors:
    count = 0
    for n in numbers:
        if n % d == 0:
            count += 1
    output[d] = count

print(output)