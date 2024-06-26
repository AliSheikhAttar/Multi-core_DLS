##COMPILER_PARAM:::output_type:::console
bombs = [[False for y in range(80)] for x in range(5)]
hint = True
hints = [[0 for _ in range(80)] for __ in range(5)]

def hint_func(x, y):
	if 5 > x - 1 >= 0 and 80 > y - 1 >= 0:
		hints[x - 1][y - 1] += 1
	if 5 > x - 1 >= 0 and 80 > y >= 0:
		hints[x - 1][y] += 1
	if 5 > x - 1 >= 0 and 80 > y + 1>= 0:
		hints[x - 1][y + 1] += 1
	if 5 > x >= 0 and 80 > y + 1 >= 0:
		hints[x][y + 1] += 1
	if 5 > x + 1 >= 0 and 80 > y + 1 >= 0:
		hints[x + 1][y + 1] += 1
	if 5 > x + 1 >= 0 and 80 > y >= 0:
		hints[x + 1][y] += 1
	if 5 > x + 1 >= 0 and 80 > y - 1 >= 0:
		hints[x + 1][y - 1] += 1
	if 5 > x >= 0 and 80 > y - 1 >= 0:
		hints[x][y - 1] += 1


bombs[0][1] = True
hint_func(0, 1)

bombs[0][0] = True
hint_func(0, 0)

bombs[0][79] = True
hint_func(0, 79)

bombs[4][79] = True
hint_func(4, 79)

bombs[4][0] = True
hint_func(4, 0)

bombs[2][36] = True
hint_func(2, 36)

bombs[3][66] = True
hint_func(3, 66)

bombs[3][68] = True
hint_func(3, 68)

bombs[4][65] = True
hint_func(4, 65)

bombs[4][66] = True
hint_func(4, 66)


for i in range(5):
	for j in range(80):
		if bombs[i][j]:
			print('*', end ='')
		elif hint and hints[i][j] > 0:
			print(hints[i][j], end ='')
		else:
			print('#', end ='')
	print()