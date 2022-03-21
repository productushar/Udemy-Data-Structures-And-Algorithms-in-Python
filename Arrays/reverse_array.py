#Reversing 1D Array of integers
#Linear time complexity using constant memory

x = [12,6,2,1,9,10,3]

def reverse(nums):
    lowIndex = 0
    highIndex = len(nums)-1
    while(lowIndex<highIndex):
        nums[lowIndex],nums[highIndex]=nums[highIndex],nums[lowIndex]
        lowIndex+=1
        highIndex-=1
    return nums

print(reverse(x))
