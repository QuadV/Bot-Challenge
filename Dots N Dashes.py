import copy
single_side = [0, 1, 2, 4, 8]
two_sides = [3, 5, 6, 9, 10, 12]
three_sides = [7, 11, 13, 14]

def check_top(i):
	if (i == 0):
		return False
	else:
		return True

def check_right(j):
	if (j == 4):
		return False
	else:
		return True

def check_bottom(i):
	if (i == 4):
		return False
	else:
		return True

def check_left(j):
	if (j == 0):
		return False
	else:
		return True

def get_sides(i,j):
	if (elements[i][j] == 3):
		return (2,3)
	elif (elements[i][j] == 5):
		return (1,3)
	elif (elements[i][j] == 9):
		return (1,2)
	elif (elements[i][j] == 6):
		return (0,3)
	elif (elements[i][j] == 10):
		return (0,2)
	elif (elements[i][j] == 12):
		return (0,1)

def check_for_more_three_sides(virtual_elements, count):
	flag = False
	for i in range(0,5):
		for j in range(0,5):
			if(virtual_elements[i][j] in three_sides):
				if(virtual_elements[i][j] == 7):
					virtual_elements[i][j] += 2**3
					if(j != 0):
						virtual_elements[i][j-1] += 2**1
					count += 1
					flag = True
					break
				elif (virtual_elements[i][j] == 11):
					virtual_elements[i][j] += 2**2
					if(i != 4):
						virtual_elements[i+1][j] += 2**0
					count += 1
					flag = True
					break
				elif (virtual_elements[i][j] == 13):
					virtual_elements[i][j] += 2**1
					if(j != 4):
						virtual_elements[i][j+1] += 2**3
					count += 1
					flag = True
					break
				elif (virtual_elements[i][j] == 14):
					virtual_elements[i][j] += 2**0
					if(i != 0):
						virtual_elements[i-1][j] += 2**2
					count += 1
					flag = True
					break
		if(flag is True):
			break
	if(flag is True):
		check_for_more_three_sides(virtual_elements, count)
	return count

def add_for_box_side (i,j,side,virtual_elements):
	if(side == 0 and i >0):
		virtual_elements[i-1][j] += 2**2
	elif(side == 1 and j <4):
		virtual_elements[i][j+1] += 2**3
	elif(side == 2 and i < 4):
		virtual_elements[i+1][j] += 2**0
	elif(side == 3 and j >0):
		virtual_elements[i][j-1] += 2**1
	return virtual_elements
		
def check_for_squares_filled(i,j,side,virtual_elements,count):
	virtual_elements[i][j] += (2**side)
	virtual_elements = add_for_box_side(i,j,side,virtual_elements)
	if(virtual_elements[i][j] == 7):
		virtual_elements[i][j] += (2**3)
		if(j > 0):
			count += 1
			check_for_squares_filled(i,j-1,1,virtual_elements,count)
	elif (virtual_elements[i][j] == 11):
		virtual_elements[i][j] += (2**2)
		if(i < 4):
			count += 1
			check_for_squares_filled(i+1,j,0,virtual_elements,count)
	elif (virtual_elements[i][j] == 13):
		virtual_elements[i][j] += (2**1)
		if(j < 4):
			count += 1
			check_for_squares_filled(i,j+1,3,virtual_elements,count)
	elif (virtual_elements[i][j] == 14):
		virtual_elements[i][j] += (2**0)
		if(i > 0):
			count += 1
			check_for_squares_filled(i-1,j,2,virtual_elements,count)
	return check_for_more_three_sides(virtual_elements, count)

def check_count_squares_filled():
	mini = 20
	for i in range(0,5):
		for j in range(0,5):
			print ("Count Entered")
			print(str(elements[i][j]) + ": " + str(i) + " " + str(j))
			if (elements[i][j] in two_sides):
				side1, side2 = get_sides(i,j)
				#print ("After get_sides")
				virtual_elements = copy.deepcopy(elements)
				count = check_for_squares_filled(i, j, side1, virtual_elements, 0)
				if (count < mini):
					mini = count
					side = side1
					k = i
					l = j
				virtual_elements = copy.deepcopy(elements)
				count = check_for_squares_filled(i, j, side2, virtual_elements, 0)
				if (count < mini):
					mini = count
					side = side2
					k = i
					l = j
	return (k, l, side)

def check_top_line(i,j):
	if(not check_top(i)):
		return True
	elif(elements[i-1][j] in single_side):
		return True
	return False

