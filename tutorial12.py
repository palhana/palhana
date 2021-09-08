game = [[1, 0, 2],
        [1, 1, 0],
        [2, 2, 1],]

cols = list(reversed(range(len(game))))
rows = range(len(game))

for idx in rows:
    print(idx, cols[idx])

for col, row, in zip(cols, rows):
    print(row, col)

for col, row in enumerate(reversed(range(len(game)))):
    print(col, row)


'''
diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])

diags = []
for col, row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])

print(diags)
'''

'''
if game[0][0] == game[1][1] == game[2][2]:
    print("Winner")
if game[2][0] == game[1][1] == game[0][2]:
    print("Winner")
'''

