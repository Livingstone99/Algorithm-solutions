# 1) Given and array of Numbers such as [1,2,3,4,5] 
# 	return 'even' if the sum of the elements at the even indexes is greater than the sum of numbers at the odd indexes.
# 	return 'odd' if the sum of the elements at the odd indexes is greater than the sum of numbers at the even indexes.
# 	return 'equal' if they are equal

"""string[start:stop:step] uses three arguments start, stop, and step to 
carve out a subsequence. It accesses every step-th element between indices 
start (included) and stop (excluded). The double colon :: occurs if you drop the 
stop argument. In this case, Python will use the default value and doesn’t assume
 an artificial stop."""

def checkSum(arr: list) -> str:
    even = sum(arr[::2])
    odd = sum(arr[1::2])
    print(even, odd)
    if even > odd:
        return 'even'
    elif odd > even:
        return 'odd'
    else:
        return 'equal'
checkSum([1,2,3,4,1])