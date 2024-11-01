def Cloning(A): 
	A_copy = [i for i in A] 
	return A_copy 
A = [ 0, 9, 3, 5] 
B = Cloning(A) 
print("Original List:", A) 
print("After Cloning:", B) 