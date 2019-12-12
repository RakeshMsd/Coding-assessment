def countX(lst, x): 
	count = 0
	for ele in lst: 
		if (ele == x): 
			count = count + 1
	return count 
lst = [7, 5, 6, 1, 9, 10, 6, 88, 6] 
x = 6
print('{} has occurred {} times'.format(x, countX(lst, x))) 
