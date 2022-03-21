#Trapping rainwater problem

#Find the maximum amount of water that can be trapped within a given set of bars where each bar's width is 1 unit

def trapping_water_problem(heights):
    if(len(heights)<3):
        return 0
    left_max = [0 for _ in range(len(heights))]
    right_max = [0 for _ in range(len(heights))]

    for i in range(1, len(heights)):
        left_max[i] = max(left_max[i-1],heights[i-1])

    for i in range(len(heights)-2, -1, -1):
        right_max[i]= max(right_max[i+1],heights[i+1])

    trapped = 0

    for i in range(1,len(heights)-1):
        if(min(left_max[i],right_max[i])>heights[i]):
            trapped+= min(left_max[i],right_max[i]) - heights[i]

    return trapped
