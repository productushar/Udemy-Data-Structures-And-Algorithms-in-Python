#Knutt-Morris-Pratt Substring Search Implementation

def construct_pi(pattern):

    # The table has as many values as the length of the pattern 
    pi_table = [0]*len(pattern)
    prefix_counter = 0
    i = 1

    # O(M) Linear Running Time
    while i < len(pattern):
        
        if pattern[i] == pattern[prefix_counter]:
            prefix_counter = prefix_counter + 1
            pi_table[i] = prefix_counter
            i = i + 1

        else:

            if prefix_counter!=0:
                prefix_counter = pi_table[prefix_counter - 1]

            else:
                pi_table[i] = 0
                i = i + 1

    return pi_table

def search(text, pattern):
    pi_table = construct_pi(pattern)
    
    # Index i tracks the text while index j tracks the pattern
    i = 0
    j = 0

    while i < len(text) and j < len(pattern):
        
        if text[i] == pattern[j]:
            i = i + 1
            j = j + 1

        if j == len(pattern):
            print('Pattern found at index %s' % (i-j))
            j = pi_table[j - 1]

        elif i < len(text) and text[i] != pattern[j]:

            if j != 0:
                j = pi_table[j - 1]

            else:
                i = i + 1


# Testing
if __name__ == '__main__':
    search('aacaabaab','aab')
            