def check_right_line(i,j):
	if (check_right(j)):
		#print("Reached here: right")
		if(elements[i][j+1] in single_side):
			return True
	elif (not check_right(j)):
		return True
	return False

def check_bottom_line(i,j):
	if (check_bottom(i)):
		#print("Reached here: bottom")
		if(elements[i+1][j] in single_side):
			return True
	elif (not check_bottom(i)):
		return True
	return False
	
def check_left_line(i,j):
	if (check_left(j)):
		#print("Reached here: left")
		if(elements[i][j-1] in single_side):
			return True
	elif (not check_left(j)):
		return True
	return False
		
def check_for_0(i,j):
	if(check_top_line(i,j)):
		print ("here 0-top")
		return 0
	elif (check_right_line(i,j)):
		print ("here 0-right")
		return 1
	elif (check_bottom_line(i,j)):
		print ("here 0-bottom")
		return 2
	elif (check_left_line(i,j)):
		print ("here 0-left")
		return 3
	return 5

def check_for_1(i,j):
	if (check_right_line(i,j)):
		return 1
	elif (check_bottom_line(i,j)):
		return 2
	elif (check_left_line(i,j)):
		return 3
	return 5

def check_for_2(i,j):
	if(check_top_line(i,j)):
		return 0
	if (check_bottom_line(i,j)):
		return 2
	elif (check_left_line(i,j)):
		return 3
	return 5

def check_for_4(i,j):
	if(check_top_line(i,j)):
		return 0
	elif (check_right_line(i,j)):
		return 1
	if (check_left_line(i,j)):
		return 3
	return 5

def check_for_8(i,j):
	if(check_top_line(i,j)):
		return 0
	elif (check_right_line(i,j)):
		return 1
	elif (check_bottom_line(i,j)):
		return 2
	return 5
	
def check_single_side(i,j):
	if elements[i][j] in single_side:
		if(elements[i][j] == 0):
			key = check_for_0(i,j)
			if(key != 5):
				return key
		elif(elements[i][j] == 1):
			key = check_for_1(i,j)
			if(key != 5):
				return key
		elif(elements[i][j] == 2):
			key = check_for_2(i,j)
			if(key != 5):
				return key
		elif(elements[i][j] == 4):
			key = check_for_4(i,j)
			if(key != 5):
				return key
		elif(elements[i][j] == 8):
			key = check_for_8(i,j)
			if(key != 5):
				return key
	return 5

def check_for_single_side():
	for i in range(0,5):
		for j in range(0,5):
			print("check_for_single_side: " + str(elements[i][j]) + ": " + str(i) + " " + str(j))
			t = check_single_side(i,j)
			print ("t: " + str(t))
			if(t != 5):
				return (i,j,t)
	return check_count_squares_filled()

def check_boxes_filled(i,j,side):
	virtual_elements = copy.deepcopy(elements)
	count = check_for_squares_filled(i, j, side, virtual_elements, 0)
	count += check_for_more_three_sides(virtual_elements,count)
	return count

def get_side(i,j,virtual_elements):
	return (i,j,str('{0:04b}'.format(virtual_elements[i][j])[::-1]).index("0"))

def get_closing_side(i,j)
	k,l,side = get_side(i,j)
	virtual_elements = copy.deepcopy(elements)
	virtual_elements[i][j] += 2**side
	virtual_elements = add_for_box_side (i,j,side,virtual_elements)
	if(side == 0):
		if(i > 0):
			return get_side(i-1,j,virtual_elements)
	elif (side==1):
		if(j < 4):
			return get_side(i,j+1,virtual_elements)
	elif(side==2):
		if(i < 4):
			return get_side(i+1,j,virtual_elements)
	elif(side==3):
		if(j > 0):
			return get_side(i,j-1,virtual_elements)

def check_three_sides():
	for i in range(0,5):
		for j in range(0,5):
			#print(str(elements[i][j]) + ": " + str(i) + " " + str(j))
			if(elements[i][j] in three_sides):
				return (i,j,str('{0:04b}'.format(elements[i][j])[::-1]).index("0"))
	return check_for_single_side()

elements = [[],[],[],[],[]]
for i in range(0, 5):
	list1 = input().split(" ")
	elements[i] = [int(x) for x in list1]
	#elements[i].append(list2)

player = int(input())

#elements = [[15,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
#elements = [[15,0,0,0,0],[0,0,0,0,11],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

#print(elements)
i,j,side = check_three_sides()
print(str(i) , " " , str(j) , " " , str(side))
		
