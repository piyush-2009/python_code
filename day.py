rows = 5

# Upper pattern
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if i % 2 == 0:
            print("*", end=" ")
        else:
            print(j, end=" ")
    print()

print("------------------")

# Lower pattern
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
