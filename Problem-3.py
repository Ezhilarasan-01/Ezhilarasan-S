a = int(input("Enter a: "))
if a % 2 == 0:
    a = a - 1
series = []
for i in range(a):
    series.append(str(2 * i + 1))

print(", ".join(series))