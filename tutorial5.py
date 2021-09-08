l = [1,2,3,4,5]
print(l[1:3])
print(l[2:])

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

print("   a  b  c")

game[0][1] = 1

for count, row in enumerate(game):
    print(count, row)
