#Dutch National Flag Problem

#Given an array of 3 different values (0,1, and 2), sort it in linear running time using constant memory

def dutch_flag_problem(nums, pivot=1):
    i = 0
    j = 0
    k = len(nums)-1
    while(j<=k):
        if(nums[j]<pivot):
            swap(nums,i,j)
            i=i+1
            j=j+1
        elif(nums[j]>pivot):
            swap(nums,j,k)
            k=k-1
        else:
            j=j+1
    return nums

def swap(nums, index1, index2):
    nums[index1],nums[index2]=nums[index2],nums[index1]
