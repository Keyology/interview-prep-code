# Given an unsorted array of integers, 
# print all pairs with given difference k

 
# Input: arr = [1,5,2,2,2,5,5,4], k=3
# Output: (2,5) and (1,4)

"""Time Complexity is O(n^2)"""
def findDifferencePairs(arr, k):
    # instantiate a  list
    solution_set = set()
    # iterate through the array with element i
    for i in range(0, len(arr)-1):
        # iterate through the array with element i2
        for i2 in range(i+1, len(arr)):
            # check if the difference == k
            if abs(arr[i2]-arr[i]) == k:
                # check if pair is already in solutions
                if not arr[i] in solution_set and not arr[i2] in solution_set:
                    # if not add to solutions
                    solution_set.add(arr[i])
                    solution_set.add(arr[i2])
                    print(arr[i], arr[i2])
    # return
    return 


"""Time complexity is O(n) """
def findDifferencePairs_sort(arr, k):
    # put all numbers into a set
    arr = set(arr)
    print(f"arr: {arr}")
    picker = set()
    for i in arr: # O(n)
        # check if i is already in picker
        if i+3 in picker:
            # if it is, then print solution
            print(i+3, i)
        if i-3 in picker:
            # if it is, then print solution
            print(i-3, i)
        # add i to the set
        picker.add(i)
    return

# TEST

arr = [1,5,2,2,2,5,5,4,-2,8]
k = 3

findDifferencePairs_sort(arr, k)