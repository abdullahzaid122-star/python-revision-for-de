squares = []
for num in range(0, 21, 2):
    squares.append(num ** 2)
sliced = squares[3:8]
sliced.sort(reverse=True)
print(sliced)