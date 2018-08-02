# Find All duplicates in Array

def findAllDuplicates(nums):

    output=[]

    for i in nums:
        index = abs(i) - 1
        if nums[index] < 0:
            output.append(index+1)
        nums[index] *= -1

    return output

#nums = [1, 2, 2, 1]
#nums = [4, 1, 3, 2, 5, 6]
nums = [2, 1, 3, 2, 3, 5]
print(findAllDuplicates(nums))
