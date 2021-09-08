game = [[1, 1, 1],
        [0, 2, 0],
        [2, 2, 0],]

'''
def win(current_game):
    for row in game:
        print(row)
        col1 = row[0]
        col2 = row[1]
        col3 = row[2]
        if col1 == col2 == col3:
            print("Winner!")
'''
'''
def win(current_game):
    for row in game:
        print(row)
        all_match = True
        for item in row:
            if item != row[0]:
                all_match = False
        if all_match:
            print("winner!!!")
'''

def win(current_game):
    for row in game:
        if row.count(row[0]) == len(row) and row[0] !=0:
            print("Winner!")

win(game)
