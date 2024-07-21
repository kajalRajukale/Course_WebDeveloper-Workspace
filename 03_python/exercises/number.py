y = int(input("Enter the numer"))
x = 3
for i in range(1, y + 1):
    result = x * i
    print(f"{x} * {i} = {result}")
else:
    if y > 20:
        print("the number of rows has been limited to 20.")