# Array Subset of another array

# Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m. Task is to check whether a2[] is a subset of a1[] or not. Both the arrays can be sorted or unsorted. It may be assumed that elements in both array are distinct.

array = [ 11, 1, 13, 21, 3, 7 ]
check_subset = [ 11, 3, 7, 1 ]
check = True

for index in range ( 0 , len ( check_subset ) ) :
    temp = check_subset [ index ] 
    
    if temp not in array : check = False

print ( check )
