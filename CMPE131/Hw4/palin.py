def palindrome(lst):
	if len(lst) <=1:
		return True
	else:
		for i in range(len(lst)//2):
			if lst[i] !=lst[-i-1]:
				return False
			return True
