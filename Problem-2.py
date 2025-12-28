a = int(input("Enter a: "))
series = list(range(1, 2 * a, 2))
print(*series, sep=", ")