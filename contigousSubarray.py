"""Given an array of numbers 'n' and and integer 'k' return the number of contiguous 
subarrays of 'n' with number of unique elements (elements that have only one appearance) 
equal to or greater than 'k' 
		[5,5,5,5] and 2 should return 0		
		[1,2,1,1] and 2 should return 2"""


def contiguousSubarray(arr: list, k: int) -> int:
    count = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if len(set(arr[i:j+1])) >= k:
                count += 1
    return count

contiguousSubarray([1,2,1,1], 2)