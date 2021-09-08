game_size = 3
print("   0  1  2")
'''
s = "   "
for i in range(game_size):
	s += str(i) + "  "

s = " "
for i in range(game_size):
	s += "  " + str(i)
'''
s = "   "+"  ".join([str(i) for i in range(game_size)])

print(s)


