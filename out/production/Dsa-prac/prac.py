# write heapsort 
# we first generate a heap from the array so -> func heapify()
# then we sort the heap  -> func sortHeap()
"""
nums = [[1,3,5,4],
				[4,6,7,1],
				[0,2,8,1]]
n = len(nums[0])
# c = nums[0].length

print(n)
# print(c)

"""
# def call():
#     count = 0

#     def foo2():
#         count =+ 1
#         print(count)
#     for i in range(2):
#         foo2()
#     return(print(count))

# call()
#

ls = sorted('apb')
print(ls)

array = ['yo', 'wassup', 'lets go']
obj = enumerate(array)
print(type(next(obj)))
i=0
while (i<=2):
  print(next(obj))
  i+=1


# Implementing Kadane's Algorithm
nums = []

def maxSubArray(nums: List[int]) -> int:

	maxSum = 0
	current_sum = 0
	for x in nums:
		if (current_sum	< maxSum):
			current_sum	= current_sum + x
	return