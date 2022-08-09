# Merge Sort Implementation

def merge_sort(nums):

    # Base case
    if len(nums) == 1:
        return

    # Divide Phase
    middle_index = len(nums) // 2
    left_half = nums[:middle_index]
    right_half = nums[middle_index:]

    merge_sort(left_half)
    merge_sort(right_half)

    # Conquer Phase
    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j<len(right_half):
        
        if left_half[i] < right_half[j]:
            nums[k] = left_half[i]
            i = i + 1

        else:
            nums[k] = right_half[j]
            j = j + 1

        k = k + 1

    # For the additional items left in the respective left/right subarrays
    while i < len(left_half):
        nums[k] = left_half[i]
        i = i + 1
        k = k + 1

    while j < len(right_half):
        nums[k] = right_half[j]
        j = j + 1
        k = k + 1


# Testing
if __name__ == '__main__':

    x = [1,-4,0,10,5,4,3,100]
    merge_sort(x)
    print("Sorted Array:",x)
