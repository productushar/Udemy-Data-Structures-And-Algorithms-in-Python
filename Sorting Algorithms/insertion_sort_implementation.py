# Insertion Sort Implementation

def insertion_sort(nums):

    for i in range(len(nums)):
        j = i

        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j = j - 1


# Testing
if __name__ == '__main__':
    
    n = [1,-5,0,2,-1,10,9,100,56,-34]
    insertion_sort(n)
    print("Sorted Array:",n)
