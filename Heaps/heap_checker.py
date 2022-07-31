# Challenge: Validating whether a given array is a minimum heap or not

def is_min_heap(heap):

    num_items = (len(heap)-2)//2

    for i in range(num_items):
        if(heap[i] > heap[2*i+1] or heap[i] > heap[2*i+2]):
            return False

    return True
