game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]


def game_board(player=0, row=0, column=0, just_display=False):
    print("   0  1  2")
    if not just_display:
        game[row][column] = player		# put a value on the entry
    for count, row in enumerate(game):	# just do print the board
        print(count, row)

game_board(just_display=True)
game_board(player=1, row=0, column=1)
