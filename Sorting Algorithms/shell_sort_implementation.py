# Shell Sort Implementation

def shell_sort(nums):

    gap = len(nums) // 2

    while gap > 0:

        for i in range(gap,len(nums)):
            j = i

            while j >= gap and nums[j - gap] > nums[j]:
                nums[j - gap], nums[j] = nums[j], nums[j - gap]
                j = j - gap
                
        gap = gap // 2
        

# Testing
if __name__ == '__main__':
    
    n = [10,-4,0,3,2,1,100,-8]
    shell_sort(n)
    print("Sorted Array:",n)
