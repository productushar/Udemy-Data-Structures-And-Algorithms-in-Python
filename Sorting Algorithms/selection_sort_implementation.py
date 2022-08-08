# Selection Sort Implementation

def selection_sort(nums):

    for i in range(len(nums)-1):
        index = i

        for j in range(i, len(nums)):

            if nums[j] < nums[index]:
                index = j
                
        if index != i:
            nums[i], nums[index] = nums[index], nums[i]


# Testing      
if __name__ == '__main__':
    
    n = [1,-5,0,2,-1,10,9,100,56,-34]
    selection_sort(n)
    print("Sorted Array:",n)
