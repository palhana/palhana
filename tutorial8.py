'''game = "I want to play a game"
print(id(game))

def game_board(player=0, row=0, column=0, just_display=False):
    global game
    game = "A game"
    print(id(game))
    print(game)

game_board()
print(game)
print(id(game))
'''

'''x=1		#tuple is immutable, 노!
def test():
	x=2
test()
print(x)

x=1
def test():
	global x
	x=2
test()
print(x)

x=[1,2,3]	#list 라서 바꾸는게 예스~
def test():
	x[1]=0
test()
print(x)

x=[1]		#list의 값은 index를 이용해 바꾸어야 해요, 노!
def test():
	x=[2]
test()
print(x)
	
x=[1]
def test():
	global x
	x=[2]
test()
print(x)

x=[1]		#index를 썼으니 list에서 작동, 예스~
def test():
	x[0]=2
test()
print(x)
'''


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    if not just_display:
        game_map[row][column] = player
    for count, row in enumerate(game_map):
        print(count, row)
    return game_map

game = game_board(game, just_display=True)
game = game_board(game, player=1, row=2, column=-1)
